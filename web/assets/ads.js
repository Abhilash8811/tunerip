// Ad Management System for yt2mp3.lol
// Priority: User Experience First, Revenue Second
// Note: Ad network handles auto-refresh (30s), no manual refresh needed
(function() {
  'use strict';

  // Configuration - Zone IDs for different ad sizes
  const AD_ZONES = {
    banner_728x90: '5914450',      // Desktop banner
    mobile_300x100: '5914456',     // Mobile banner large
    mobile_300x50: '5914454',      // Mobile banner small
    rectangle_300x250: '5914446',  // Sidebar/in-content
    banner_300x500: '5914458'      // Tall sidebar banner (desktop only)
  };

  const AD_CONFIG = {
    provider: 'https://a.magsrv.com/ad-provider.js',
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
    adsLoaded: 0
  };

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
      // Use tall 300x500 banner for sidebar on desktop
      if (adType === 'sidebar') {
        return AD_ZONES.banner_300x500;
      }
      return AD_ZONES.rectangle_300x250;
    }
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
    
    // Remove loading state after a delay
    setTimeout(() => {
      container.classList.remove('loading');
    }, 1000);
    
    // Trigger ad load after a short delay to ensure DOM is ready
    setTimeout(() => {
      if (window.AdProvider) {
        window.AdProvider.push({ serve: {} });
      }
    }, 100);
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
    setupStickyAdClose();
    
    // Log device type for debugging
    console.log('Ad System Initialized:', {
      device: isMobile ? 'mobile' : (isTablet ? 'tablet' : 'desktop'),
      maxAds: isMobile ? AD_CONFIG.maxAdsPerPage.mobile : AD_CONFIG.maxAdsPerPage.desktop,
      autoRefresh: 'Handled by ad network (30s)'
    });
  }

  // Expose minimal API
  window.AdManager = {
    loadAd: loadAd,
    isMobile: isMobile
  };
})();
