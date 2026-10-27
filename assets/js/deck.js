/**
 * McKinsey 16:9 Slide Presentation Engine (進金生能源 6692)
 * Supports keyboard navigation, speaker notes (N), slide grid (G), fullscreen (F), and lightbox
 */

(function () {
  let currentSlide = 1;
  const totalSlides = document.querySelectorAll('.slide-item').length || 20;

  const slides = document.querySelectorAll('.slide-item');
  const counterEl = document.getElementById('slide-counter-text');
  const progressBar = document.getElementById('deck-progress-bar');
  const prevBtn = document.getElementById('deck-prev-btn');
  const nextBtn = document.getElementById('deck-next-btn');

  const notesDrawer = document.getElementById('speaker-notes-drawer');
  const notesToggleBtn = document.getElementById('notes-toggle-btn');
  const notesCloseBtn = document.getElementById('notes-close-btn');

  const overviewModal = document.getElementById('overview-modal');
  const overviewToggleBtn = document.getElementById('overview-toggle-btn');
  const overviewCloseBtn = document.getElementById('overview-close-btn');
  const overviewGrid = document.getElementById('overview-grid');

  const lightboxModal = document.getElementById('lightbox-modal');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const lightboxCloseBtn = document.getElementById('lightbox-close-btn');

  const fullscreenBtn = document.getElementById('fullscreen-btn');
  const printBtn = document.getElementById('print-btn');

  // Go to slide
  function goToSlide(slideNum) {
    if (slideNum < 1) slideNum = 1;
    if (slideNum > totalSlides) slideNum = totalSlides;

    currentSlide = slideNum;

    // Toggle active classes
    slides.forEach((slide, idx) => {
      if (idx + 1 === currentSlide) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });

    // Update counter & progress
    if (counterEl) {
      counterEl.textContent = `${currentSlide} / ${totalSlides}`;
    }
    if (progressBar) {
      progressBar.style.width = `${(currentSlide / totalSlides) * 100}%`;
    }

    // Update URL hash
    window.location.hash = `s${currentSlide}`;

    // Update speaker notes content
    updateSpeakerNotes();

    // Update overview thumbnail highlighting
    updateOverviewHighlight();
  }

  function nextSlide() {
    if (currentSlide < totalSlides) {
      goToSlide(currentSlide + 1);
    }
  }

  function prevSlide() {
    if (currentSlide > 1) {
      goToSlide(currentSlide - 1);
    }
  }

  // Speaker notes
  function updateSpeakerNotes() {
    if (!notesDrawer) return;
    const currentSlideEl = document.querySelector(`.slide-item[data-slide="${currentSlide}"]`);
    if (!currentSlideEl) return;

    const noteTakeaway = currentSlideEl.getAttribute('data-note-takeaway') || '本頁重點：依規範嚴格落實。';
    const noteDetail = currentSlideEl.getAttribute('data-note-detail') || '實務數據與補充說明：詳見相關技術手冊。';
    const noteTransition = currentSlideEl.getAttribute('data-note-transition') || '下一頁重點：進入下一核心環節。';

    const colTakeaway = document.getElementById('notes-col-takeaway');
    const colDetail = document.getElementById('notes-col-detail');
    const colTransition = document.getElementById('notes-col-transition');

    if (colTakeaway) colTakeaway.textContent = noteTakeaway;
    if (colDetail) colDetail.textContent = noteDetail;
    if (colTransition) colTransition.textContent = noteTransition;
  }

  function toggleNotes() {
    if (!notesDrawer) return;
    notesDrawer.classList.toggle('open');
    if (notesToggleBtn) {
      notesToggleBtn.classList.toggle('gold-active');
    }
  }

  // Overview Grid
  function buildOverviewGrid() {
    if (!overviewGrid) return;
    overviewGrid.innerHTML = '';
    slides.forEach((slide, idx) => {
      const slideNum = idx + 1;
      const title = slide.querySelector('.slide-action-title')?.textContent || `Slide ${slideNum}`;
      const card = document.createElement('div');
      card.className = `overview-thumb-card ${slideNum === currentSlide ? 'current' : ''}`;
      card.innerHTML = `
        <div class="thumb-card-num">PAGE ${slideNum}</div>
        <div class="thumb-card-title">${title}</div>
      `;
      card.addEventListener('click', () => {
        goToSlide(slideNum);
        toggleOverview(false);
      });
      overviewGrid.appendChild(card);
    });
  }

  function updateOverviewHighlight() {
    if (!overviewGrid) return;
    const cards = overviewGrid.querySelectorAll('.overview-thumb-card');
    cards.forEach((card, idx) => {
      if (idx + 1 === currentSlide) {
        card.classList.add('current');
      } else {
        card.classList.remove('current');
      }
    });
  }

  function toggleOverview(forceState) {
    if (!overviewModal) return;
    const isOpen = forceState !== undefined ? forceState : !overviewModal.classList.contains('open');
    if (isOpen) {
      buildOverviewGrid();
      overviewModal.classList.add('open');
    } else {
      overviewModal.classList.remove('open');
    }
  }

  // Lightbox Modal
  function openLightbox(imgSrc, captionText) {
    if (!lightboxModal || !lightboxImg) return;
    lightboxImg.src = imgSrc;
    if (lightboxCaption) {
      lightboxCaption.textContent = captionText || '原版乙級回訓實體講義投影片對照';
    }
    lightboxModal.classList.add('open');
  }

  function closeLightbox() {
    if (!lightboxModal) return;
    lightboxModal.classList.remove('open');
  }

  // Fullscreen
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch((err) => {
        console.warn('Fullscreen request failed:', err);
      });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  // Event Listeners
  if (prevBtn) prevBtn.addEventListener('click', prevSlide);
  if (nextBtn) nextBtn.addEventListener('click', nextSlide);

  if (notesToggleBtn) notesToggleBtn.addEventListener('click', toggleNotes);
  if (notesCloseBtn) notesCloseBtn.addEventListener('click', () => notesDrawer.classList.remove('open'));

  if (overviewToggleBtn) overviewToggleBtn.addEventListener('click', () => toggleOverview());
  if (overviewCloseBtn) overviewCloseBtn.addEventListener('click', () => toggleOverview(false));

  if (lightboxCloseBtn) lightboxCloseBtn.addEventListener('click', closeLightbox);
  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if (e.target === lightboxModal) closeLightbox();
    });
  }

  if (fullscreenBtn) fullscreenBtn.addEventListener('click', toggleFullscreen);
  if (printBtn) printBtn.addEventListener('click', () => window.print());

  // Attach Lightbox triggers to all preview thumbnails
  document.querySelectorAll('.open-lightbox-trigger').forEach((el) => {
    el.addEventListener('click', () => {
      const src = el.getAttribute('data-img-src') || el.querySelector('img')?.src;
      const cap = el.getAttribute('data-caption') || '原廠講義原圖對照';
      if (src) openLightbox(src, cap);
    });
  });

  // Keyboard Shortcuts
  document.addEventListener('keydown', (e) => {
    // If in search input, don't trigger slide shortcuts
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    switch (e.key) {
      case 'ArrowRight':
      case 'PageDown':
      case ' ': // Space
        e.preventDefault();
        nextSlide();
        break;
      case 'ArrowLeft':
      case 'PageUp':
      case 'Backspace':
        e.preventDefault();
        prevSlide();
        break;
      case 'Home':
        e.preventDefault();
        goToSlide(1);
        break;
      case 'End':
        e.preventDefault();
        goToSlide(totalSlides);
        break;
      case 'n':
      case 'N':
        e.preventDefault();
        toggleNotes();
        break;
      case 'g':
      case 'G':
        e.preventDefault();
        toggleOverview();
        break;
      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;
      case 'p':
      case 'P':
        if (e.ctrlKey) break; // let Ctrl+P print natively
        e.preventDefault();
        window.print();
        break;
      case 'Escape':
        if (lightboxModal?.classList.contains('open')) closeLightbox();
        else if (overviewModal?.classList.contains('open')) toggleOverview(false);
        else if (notesDrawer?.classList.contains('open')) notesDrawer.classList.remove('open');
        break;
    }
  });

  // Touch Swipe for Mobile / Tablet
  let touchStartX = 0;
  let touchEndX = 0;
  document.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  document.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    if (touchStartX - touchEndX > 50) {
      nextSlide(); // swipe left
    } else if (touchEndX - touchStartX > 50) {
      prevSlide(); // swipe right
    }
  }, { passive: true });

  // Init from URL Hash
  const hash = window.location.hash;
  if (hash && hash.startsWith('#s')) {
    const s = parseInt(hash.replace('#s', ''), 10);
    if (!isNaN(s) && s >= 1 && s <= totalSlides) {
      goToSlide(s);
    } else {
      goToSlide(1);
    }
  } else {
    goToSlide(1);
  }
})();
