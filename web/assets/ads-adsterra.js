// Ad Management System for yt2mp3.lol - Adsterra Integration
// Priority: User Experience First, Revenue Second
(function() {
  'use strict';

  // Adsterra Configuration - Add your ad codes here
  const ADSTERRA_ZONES = {
    // Desktop banners (728x90)
    banner_728x90: {
      key: 'b14f8d923aebce5fa713180a7c8367a2',
      format: 'iframe',
      height: 90,
      width: 728
    },
    // Add more zones as you get them from Adsterra
    // Example for 300x250:
    // rectangle_300x250: {
    //   key: 'YOUR_KEY_HERE',
    //   format: 'iframe',
    //   height: 250,
    //   width: 300
    // }
  };

  const AD_CONFIG = {
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

  // Get appropriate ad config based on device and ad type
  function getAdConfig(adType) {
    // For now, use 728x90 banner for desktop banners
    if (!isMobile && (adType === 'banner-top' || adType === 'banner-bottom')) {
      return ADSTERRA_ZONES.banner_728x90;
    }
    
    // Add more mappings as you get more zone codes
    // For mobile, sidebar, etc.
    
    return null; // No ad config for this type yet
  }

  // Load ads immediately
  function setupAdLoading() {
    const adContainers = document.querySelectorAll('.ad-container');
    const maxAds = isMobile ? AD_CONFIG.maxAdsPerPage.mobile : AD_CONFIG.maxAdsPerPage.desktop;
    
    // Load all ads immediately
    Array.from(adContainers).slice(0, maxAds).forEach(container => {
      loadAd(container);
    });
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
