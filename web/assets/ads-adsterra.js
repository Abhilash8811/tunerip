// Ad Management System for yt2mp3.lol - Adsterra Integration
// Priority: User Experience First, Revenue Second
(function() {
  'use strict';

  // Adsterra Configuration - All ad zones
  const ADSTERRA_ZONES = {
    // Desktop banners (728x90)
    banner_728x90: {
      key: 'b14f8d923aebce5fa713180a7c8367a2',
      format: 'iframe',
      height: 90,
      width: 728
    },
    
    // Rectangle (300x250) - Sidebar & in-content
    rectangle_300x250: {
      key: 'cd9a18b58b4948fba1f22f6a32d732ed',
      format: 'iframe',
      height: 250,
      width: 300
    },
    
    // Mobile sticky (320x50)
    mobile_320x50: {
      key: 'cf4348e6aabf00dbeec372cda8e938bc',
      format: 'iframe',
      height: 50,
      width: 320
    },
    
    // Skyscraper (160x300)
    skyscraper_160x300: {
      key: '27d800a565a324b34bd8f1f65f784ff7',
      format: 'iframe',
      height: 300,
      width: 160
    },
    
    // Wide skyscraper (160x600)
    wide_skyscraper_160x600: {
      key: 'f3c7986a3f17b702370bfa109dd89801',
      format: 'iframe',
      height: 600,
      width: 160
    }
  };

  const AD_CONFIG = {
    maxAdsPerPage: {
      mobile: 3,  // Maximum 3 ads on mobile
      desktop: 4  // Maximum 4 ads on desktop
    },
    autoRefresh: {
      enabled: true,
      interval: 25000  // 25 seconds in milliseconds
    },
    lazyLoad: {
      enabled: true,
      rootMargin: '300px'  // Load ads 300px before they come into view
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

  // Get appropriate ad config based on device and ad type
  function getAdConfig(adType) {
    // Desktop top/bottom banners - 728x90
    if (!isMobile && (adType === 'banner-top' || adType === 'banner-bottom')) {
      return ADSTERRA_ZONES.banner_728x90;
    }
    
    // Desktop sidebar - Use wide skyscraper (160x600) for better visibility
    if (!isMobile && adType === 'sidebar') {
      return ADSTERRA_ZONES.wide_skyscraper_160x600;
    }
    
    // In-content ads - 300x250 rectangle (works on all devices)
    if (adType === 'in-content') {
      return ADSTERRA_ZONES.rectangle_300x250;
    }
    
    // Mobile top/bottom banners - Use 300x250 rectangle
    if (isMobile && (adType === 'banner-top' || adType === 'banner-bottom')) {
      return ADSTERRA_ZONES.rectangle_300x250;
    }
    
    // Mobile sticky bottom - 320x50
    if (isMobile && adType === 'sticky') {
      return ADSTERRA_ZONES.mobile_320x50;
    }
    
    return null; // No ad config for this type
  }

  // Load ads with lazy loading support
  function setupAdLoading() {
    const adContainers = document.querySelectorAll('.ad-container');
    const maxAds = isMobile ? AD_CONFIG.maxAdsPerPage.mobile : AD_CONFIG.maxAdsPerPage.desktop;
    
    if (AD_CONFIG.lazyLoad.enabled && 'IntersectionObserver' in window) {
      // Use lazy loading with IntersectionObserver
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && session.adsLoaded < maxAds) {
            loadAd(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { rootMargin: AD_CONFIG.lazyLoad.rootMargin });

      adContainers.forEach(container => {
        if (session.adsLoaded < maxAds) {
          observer.observe(container);
        }
      });
    } else {
      // Fallback: Load all ads immediately
      Array.from(adContainers).slice(0, maxAds).forEach(container => {
        loadAd(container);
      });
    }
  }

  // Load ad into container
  function loadAd(container) {
    if (container.dataset.loaded === 'true') return;
    
    const adType = container.dataset.adType;
    const adConfig = getAdConfig(adType);
    
    if (!adConfig) {
      console.log(`No Adsterra config for ad type: ${adType}`);
      return;
    }
    
    // Show loading state
    container.classList.add('loading');
    
    // Create Adsterra ad container
    const adWrapper = document.createElement('div');
    adWrapper.className = 'adsterra-ad';
    adWrapper.style.textAlign = 'center';
    
    // Create script for atOptions
    const optionsScript = document.createElement('script');
    optionsScript.textContent = `atOptions = ${JSON.stringify({
      key: adConfig.key,
      format: adConfig.format,
      height: adConfig.height,
      width: adConfig.width,
      params: {}
    })};`;
    
    // Create script for invoke.js
    const invokeScript = document.createElement('script');
    invokeScript.src = `https://www.highperformanceformat.com/${adConfig.key}/invoke.js`;
    invokeScript.async = true;
    
    // Append scripts to wrapper
    adWrapper.appendChild(optionsScript);
    adWrapper.appendChild(invokeScript);
    
    // Add wrapper to container
    container.appendChild(adWrapper);
    container.dataset.loaded = 'true';
    container.dataset.adKey = adConfig.key;
    session.adsLoaded++;
    
    // Remove loading state after a delay
    setTimeout(() => {
      container.classList.remove('loading');
    }, 1000);
    
    console.log(`✅ Adsterra ad loaded: ${adType} (${adConfig.width}x${adConfig.height})`);
    
    // Setup auto-refresh if enabled
    if (AD_CONFIG.autoRefresh.enabled) {
      setupAutoRefresh(container, adConfig);
    }
  }
  
  // Auto-refresh ad every 25 seconds
  function setupAutoRefresh(container, adConfig) {
    const refreshInterval = setInterval(() => {
      // Check if container still exists and is visible
      if (!document.body.contains(container)) {
        clearInterval(refreshInterval);
        return;
      }
      
      // Check if ad is in viewport (only refresh visible ads)
      const rect = container.getBoundingClientRect();
      const isVisible = (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
      
      if (isVisible) {
        refreshAd(container, adConfig);
      }
    }, AD_CONFIG.autoRefresh.interval);
    
    // Store interval ID for cleanup
    container.dataset.refreshInterval = refreshInterval;
  }
  
  // Refresh ad by recreating it
  function refreshAd(container, adConfig) {
    // Find and remove old ad wrapper
    const oldWrapper = container.querySelector('.adsterra-ad');
    if (oldWrapper) {
      oldWrapper.remove();
    }
    
    // Create new ad wrapper
    const adWrapper = document.createElement('div');
    adWrapper.className = 'adsterra-ad';
    adWrapper.style.textAlign = 'center';
    
    // Create script for atOptions
    const optionsScript = document.createElement('script');
    optionsScript.textContent = `atOptions = ${JSON.stringify({
      key: adConfig.key,
      format: adConfig.format,
      height: adConfig.height,
      width: adConfig.width,
      params: {}
    })};`;
    
    // Create script for invoke.js
    const invokeScript = document.createElement('script');
    invokeScript.src = `https://www.highperformanceformat.com/${adConfig.key}/invoke.js?t=${Date.now()}`;
    invokeScript.async = true;
    
    // Append scripts to wrapper
    adWrapper.appendChild(optionsScript);
    adWrapper.appendChild(invokeScript);
    
    // Add wrapper to container
    container.appendChild(adWrapper);
    
    console.log(`🔄 Ad refreshed: ${container.dataset.adType}`);
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
    setupAdLoading();
    setupStickyAdClose();
    
    // Log device type for debugging
    console.log('🎯 Adsterra Ad System Initialized:', {
      device: isMobile ? 'mobile' : (isTablet ? 'tablet' : 'desktop'),
      maxAds: isMobile ? AD_CONFIG.maxAdsPerPage.mobile : AD_CONFIG.maxAdsPerPage.desktop,
      adsLoaded: session.adsLoaded,
      lazyLoading: AD_CONFIG.lazyLoad.enabled ? 'Enabled (300px margin)' : 'Disabled',
      autoRefresh: AD_CONFIG.autoRefresh.enabled ? `Enabled (${AD_CONFIG.autoRefresh.interval/1000}s)` : 'Disabled',
      network: 'Adsterra'
    });
  }

  // Expose minimal API
  window.AdManager = {
    loadAd: loadAd,
    isMobile: isMobile,
    network: 'Adsterra'
  };

})();
