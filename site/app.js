(function () {
  var storage = {
    getItem: function (key) {
      try {
        return localStorage.getItem(key);
      } catch (e) {
        return null;
      }
    },
    setItem: function (key, value) {
      try {
        localStorage.setItem(key, value);
      } catch (e) {}
    }
  };

  var root = document.documentElement;
  var stored = storage.getItem('theme');
  if (stored) {
    root.setAttribute('data-theme', stored);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    root.setAttribute('data-theme', 'dark');
  } else {
    root.setAttribute('data-theme', 'light');
  }
  updateThemeIcon();

  var currentLang = storage.getItem('aifs-lang') || 'zh-CN';

  var i18n = {
    en: {
      tagline: "503 lessons. 20 phases. Every algorithm built from raw math before a single framework gets imported.",
      attribution: "Maintained by Rohit Ghumare and contributors. Run on your own machine.",
      finishedLessons: "Finished Lessons",
      phases: "Phases",
      languages: "Languages",
      glossaryTerms: "Glossary Terms",
      curriculum: "Curriculum · 20 phases · 503 lessons",
      tapPhase: "Tap a phase to expand its lessons. Each one ships when its math, code, and test are all written.",
      legendComplete: "Complete",
      legendInProgress: "In progress",
      legendPlanned: "Planned",
      colophonTitle: "Colophon",
      colophonText: "The entire curriculum is on GitHub. Clone it, fork it, learn at your own pace. No paywall, no signup. Every lesson has runnable code in Python, TypeScript, Rust, or Julia, depending on what fits the concept best.",
      howThisWorks: "How this works",
      preface1: "Most AI material teaches in scattered pieces. A paper here, a fine-tuning post there, a flashy agent demo somewhere else. The pieces rarely line up. You ship a chatbot but can't explain its loss curve. You hook a function to an agent but can't say what attention does inside the model that's calling it.",
      preface2: "This curriculum is the spine. 20 phases, 503 lessons, four languages: Python, TypeScript, Rust, Julia. Linear algebra at one end, autonomous swarms at the other. Every algorithm gets built from raw math first. Backprop. Tokenizer. Attention. Agent loop. By the time PyTorch shows up, you already know what it's doing under the hood.",
      preface3: "Each lesson runs the same loop: read the problem, derive the math, write the code, run the test, keep the artifact. No five-minute videos, no copy-paste deploys, no hand-holding. Free, open source, and built to run on your own laptop.",
      currentProgress: "Current Progress",
      progressSaved: "Progress saved in browser only",
      resetProgress: "Reset progress",
      review: "Review",
      read: "Read",
      completed: "completed"
    },
    'zh-CN': {
      tagline: "503 课时，20 个阶段。在导入任何框架之前，全部由手写数学公式和代码构建每一个核心 AI 算法。",
      attribution: "由 Rohit Ghumare 与众多贡献者共同维护。在您自己的本地机器上运行。",
      finishedLessons: "已完成课时",
      phases: "完成阶段",
      languages: "使用语言",
      glossaryTerms: "术语表词条",
      curriculum: "课程大纲 · 20 个阶段 · 503 课时",
      tapPhase: "点击阶段卡片展开课时列表。每个课时在其数学原理、代码实现和测试用例全部完成后即可使用。",
      legendComplete: "已完成",
      legendInProgress: "进行中",
      legendPlanned: "已计划",
      colophonTitle: "关于项目",
      colophonText: "完整课程均在 GitHub 上开源。克隆、分叉并以您自己的节奏学习。无付费墙，无需注册。每一课都包含 Python、TypeScript、Rust 或 Julia 的可运行代码，以最契合概念的语言实现。",
      howThisWorks: "教学理念",
      preface1: "大多数 AI 教程都是零散的。这里一篇论文，那里一篇微调文章，或者某个炫酷的智能体演示。这些碎片很难拼凑完整。你开发了一个聊天机器人，却无法解释它的损失曲线。你给智能体挂载了一个函数，却说不清楚调用它的模型内部，注意力机制到底在干什么。",
      preface2: "而本课程则是主干。20 个阶段，503 个课时，四种语言：Python、TypeScript、Rust、Julia。从最基础的线性代数，到最前沿的自主多智能体协作。每个算法都先从手写数学推导开始。反向传播、分词器、注意力机制、智能体循环。在 PyTorch 登场前，你已经完全看透了它底层的运作方式。",
      preface3: "每个课时都遵循同一个循环：阅读问题、推导数学、手写代码、运行测试、保留产出。没有五分钟的快餐视频，没有一键复制部署，没有保姆式教学。完全免费、开源，为在您自己的笔记本上运行而生。",
      currentProgress: "当前进度",
      progressSaved: "进度仅保存在当前浏览器",
      resetProgress: "重置所有进度",
      review: "复习",
      read: "阅读",
      completed: "已完成"
    }
  };

  function getPhases() {
    return (currentLang === 'zh-CN' && typeof PHASES_ZH !== 'undefined') ? PHASES_ZH : PHASES;
  }

  function updateStaticTranslations() {
    var t = i18n[currentLang] || i18n.en;
    
    var navLinks = document.querySelectorAll('.header-nav > a');
    if (navLinks.length >= 4) {
      navLinks[0].textContent = currentLang === 'zh-CN' ? '课程大纲' : 'Contents';
      navLinks[1].textContent = currentLang === 'zh-CN' ? '课程目录' : 'Catalog';
      navLinks[2].textContent = currentLang === 'zh-CN' ? '学习路径' : 'Roadmap';
      navLinks[3].textContent = currentLang === 'zh-CN' ? '术语表' : 'Glossary';
      if (navLinks[4]) navLinks[4].textContent = currentLang === 'zh-CN' ? '关于' : 'About';
    }

    var tagline = document.querySelector('.manual-tagline');
    if (tagline) tagline.textContent = t.tagline;
    var attr = document.querySelector('.manual-attribution');
    if (attr) attr.textContent = t.attribution;
    
    var prefaceEyebrow = document.querySelector('.preface-eyebrow');
    if (prefaceEyebrow) prefaceEyebrow.textContent = t.howThisWorks;
    var prefacePs = document.querySelectorAll('.preface-body p');
    if (prefacePs.length >= 3) {
      prefacePs[0].textContent = t.preface1;
      prefacePs[1].textContent = t.preface2;
      prefacePs[2].textContent = t.preface3;
    }

    var statRows = document.querySelectorAll('.stat-row');
    if (statRows.length >= 4) {
      statRows[0].querySelector('.stat-row-label').textContent = t.finishedLessons;
      statRows[1].querySelector('.stat-row-label').textContent = t.phases;
      statRows[2].querySelector('.stat-row-label').textContent = t.languages;
      statRows[3].querySelector('.stat-row-label').textContent = t.glossaryTerms;
    }
    var statBlockTitle = document.querySelector('.stat-block-title');
    if (statBlockTitle) statBlockTitle.textContent = t.currentProgress;

    var tocTitle = document.querySelector('.toc-title');
    if (tocTitle) {
      var totalL = getPhases().reduce(function (acc, p) { return acc + p.lessons.length; }, 0);
      tocTitle.textContent = currentLang === 'zh-CN' ? ('课程大纲 · 20 个阶段 · ' + totalL + ' 课时') : t.curriculum;
    }
    var tocSubtitle = document.querySelector('.toc-subtitle');
    if (tocSubtitle) tocSubtitle.textContent = t.tapPhase;
    var legendItems = document.querySelectorAll('.legend-item');
    if (legendItems.length >= 3) {
      legendItems[0].childNodes[1].nodeValue = ' ' + t.legendComplete;
      legendItems[1].childNodes[1].nodeValue = ' ' + t.legendInProgress;
      legendItems[2].childNodes[1].nodeValue = ' ' + t.legendPlanned;
    }

    var colophonEyebrow = document.querySelector('.colophon-eyebrow');
    if (colophonEyebrow) colophonEyebrow.textContent = t.colophonTitle;
    var colophonP = document.querySelector('.colophon-grid p');
    if (colophonP) colophonP.textContent = t.colophonText;

    var note = document.querySelector('.modal-footer-note');
    if (note) note.textContent = t.progressSaved;
    var reset = document.getElementById('modalReset');
    if (reset) reset.textContent = t.resetProgress;
  }

  document.addEventListener('DOMContentLoaded', function () {
    initThemeToggle();
    initLangToggle();
    populateStats();
    renderPhases();
    initStaggerIndex();
    initModal();
    initCopyButton();
    initSmoothScroll();
    initFadeObserver();
    initScrollExplode();
  });

  function updateThemeIcon() {
    var icon = document.getElementById('themeIcon');
    if (!icon) return;
    var theme = root.getAttribute('data-theme');
    icon.textContent = theme === 'light' ? 'N' : 'D';
  }

  function initThemeToggle() {
    var btn = document.getElementById('themeToggle');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var current = root.getAttribute('data-theme');
      var next = current === 'light' ? 'dark' : 'light';
      root.setAttribute('data-theme', next);
      storage.setItem('theme', next);
      updateThemeIcon();
    });
    updateThemeIcon();
  }

  function initLangToggle() {
    var langBtn = document.getElementById('langToggle');
    if (!langBtn) return;
    
    var updateLangButton = function() {
      langBtn.textContent = currentLang === 'zh-CN' ? 'ZH-CN' : 'EN';
    };
    
    updateLangButton();
    updateStaticTranslations();

    langBtn.addEventListener('click', function () {
      currentLang = currentLang === 'en' ? 'zh-CN' : 'en';
      storage.setItem('aifs-lang', currentLang);
      updateLangButton();
      updateStaticTranslations();
      populateStats();
      renderPhases();
    });
  }

  function computeStats() {
    var phasesList = getPhases();
    var totalLessons = 0;
    var completeLessons = 0;
    var hasProgress = !!window.AIFSProgress;
    for (var i = 0; i < phasesList.length; i++) {
      var lessons = phasesList[i].lessons;
      totalLessons += lessons.length;
      for (var j = 0; j < lessons.length; j++) {
        var staticDone = lessons[j].status === 'complete';
        var userDone = false;
        if (hasProgress && lessons[j].url) {
          var lp = window.AIFSProgress.extractPath(lessons[j].url);
          if (lp) userDone = window.AIFSProgress.isLessonComplete(lp);
        }
        if (staticDone || userDone) completeLessons++;
      }
    }
    var completePhases = 0;
    for (var p = 0; p < phasesList.length; p++) {
      if (phasesList[p].status === 'complete') completePhases++;
    }
    return {
      lessons: totalLessons,
      phases: phasesList.length,
      complete: completeLessons,
      completePhases: completePhases
    };
  }

  function setBar(selector, pct) {
    var el = document.querySelector(selector);
    if (!el) return;
    var clamped = Math.max(0, Math.min(100, pct));
    el.setAttribute('data-target-pct', clamped.toFixed(1));
    if (el.classList.contains('in-view') || !window.IntersectionObserver) {
      el.style.setProperty('--bar-pct', clamped.toFixed(1) + '%');
    } else {
      el.style.setProperty('--bar-pct', '0%');
    }
  }

  function populateStats() {
    var stats = computeStats();
    var pct = stats.lessons > 0 ? (stats.complete / stats.lessons) * 100 : 0;
    var phasePct = stats.phases > 0 ? (stats.completePhases / stats.phases) * 100 : 0;
    var glossaryCount = (typeof GLOSSARY !== 'undefined') ? GLOSSARY.length : 0;

    setText('[data-stat="complete-frac"]', stats.complete + ' / ' + stats.lessons);
    setText('[data-stat="phases-frac"]', stats.completePhases + ' / ' + stats.phases);
    setText('[data-stat="glossary-count"]', String(glossaryCount));
    setBar('[data-bar="complete"]', pct);
    setBar('[data-bar="phases"]', phasePct);
    setBar('[data-bar="languages"]', 100);
    setBar('[data-bar="glossary"]', glossaryCount > 0 ? 100 : 0);
  }

  function setText(selector, value) {
    var el = document.querySelector(selector);
    if (el) el.textContent = value;
  }

  function renderPhases() {
    var grid = document.getElementById('phasesGrid');
    if (!grid) return;
    var hasProgress = !!window.AIFSProgress;
    var html = '';
    var phasesList = getPhases();
    for (var i = 0; i < phasesList.length; i++) {
      var p = phasesList[i];
      var total = p.lessons.length;
      var done = 0;
      for (var j = 0; j < p.lessons.length; j++) {
        var staticDone = p.lessons[j].status === 'complete';
        var userDone = false;
        if (hasProgress && p.lessons[j].url) {
          var lp = window.AIFSProgress.extractPath(p.lessons[j].url);
          if (lp) userDone = window.AIFSProgress.isLessonComplete(lp);
        }
        if (staticDone || userDone) done++;
      }
      var statusClass = p.status.replace(/ /g, '-');
      var roman = toRoman(p.id);
      var num = String(p.id).padStart(2, '0');
      html += '<div class="toc-row" data-phase="' + i + '">';
      html += '<span class="toc-num">' + roman + '.</span>';
      html += '<div><span class="toc-status ' + statusClass + '"></span><span class="toc-name">' + escapeHtml(p.name) + '</span></div>';
      html += '<span class="toc-meta">' + done + ' / ' + total + '</span>';
      html += '<span class="toc-meta">' + num + '</span>';
      html += '</div>';
    }
    grid.innerHTML = html;

    initStaggerIndex();

    if (document.body.classList.contains('js-anim')) {
      var newRows = grid.querySelectorAll('.toc-row');
      for (var r = 0; r < newRows.length; r++) {
        newRows[r].classList.add('in-view', 'visible');
      }
    }
  }

  function toRoman(num) {
    var lookup = [
      ['M', 1000], ['CM', 900], ['D', 500], ['CD', 400],
      ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
      ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]
    ];
    var n = parseInt(num, 10);
    if (isNaN(n) || n <= 0) return String(num);
    var out = '';
    for (var k = 0; k < lookup.length; k++) {
      while (n >= lookup[k][1]) {
        out += lookup[k][0];
        n -= lookup[k][1];
      }
    }
    return out;
  }

  function initModal() {
    var overlay = document.getElementById('modalOverlay');
    var closeBtn = document.getElementById('modalClose');
    if (!overlay || !closeBtn) return;

    document.addEventListener('click', function (e) {
      var row = e.target.closest('.toc-row, .phase-card');
      if (row) {
        var idx = parseInt(row.getAttribute('data-phase'), 10);
        if (!isNaN(idx)) openModal(idx);
      }
    });

    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeModal();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeModal();
    });

    var resetBtn = document.getElementById('modalReset');
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        if (!window.AIFSProgress) return;
        var ok = window.confirm('Clear all your local progress (quiz answers and completed lessons)? This cannot be undone.');
        if (!ok) return;
        window.AIFSProgress.reset();
      });
    }
  }

  var currentPhaseIdx = -1;

  function openModal(idx) {
    var phasesList = getPhases();
    var p = phasesList[idx];
    if (!p) return;
    currentPhaseIdx = idx;

    document.getElementById('modalPhaseNum').textContent = 'PHASE ' + String(p.id).padStart(2, '0');
    document.getElementById('modalTitle').textContent = p.name;
    document.getElementById('modalDesc').textContent = p.desc;

    renderModalLessons(p);

    document.getElementById('modalOverlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function renderModalLessons(p) {
    var container = document.getElementById('modalLessons');
    if (!container) return;

    var hasProgress = !!window.AIFSProgress;
    var userDone = 0;
    var html = '';

    for (var i = 0; i < p.lessons.length; i++) {
      var l = p.lessons[i];
      var pathMatch = l.url ? l.url.match(/(phases\/[^/]+\/[^/]+)\/?$/) : null;
      var lessonPath = pathMatch ? pathMatch[1] : '';
      var userComplete = hasProgress && lessonPath && window.AIFSProgress.isLessonComplete(lessonPath);
      if (userComplete) userDone++;

      var statusClass = l.status.replace(/ /g, '-');
      if (userComplete) statusClass = 'complete';

      html += '<div class="modal-lesson' + (userComplete ? ' user-done' : '') + '">';
      html += '<span class="modal-lesson-status ' + statusClass + '"' + (userComplete ? ' title="You completed this lesson"' : '') + '></span>';
      if (l.url) {
        html += '<a href="' + l.url + '" target="_blank" rel="noopener">' + escapeHtml(l.name) + '</a>';
      } else {
        html += '<a>' + escapeHtml(l.name) + '</a>';
      }
      html += '<span class="modal-lesson-type" data-type="' + escapeHtml(l.type) + '"' + (l.combines ? ' title="Combines: ' + escapeHtml(l.combines) + '"' : '') + '>' + escapeHtml(l.type) + '</span>';
      html += '<span class="modal-lesson-lang">' + escapeHtml(l.lang) + '</span>';

      var actionHtml = '';
      if ((l.status === 'complete' || userComplete) && lessonPath) {
        var actionText = userComplete ? (currentLang === 'zh-CN' ? '复习' : 'Review') : (currentLang === 'zh-CN' ? '阅读' : 'Read');
        actionHtml = '<a href="lesson.html?path=' + lessonPath + '" class="modal-lesson-read">' + actionText + '</a>';
      }
      var toggleHtml = '';
      if (hasProgress && lessonPath) {
        toggleHtml = '<button type="button" class="modal-lesson-toggle' + (userComplete ? ' done' : '') + '" data-path="' + lessonPath + '" title="' + (userComplete ? 'Mark as not done' : 'Mark complete') + '" aria-label="' + (userComplete ? 'Mark as not done' : 'Mark complete') + '">' + (userComplete ? '✓' : '+') + '</button>';
      }
      html += (actionHtml || '<span class="modal-lesson-read-placeholder" aria-hidden="true"></span>') + toggleHtml;
      html += '</div>';
    }

    container.innerHTML = html;

    var toggles = container.querySelectorAll('.modal-lesson-toggle');
    for (var t = 0; t < toggles.length; t++) {
      toggles[t].addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var path = this.getAttribute('data-path');
        if (!path || !window.AIFSProgress) return;
        if (window.AIFSProgress.isLessonComplete(path)) {
          window.AIFSProgress.unmarkLessonComplete(path);
        } else {
          window.AIFSProgress.markLessonComplete(path);
        }
      });
    }

    var progEl = document.getElementById('modalProgress');
    var barEl = document.getElementById('modalProgressBar');
    var barFill = document.getElementById('modalProgressBarFill');
    if (hasProgress && p.lessons.length > 0) {
      var pct = Math.round((userDone / p.lessons.length) * 100);
      if (progEl) {
        progEl.style.display = '';
        var completedText = currentLang === 'zh-CN' ? '已完成' : 'completed';
        progEl.innerHTML = '<span class="modal-progress-count">' + userDone + ' / ' + p.lessons.length + '</span> <span class="modal-progress-label">' + completedText + '</span> <span class="modal-progress-pct">' + pct + '%</span>';
      }
      if (barEl && barFill) {
        barEl.style.display = '';
        barFill.style.width = pct + '%';
      }
    } else {
      if (progEl) progEl.style.display = 'none';
      if (barEl) barEl.style.display = 'none';
    }
  }

  if (window.AIFSProgress) {
    window.AIFSProgress.onChange(function () {
      var phasesList = getPhases();
      if (currentPhaseIdx >= 0 && phasesList[currentPhaseIdx]) {
        renderModalLessons(phasesList[currentPhaseIdx]);
      }
      populateStats();
      renderPhases();
    });
  }

  function closeModal() {
    document.getElementById('modalOverlay').classList.remove('open');
    document.body.style.overflow = '';
  }

  function initCopyButton() {
    var btn = document.getElementById('copyBtn');
    var code = document.getElementById('cloneCmd');
    if (!btn || !code) return;
    var originalLabel = btn.textContent;
    var revertTimer = null;
    btn.addEventListener('click', function () {
      navigator.clipboard.writeText(code.textContent).then(function () {
        btn.textContent = '✓';
        if (revertTimer) clearTimeout(revertTimer);
        revertTimer = setTimeout(function () { btn.textContent = originalLabel; }, 1500);
      });
    });
  }

  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
      link.addEventListener('click', function (e) {
        var target = document.querySelector(link.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth' });
        }
      });
    });
  }

  function initFadeObserver() {
    var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!window.IntersectionObserver || prefersReduced) {
      document.querySelectorAll('.reveal, .fade-in, .stat-row-bar').forEach(function (el) {
        el.classList.add('in-view', 'visible');
        var target = el.getAttribute('data-target-pct');
        if (target !== null) el.style.setProperty('--bar-pct', target + '%');
      });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          if (entry.target.classList.contains('stat-row-bar')) {
            var target = entry.target.getAttribute('data-target-pct');
            if (target !== null) entry.target.style.setProperty('--bar-pct', target + '%');
          }
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    document.querySelectorAll('.reveal, .fade-in, .stat-row-bar').forEach(function (el) {
      observer.observe(el);
    });
  }

  function initStaggerIndex() {
    var rows = document.querySelectorAll('.toc-row');
    for (var i = 0; i < rows.length; i++) {
      rows[i].style.setProperty('--stagger-index', i);
    }
  }

  function initScrollExplode() {
    var containers = document.querySelectorAll('[data-svg-explode]');
    if (!containers.length) return;
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      for (var c = 0; c < containers.length; c++) applyExplode(containers[c], 1);
      return;
    }

    var ticking = false;
    function update() {
      ticking = false;
      var vh = window.innerHeight || document.documentElement.clientHeight;
      for (var i = 0; i < containers.length; i++) {
        var rect = containers[i].getBoundingClientRect();
        var startEdge = vh;
        var endEdge = vh * 0.35;
        var raw = (startEdge - rect.top) / (startEdge - endEdge);
        var progress = Math.max(0, Math.min(1, raw));
        progress = 1 - Math.pow(1 - progress, 3);
        applyExplode(containers[i], progress);
      }
    }
    function onScroll() {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(update);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  }

  function applyExplode(container, progress) {
    // Each layer / label animates over its own window in [stagger_start, stagger_start + window].
    // Sequential reveal: layer N waits for layer N-1 to mostly settle before starting.
    var STAGGER_DENOM = 720; // higher → wider gaps between layer entrances
    var WINDOW = 0.55;       // each layer's local animation duration as fraction of global progress

    function localProgress(staggerAttr) {
      var stagger = parseFloat(staggerAttr) || 0;
      var start = stagger / STAGGER_DENOM;
      var local = (progress - start) / WINDOW;
      if (local < 0) local = 0;
      if (local > 1) local = 1;
      // ease-out cubic on the local segment
      return 1 - Math.pow(1 - local, 3);
    }

    var layers = container.querySelectorAll('.explode-layer');
    for (var i = 0; i < layers.length; i++) {
      var final = parseFloat(layers[i].getAttribute('data-final')) || 0;
      var lp = localProgress(layers[i].getAttribute('data-stagger'));
      var dy = -final * lp;
      layers[i].setAttribute('transform', 'translate(0, ' + dy.toFixed(2) + ')');
      layers[i].setAttribute('opacity', lp.toFixed(3));
    }
    var labels = container.querySelectorAll('.explode-label');
    for (var j = 0; j < labels.length; j++) {
      var final2 = parseFloat(labels[j].getAttribute('data-final')) || 0;
      var lp2 = localProgress(labels[j].getAttribute('data-stagger'));
      var dy2 = -final2 * lp2;
      labels[j].setAttribute('transform', 'translate(0, ' + dy2.toFixed(2) + ')');
      labels[j].setAttribute('opacity', lp2.toFixed(3));
    }
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str == null ? '' : str;
    return div.innerHTML;
  }
})();
