/**
 * McKinsey Search Engine for PV O&M Knowledge Hub
 * Instant full-text search with highlighting and slide deep-links
 */

(function () {
  let searchIndex = [];
  const searchInput = document.getElementById('global-search-input');
  const resultsDropdown = document.getElementById('search-results-dropdown');
  const clearBtn = document.getElementById('search-clear-btn');

  // Load search index
  async function initSearch() {
    try {
      const basePath = window.location.pathname.includes('/courses/') ? '../' : './';
      const response = await fetch(`${basePath}data/search-index.json`);
      if (response.ok) {
        searchIndex = await response.json();
      }
    } catch (err) {
      console.warn('Search index load failed:', err);
    }
  }

  // Highlight matched terms
  function highlightText(text, query) {
    if (!query) return text;
    const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
  }

  function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Perform Search
  function performSearch(query) {
    if (!query || query.trim().length === 0) {
      if (resultsDropdown) resultsDropdown.style.display = 'none';
      if (clearBtn) clearBtn.style.display = 'none';
      return;
    }

    if (clearBtn) clearBtn.style.display = 'block';

    const q = query.trim().toLowerCase();
    const terms = q.split(/\s+/).filter(Boolean);

    const matches = searchIndex.filter((item) => {
      const searchTarget = `${item.title} ${item.content} ${item.category} ${(item.tags || []).join(' ')}`.toLowerCase();
      return terms.every((term) => searchTarget.includes(term));
    });

    renderResults(matches, query);
  }

  // Render search results
  function renderResults(results, query) {
    if (!resultsDropdown) return;

    if (results.length === 0) {
      resultsDropdown.innerHTML = `
        <div class="search-results-header">
          <span>未找到與「${escapeHtml(query)}」相符的工程項目</span>
        </div>
        <div style="padding: 1.5rem; text-align: center; color: #64748B; font-size: 0.9rem;">
          建議嘗試其他關鍵字：如「熱斑」、「清洗」、「變流器」、「三相平衡」、「RSD」、「MC4」
        </div>
      `;
      resultsDropdown.style.display = 'block';
      return;
    }

    const basePath = window.location.pathname.includes('/courses/') ? '../' : './';
    let html = `
      <div class="search-results-header">
        <span>檢索結果（共 ${results.length} 筆項目）</span>
        <span>按 Esc 關閉</span>
      </div>
    `;

    results.slice(0, 8).forEach((item) => {
      const highlightedTitle = highlightText(escapeHtml(item.title), query);
      const highlightedContent = highlightText(escapeHtml(item.content.substring(0, 140)) + '...', query);
      const url = `${basePath}${item.anchor}`;

      html += `
        <a href="${url}" class="search-result-item">
          <div class="search-result-title">
            <span>${highlightedTitle}</span>
            <span style="font-size: 0.72rem; color: #0284C7; font-family: monospace;">Slide #${item.slideNo}</span>
          </div>
          <div class="search-result-meta">
            <span class="badge badge-blue">${item.category}</span>
            <span>${item.courseTitle.substring(0, 24)}...</span>
          </div>
          <div class="search-result-snippet">${highlightedContent}</div>
        </a>
      `;
    });

    resultsDropdown.innerHTML = html;
    resultsDropdown.style.display = 'block';
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Event Listeners
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      performSearch(e.target.value);
    });

    searchInput.addEventListener('focus', () => {
      if (searchInput.value.trim().length > 0) {
        performSearch(searchInput.value);
      }
    });

    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        resultsDropdown.style.display = 'none';
        clearBtn.style.display = 'none';
        searchInput.focus();
      });
    }

    // Shortcut: Ctrl+K or / to focus search
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey && e.key === 'k') || (e.key === '/' && document.activeElement !== searchInput)) {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
      } else if (e.key === 'Escape' && resultsDropdown) {
        resultsDropdown.style.display = 'none';
      }
    });

    // Close on click outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-container') && resultsDropdown) {
        resultsDropdown.style.display = 'none';
      }
    });
  }

  // Quick hint pills click handler
  document.querySelectorAll('.hint-pill').forEach((pill) => {
    pill.addEventListener('click', () => {
      const keyword = pill.getAttribute('data-keyword');
      if (searchInput && keyword) {
        searchInput.value = keyword;
        performSearch(keyword);
        searchInput.focus();
      }
    });
  });

  // Filter Buttons on Home Page
  document.querySelectorAll('.filter-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.getAttribute('data-category');
      const cards = document.querySelectorAll('.course-card');
      cards.forEach((card) => {
        if (cat === 'all' || card.getAttribute('data-category') === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Init
  initSearch();
})();
