/* app/static/js/app.js */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Dark Mode Toggle Logic
  const themeToggleBtn = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
  
  const getTheme = () => {
    const saved = localStorage.getItem('theme');
    if (saved) return saved;
    return prefersDark.matches ? 'dark' : 'light';
  };
  
  const setTheme = (theme) => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
    updateThemeToggleUI(theme);
  };
  
  const updateThemeToggleUI = (theme) => {
    if (!themeToggleBtn) return;
    const sunIcon = themeToggleBtn.querySelector('.sun-icon');
    const moonIcon = themeToggleBtn.querySelector('.moon-icon');
    
    if (theme === 'dark') {
      sunIcon?.classList.remove('hidden');
      moonIcon?.classList.add('hidden');
    } else {
      sunIcon?.classList.add('hidden');
      moonIcon?.classList.remove('hidden');
    }
  };
  
  // Init theme
  const currentTheme = getTheme();
  setTheme(currentTheme);
  
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const isDark = document.documentElement.classList.contains('dark');
      setTheme(isDark ? 'light' : 'dark');
    });
  }
  
  // 2. Command Palette (Ctrl+K / Cmd+K)
  const palette = document.getElementById('command-palette');
  const paletteInput = document.getElementById('command-palette-input');
  const paletteResults = document.getElementById('command-palette-results');
  const closePaletteBtn = document.getElementById('close-palette');
  const openPaletteBtns = document.querySelectorAll('.open-palette-trigger');
  
  const togglePalette = (show) => {
    if (!palette) return;
    if (show) {
      palette.classList.remove('hidden', 'opacity-0', 'pointer-events-none');
      paletteInput.focus();
      document.body.style.overflow = 'hidden';
    } else {
      palette.classList.add('hidden', 'opacity-0', 'pointer-events-none');
      paletteInput.value = '';
      paletteResults.innerHTML = '';
      document.body.style.overflow = '';
    }
  };
  
  // Open palette
  openPaletteBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      togglePalette(true);
    });
  });
  
  // Close palette
  closePaletteBtn?.addEventListener('click', () => togglePalette(false));
  palette?.addEventListener('click', (e) => {
    if (e.target === palette) togglePalette(false);
  });
  
  // Hotkeys
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      const isHidden = palette?.classList.contains('hidden');
      togglePalette(isHidden);
    }
    if (e.key === 'Escape') {
      togglePalette(false);
    }
  });
  
  // Fuzzy search dynamic queries
  let debounceTimeout;
  paletteInput?.addEventListener('input', (e) => {
    clearTimeout(debounceTimeout);
    const query = e.target.value.trim();
    
    if (query.length < 2) {
      paletteResults.innerHTML = '<p class="text-sm text-gray-500 py-3 text-center">Type at least 2 characters to search...</p>';
      return;
    }
    
    debounceTimeout = setTimeout(() => {
      fetch(`/api/search?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {
          renderSearchResults(data);
        })
        .catch(err => {
          console.error("Search API error:", err);
          paletteResults.innerHTML = '<p class="text-sm text-red-500 py-3 text-center">Failed to fetch search results.</p>';
        });
    }, 150);
  });
  
  const renderSearchResults = (results) => {
    if (!paletteResults) return;
    if (results.length === 0) {
      paletteResults.innerHTML = '<p class="text-sm text-gray-500 py-3 text-center">No results match your query.</p>';
      return;
    }
    
    let html = '<div class="space-y-1">';
    results.forEach(item => {
      html += `
        <a href="${item.url}" class="block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition">
          <div class="flex justify-between items-center">
            <span class="font-medium text-sm text-gray-900 dark:text-gray-100">${item.title}</span>
            <span class="text-xs px-2 py-0.5 rounded bg-gray-200 dark:bg-gray-700 text-gray-600 dark:text-gray-300 font-display">${item.category}</span>
          </div>
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">${item.snippet}</p>
        </a>
      `;
    });
    html += '</div>';
    paletteResults.innerHTML = html;
  };
  
  // 3. Cookie Consent Banner
  const cookieBanner = document.getElementById('cookie-banner');
  const acceptCookieBtn = document.getElementById('accept-cookies');
  
  if (cookieBanner && !localStorage.getItem('cookies_accepted')) {
    setTimeout(() => {
      cookieBanner.classList.remove('translate-y-full');
    }, 1500);
  }
  
  acceptCookieBtn?.addEventListener('click', () => {
    localStorage.setItem('cookies_accepted', 'true');
    cookieBanner.classList.add('translate-y-full');
  });
  
  // 4. Self-dismissing Toast alerts
  const toasts = document.querySelectorAll('.toast-alert');
  toasts.forEach(toast => {
    setTimeout(() => {
      toast.classList.add('opacity-0', 'scale-95');
      setTimeout(() => toast.remove(), 300);
    }, 5000);
  });
  
  // 5. Magnetic Hover Button Interaction (subtle layout shift offset)
  const magneticButtons = document.querySelectorAll('.magnetic-btn');
  magneticButtons.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      
      btn.style.transform = `translate(${x * 0.2}px, ${y * 0.2}px)`;
    });
    
    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0px, 0px)';
    });
  });
});
