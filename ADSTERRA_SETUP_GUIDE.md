# Adsterra Integration Guide

## ✅ Current Status

Adsterra ad network is now integrated! The system is ready to display ads.

## 🧪 Testing

### Step 1: Test Direct Ad Code

Visit: **https://yt2mp3.lol/test-adsterra.html**

This test page shows:
1. **Direct Adsterra code** - Should work immediately if your account is approved
2. **Our ad system** - Should work if the integration is correct
3. **Debug tools** - Click "Run Debug Check" to see system status

### Step 2: Check Console

Open browser console (F12) and look for:

```
🎯 Adsterra Ad System Initialized: {
  device: "desktop",
  maxAds: 4,
  adsLoaded: 1,
  network: "Adsterra"
}
```

And:

```
✅ Adsterra ad loaded: banner-top (728x90)
```

### Step 3: Verify Ads Display

- ✅ **If you see actual ads** → Everything is working!
- ⚠️ **If you see "Advertisement" label only** → Check Adsterra dashboard
- ❌ **If you see errors in console** → Check the error message

## 📋 Current Ad Zones

| Location | Size | Adsterra Key | Status |
|----------|------|--------------|--------|
| Top Banner (Desktop) | 728×90 | b14f8d923aebce5fa713180a7c8367a2 | ✅ Configured |
| Below Converter | - | Not added yet | ⏳ Pending |
| Sidebar | - | Not added yet | ⏳ Pending |
| Mobile Banner | - | Not added yet | ⏳ Pending |
| Sticky Bottom | - | Not added yet | ⏳ Pending |

## 🔧 Adding More Ad Zones

### Step 1: Get Ad Code from Adsterra

1. Log into your Adsterra dashboard
2. Create a new ad unit (e.g., 300×250 for sidebar)
3. Copy the ad code, which looks like:

```html
<script>
atOptions = {
  'key' : 'YOUR_KEY_HERE',
  'format' : 'iframe',
  'height' : 250,
  'width' : 300,
  'params' : {}
};
</script>
<script src="https://www.highperformanceformat.com/YOUR_KEY_HERE/invoke.js"></script>
```

### Step 2: Add to ads-adsterra.js

Open `web/assets/ads-adsterra.js` and add your new zone to the `ADSTERRA_ZONES` object:

```javascript
const ADSTERRA_ZONES = {
  // Existing zone
  banner_728x90: {
    key: 'b14f8d923aebce5fa713180a7c8367a2',
    format: 'iframe',
    height: 90,
    width: 728
  },
  
  // NEW: Add your zone here
  rectangle_300x250: {
    key: 'YOUR_KEY_HERE',  // From Adsterra
    format: 'iframe',
    height: 250,
    width: 300
  },
  
  // For mobile banners
  mobile_300x100: {
    key: 'YOUR_MOBILE_KEY_HERE',
    format: 'iframe',
    height: 100,
    width: 300
  }
};
```

### Step 3: Update getAdConfig Function

Update the `getAdConfig()` function to map ad types to your zones:

```javascript
function getAdConfig(adType) {
  // Desktop banners (728x90)
  if (!isMobile && (adType === 'banner-top' || adType === 'banner-bottom')) {
    return ADSTERRA_ZONES.banner_728x90;
  }
  
  // Desktop sidebar (300x250)
  if (!isMobile && adType === 'sidebar') {
    return ADSTERRA_ZONES.rectangle_300x250;
  }
  
  // Mobile banners (300x100)
  if (isMobile && (adType === 'banner-top' || adType === 'banner-bottom')) {
    return ADSTERRA_ZONES.mobile_300x100;
  }
  
  // In-content ads (300x250)
  if (adType === 'in-content') {
    return ADSTERRA_ZONES.rectangle_300x250;
  }
  
  return null;
}
```

### Step 4: Test

1. Save the file
2. Clear browser cache (Ctrl+Shift+Delete)
3. Reload the page (Ctrl+F5)
4. Check console for: `✅ Adsterra ad loaded: [ad-type]`

## 📱 Recommended Ad Zones to Create

Create these ad units in your Adsterra dashboard:

### Desktop
1. ✅ **728×90 Banner** - Already configured
2. ⏳ **300×250 Rectangle** - For sidebar and in-content
3. ⏳ **300×600 Half Page** - For sidebar (optional, higher revenue)

### Mobile
1. ⏳ **300×100 Banner** - For top/bottom banners
2. ⏳ **300×250 Rectangle** - For in-content
3. ⏳ **320×50 Banner** - For sticky bottom

## 🎯 Ad Placement Strategy

### Desktop (4 ads max)
1. **Top Banner** - 728×90 (after header)
2. **Below Converter** - 728×90 (after hero section)
3. **Sidebar** - 300×250 or 300×600 (sticky)
4. **In-Content** - 300×250 (between sections)

### Mobile (3 ads max)
1. **Top Banner** - 300×100 (after header)
2. **Below Converter** - 300×100 (after converter)
3. **Sticky Bottom** - 320×50 (fixed at bottom, closeable)

## 🔍 Troubleshooting

### Ads not showing?

**Check 1: Adsterra Account**
- Is your account approved?
- Are the ad units active?
- Is your site verified?

**Check 2: Console Errors**
```javascript
// Run in console
console.log({
  AdManager: typeof window.AdManager,
  network: window.AdManager?.network,
  containers: document.querySelectorAll('.ad-container').length,
  loaded: document.querySelectorAll('[data-loaded="true"]').length
});
```

**Check 3: Ad Code**
- Is the key correct?
- Is the invoke.js URL correct?
- Are there any typos?

**Check 4: Browser**
- Disable ad blocker
- Clear cache
- Try incognito mode

### Wrong ad size showing?

Check the `getAdConfig()` function - make sure the ad type is mapped to the correct zone.

### Ads showing on wrong device?

Check the device detection:
```javascript
console.log({
  isMobile: window.AdManager.isMobile,
  windowWidth: window.innerWidth
});
```

## 📊 Performance Tips

1. **Use appropriate sizes** - Don't use 728×90 on mobile
2. **Limit ad count** - Max 3 on mobile, 4 on desktop
3. **Test different placements** - See what works best
4. **Monitor fill rate** - Check Adsterra dashboard for stats

## 🚀 Going Live on All Pages

Once ads are working on the test page:

1. The main index.html already uses ads-adsterra.js
2. Update all other HTML files to use ads-adsterra.js:
   - Replace `ads.js` with `ads-adsterra.js` in script tags
   - Remove old ad provider scripts

Or run this command to update all files:
```bash
# Find and replace in all HTML files
find web -name "*.html" -type f -exec sed -i 's/ads\.js/ads-adsterra.js/g' {} \;
```

## 📞 Need Help?

1. **Check test page**: /test-adsterra.html
2. **Check console**: F12 → Console tab
3. **Check Adsterra dashboard**: Verify account status
4. **Check documentation**: Adsterra support docs

---

**Last Updated:** April 30, 2026
**Ad Network:** Adsterra
**Status:** ✅ Ready for testing
