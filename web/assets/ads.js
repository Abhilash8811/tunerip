// Ad Management System for yt2mp3.lol
// Priority: User Experience First, Revenue Second
(function() {
  'use strict';

  // Configuration - Zone IDs for different ad sizes
  const AD_ZONES = {
    banner_728x90: '5914450',      // Desktop banner
    mobile_300x100: '5914456',     // Mobile banner large
    mobile_300x50: '5914454',      // Mobile banner small
    rectangle_300x250: '5914446'   // Sidebar/in-content
  };

  const AD_CONFIG = {
    provider: 'https://a.magsrv.com/ad-provider.js',
    refreshInterval: 45000, // 45 seconds (less aggressive)
    lazyLoadMargin: '300px', // Load earlier for smoother experience
    maxAdsPerPage: {
      mobile: 3,  // Maximum 3 ads on mobile
      desktop: 4  // Maximum 4 ads on desktop
    }
  };

  // Detect device type
  const isMobile = window.innerWidth < 768;
  const isTablet = window.innerWidth >= 768 && window.innerWidth < 1024;
  const isDesktop = window.innerWidth >= 1024;

  // Track session
  const session = {
    lastActivity: Date.now(),
    adsLoaded: 0
  };

  // Update last activity
  ['mousemove', 'scroll', 'keypress', 'click', 'touchstart'].forEach(event => {
    document.addEventListener(event, () => {
      session.lastActivity = Date.now();
    }, { passive: true });
  });

  // Check if user is active
  function isUserActive() {
    return Date.now() - session.lastActivity < 10000 && !document.hidden;
  }

  // Get appropriate zone ID based on device and ad type
  function getZoneId(adType) {
    if (isMobile) {
      if (adType === 'banner-top' || adType === 'banner-bottom') {
        return AD_ZONES.mobile_300x100;
      }
      if (adType === 'sticky') {
        return AD_ZONES.mobile_300x50;
      }
      return AD_ZONES.rectangle_300x250;
    } else {
      if (adType === 'banner-top' || adType === 'banner-bottom') {
        return AD_ZONES.banner_728x90;
      }
      return AD_ZONES.rectangle_300x250;
    }
  }

  // Lazy load ads
  function setupLazyLoading() {
    const adContainers = document.querySelectorAll('.ad-lazy');
    const maxAds = isMobile ? AD_CONFIG.maxAdsPerPage.mobile : AD_CONFIG.maxAdsPerPage.desktop;
    
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && session.adsLoaded < maxAds) {
            loadAd(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { rootMargin: AD_CONFIG.lazyLoadMargin });

      adContainers.forEach(container => observer.observe(container));
    } else {
      // Fallback for older browsers
      Array.from(adContainers).slice(0, maxAds).forEach(container => loadAd(container));
    }
  }

  // Load ad into container
  function loadAd(container) {
    if (container.dataset.loaded === 'true') return;
    
    const adType = container.dataset.adType;
    const zoneId = getZoneId(adType);
    
    // Show loading state
    container.classList.add('loading');
    
    // Create ad insertion point
    const ins = document.createElement('ins');
    ins.className = 'eas6a97888e2';
    ins.setAttribute('data-zoneid', zoneId);
    
    container.appendChild(ins);
    container.dataset.loaded = 'true';
    container.dataset.zoneId = zoneId;
    session.adsLoaded++;
    
    // Trigger ad load
    if (window.AdProvider) {
      window.AdProvider.push({ serve: {} });
    }
    
    // Remove loading state after a delay
    setTimeout(() => {
      container.classList.remove('loading');
    }, 1000);
  }

  // Setup ad refresh (only for non-intrusive ads)
  function setupAdRefresh() {
    const refreshableAds = document.querySelectorAll('.ad-refresh');
    
    refreshableAds.forEach(ad => {
      setInterval(() => {
        // Only refresh if user is active and ad is visible
        if (isUserActive() && ad.dataset.loaded === 'true' && isElementInViewport(ad)) {
          const ins = ad.querySelector('ins');
          if (ins && window.AdProvider) {
            // Refresh ad
            ins.remove();
            const newIns = document.createElement('ins');
            newIns.className = 'eas6a97888e2';
            newIns.setAttribute('data-zoneid', ad.dataset.zoneId);
            ad.appendChild(newIns);
            window.AdProvider.push({ serve: {} });
          }
        }
      }, AD_CONFIG.refreshInterval);
    });
  }

  // Check if element is in viewport
  function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  // Close mobile sticky ad
  function setupStickyAdClose() {
    const stickyAd = document.querySelector('.ad-sticky-bottom');
    if (!stickyAd) return;

    const closeBtn = stickyAd.querySelector('.ad-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        stickyAd.style.transform = 'translateY(100%)';
        setTimeout(() => {
          stickyAd.style.display = 'none';
          document.body.classList.remove('has-sticky-ad');
        }, 300);
        sessionStorage.setItem('sticky_ad_closed', 'true');
      });
    }

    // Don't show if user closed it before
    if (sessionStorage.getItem('sticky_ad_closed') === 'true') {
      stickyAd.style.display = 'none';
      document.body.classList.remove('has-sticky-ad');
    }
  }

  // Hide ads on specific pages if needed
  function checkPageType() {
    const path = window.location.pathname;
    const noAdPages = ['/privacy-policy/', '/terms-of-use/'];
    
    if (noAdPages.some(page => path.includes(page))) {
      document.querySelectorAll('.ad-container').forEach(ad => {
        ad.style.display = 'none';
      });
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    checkPageType();
    setupLazyLoading();
    setupAdRefresh();
    setupStickyAdClose();
    
    // Log device type for debugging
    console.log('Ad System Initialized:', {
      device: isMobile ? 'mobile' : (isTablet ? 'tablet' : 'desktop'),
      maxAds: isMobile ? AD_CONFIG.maxAdsPerPage.mobile : AD_CONFIG.maxAdsPerPage.desktop
    });
  }

  // Expose minimal API
  window.AdManager = {
    loadAd: loadAd,
    isMobile: isMobile
  };
})();
