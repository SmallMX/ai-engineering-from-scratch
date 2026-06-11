---
name: skill-image-text-retriever
description: 开放词表视觉：CLIP 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 18
tags: [clip, retrieval, faiss, zero-shot]
---

# 开放词表视觉：CLIP：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**开放词表视觉：CLIP**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- CLIP 用对比学习对齐图像和文本 embedding。
- zero-shot classification 通过文本 prompt 构造类别原型。
- image-text retrieval 使用共享 embedding space 排序。
- prompt wording 会影响开放词表性能。
- CLIP 擅长语义对齐，但可能忽略细粒度定位。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-image-text-retriever
description: Build an image embedding index with any CLIP checkpoint; support query-by-text and query-by-image
version: 1.0.0
phase: 4
lesson: 18
tags: [clip, retrieval, faiss, zero-shot]
---

# Image-Text Retriever

Turn a folder of images into a searchable index using CLIP embeddings.

## When to use

- Building a zero-shot image search on an internal catalog.
- Deduplicating near-identical images by embedding distance.
- Building a quick "find similar" component without a labelled dataset.

## Inputs

- `image_folder`: directory of image files.
- `clip_model`: HuggingFace id like `openai/clip-vit-base-patch32` or `google/siglip-base-patch16-224`.
- `index_type`: flat | IVF | HNSW.
- `embedding_dim`: inferred from the model.

## Steps

1. Load the CLIP model and preprocessor.
2. Batch-encode every image in the folder. Save embeddings as (N, D) float32 + filename list.
3. Build a FAISS index over the embeddings. Use inner-product on L2-normalised vectors for cosine similarity.
4. Expose two query interfaces:
   - `search_by_text(text, k)` — embed the text, search.
   - `search_by_image(image_path, k)` — embed the image, search.

## Output template

``\`python
import os
import glob
import numpy as np
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor
import faiss


class ImageTextRetriever:
    def __init__(self, model_name="openai/clip-vit-base-patch32"):
        self.model = CLIPModel.from_pretrained(model_name).eval()
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.dim = self.model.config.projection_dim
        self.index = None
        self.filenames = []

    @torch.no_grad()
    def _encode_images(self, paths, batch=16):
        embs = []
        for i in range(0, len(paths), batch):
            imgs = [Image.open(p).convert("RGB") for p in paths[i:i + batch]]
            inputs = self.processor(images=imgs, return_tensors="pt")
            out = self.model.get_image_features(**inputs)
            out = out / out.norm(dim=-1, keepdim=True)
            embs.append(out.cpu().numpy())
        return np.concatenate(embs).astype(np.float32)

    @torch.no_grad()
    def _encode_text(self, texts):
        inputs = self.processor(text=texts, return_tensors="pt", padding=True)
        out = self.model.get_text_features(**inputs)
        out = out / out.norm(dim=-1, keepdim=True)
        return out.cpu().numpy().astype(np.float32)

    def build_index(self, folder, index_type="flat"):
        exts = ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.bmp")
        files = []
        for ext in exts:
            files.extend(glob.glob(os.path.join(folder, ext)))
        self.filenames = sorted(files)
        embs = self._encode_images(self.filenames)
        if index_type == "IVF":
            quantizer = faiss.IndexFlatIP(self.dim)
            nlist = min(256, max(4, len(embs) // 32))
            self.index = faiss.IndexIVFFlat(quantizer, self.dim, nlist)
            self.index.train(embs)
        elif index_type == "HNSW":
            self.index = faiss.IndexHNSWFlat(self.dim, 32, faiss.METRIC_INNER_PRODUCT)
        else:
            self.index = faiss.IndexFlatIP(self.dim)
        self.index.add(embs)

    def search_by_text(self, text, k=5):
        q = self._encode_text([text])
        dist, idx = self.index.search(q, k)
        return [(self.filenames[i], float(d)) for d, i in zip(dist[0], idx[0])]

    def search_by_image(self, image_path, k=5):
        q = self._encode_images([image_path])
        dist, idx = self.index.search(q, k)
        return [(self.filenames[i], float(d)) for d, i in zip(dist[0], idx[0])]
``\`

## Report

``\`
[retriever]
  model:          <name>
  num_images:     <int>
  dim:            <int>
  index_type:     flat | IVF | HNSW
  index_size_mb:  <float>
``\`

## Rules

- Always L2-normalise embeddings before indexing; FAISS's inner product on normalised vectors equals cosine similarity.
- For < 100k images, `IndexFlatIP` (exact) is simplest and fastest.
- For 100k-10M, `IndexIVFFlat` is the standard trade-off.
- For > 10M, use HNSW or a product-quantised variant.
- Never rebuild the index on every query; embed once, search many times.

```
