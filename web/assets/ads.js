// Ad Management System for yt2mp3.lol
(function() {
  'use strict';

  // Configuration
  const AD_CONFIG = {
    zoneId: '5914446', // Your zone ID
    provider: 'https://a.magsrv.com/ad-provider.js',
    refreshInterval: 30000, // 30 seconds
    lazyLoadMargin: '200px',
    maxInterstitialPerSession: 1
  };

  // Track session
  const session = {
    interstitialShown: parseInt(sessionStorage.getItem('interstitial_shown') || '0'),
    lastActivity: Date.now()
  };

  // Update last activity
  ['mousemove', 'scroll', 'keypress', 'click', 'touchstart'].forEach(event => {
    document.addEventListener(event, () => {
      session.lastActivity = Date.now();
    }, { passive: true });
  });

  // Check if user is active
  function isUserActive() {
    return Date.now() - session.lastActivity < 5000 && !document.hidden;
  }

  // Lazy load ads
  function setupLazyLoading() {
    const adContainers = document.querySelectorAll('.ad-lazy');
    
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            loadAd(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { rootMargin: AD_CONFIG.lazyLoadMargin });

      adContainers.forEach(container => observer.observe(container));
    } else {
      // Fallback for older browsers
      adContainers.forEach(container => loadAd(container));
    }
  }

  // Load ad into container
  function loadAd(container) {
    if (container.dataset.loaded === 'true') return;
    
    const adType = container.dataset.adType;
    const zoneId = container.dataset.zoneId || AD_CONFIG.zoneId;
    
    // Create ad insertion point
    const ins = document.createElement('ins');
    ins.className = 'eas6a97888e2';
    ins.setAttribute('data-zoneid', zoneId);
    
    container.appendChild(ins);
    container.dataset.loaded = 'true';
    
    // Trigger ad load
    if (window.AdProvider) {
      window.AdProvider.push({ serve: {} });
    }
  }

  // Setup ad refresh
  function setupAdRefresh() {
    const refreshableAds = document.querySelectorAll('.ad-refresh');
    
    refreshableAds.forEach(ad => {
      setInterval(() => {
        if (isUserActive() && ad.dataset.loaded === 'true') {
          // Refresh logic - depends on your ad network
          const ins = ad.querySelector('ins');
          if (ins && window.AdProvider) {
            // Re-trigger ad load
            window.AdProvider.push({ serve: {} });
          }
        }
      }, AD_CONFIG.refreshInterval);
    });
  }

  // Show interstitial ad
  function showInterstitial() {
    if (session.interstitialShown >= AD_CONFIG.maxInterstitialPerSession) {
      return;
    }

    // Create interstitial container
    const overlay = document.createElement('div');
    overlay.className = 'ad-interstitial-overlay';
    overlay.innerHTML = `
      <div class="ad-interstitial-container">
        <button class="ad-interstitial-close" aria-label="Close ad">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        <div class="ad-interstitial-content" data-ad-type="interstitial" data-zone-id="${AD_CONFIG.zoneId}"></div>
      </div>
    `;

    document.body.appendChild(overlay);
    document.body.style.overflow = 'hidden';

    // Load ad
    loadAd(overlay.querySelector('.ad-interstitial-content'));

    // Close button
    const closeBtn = overlay.querySelector('.ad-interstitial-close');
    let canClose = false;
    
    // Allow closing after 3 seconds
    setTimeout(() => {
      canClose = true;
      closeBtn.style.opacity = '1';
      closeBtn.style.pointerEvents = 'auto';
    }, 3000);

    closeBtn.addEventListener('click', () => {
      if (canClose) {
        overlay.remove();
        document.body.style.overflow = '';
      }
    });

    // Track that we showed it
    session.interstitialShown++;
    sessionStorage.setItem('interstitial_shown', session.interstitialShown);
  }

  // Show interstitial after conversion completes
  window.addEventListener('conversionComplete', () => {
    setTimeout(showInterstitial, 1000);
  });

  // Close mobile sticky ad
  function setupStickyAdClose() {
    const stickyAd = document.querySelector('.ad-sticky-bottom');
    if (!stickyAd) return;

    const closeBtn = stickyAd.querySelector('.ad-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        stickyAd.style.display = 'none';
        sessionStorage.setItem('sticky_ad_closed', 'true');
      });
    }

    // Don't show if user closed it before
    if (sessionStorage.getItem('sticky_ad_closed') === 'true') {
      stickyAd.style.display = 'none';
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    setupLazyLoading();
    setupAdRefresh();
    setupStickyAdClose();
  }

  // Expose API
  window.AdManager = {
    showInterstitial: showInterstitial,
    loadAd: loadAd
  };
})();
