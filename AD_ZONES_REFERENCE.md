# Ad Zones Reference - yt2mp3.lol

## 🎯 Your Zone IDs

| Ad Size | Zone ID | Usage |
|---------|---------|-------|
| **728x90** | 5914450 | Desktop top/bottom banners |
| **300x250** | 5914446 | Sidebar & in-content (all devices) |
| **300x100** | 5914456 | Mobile top/bottom banners |
| **300x50** | 5914454 | Mobile sticky bottom |

## 📱 Device-Specific Ad Strategy

### Mobile (< 768px)
**Maximum 3 ads per page**

1. **Top Banner** - 300x100 (Zone: 5914456)
   - Below header, above converter
   - Auto-refresh every 45 seconds

2. **Below Converter** - 300x100 (Zone: 5914456)
   - Natural break point
   - High visibility

3. **Sticky Bottom** - 300x50 (Zone: 5914454)
   - Fixed at bottom
   - User can close
   - Remembers if closed

### Desktop (≥ 1024px)
**Maximum 4 ads per page**

1. **Top Banner** - 728x90 (Zone: 5914450)
   - Below header
   - Auto-refresh every 45 seconds

2. **Below Converter** - 728x90 (Zone: 5914450)
   - High engagement area
   - Auto-refresh

3. **Sidebar Sticky** - 300x250 (Zone: 5914446)
   - Always visible on scroll
   - Auto-refresh

4. **In-Content** - 300x250 (Zone: 5914446)
   - Between content sections
   - Lazy loaded

## ✅ UX-First Features

### 1. Lazy Loading
- Ads load only when about to be visible
- Saves bandwidth
- Faster page load

### 2. Smart Refresh
- Only refreshes if user is active
- Pauses when tab is inactive
- Only refreshes visible ads
- 45-second interval (less aggressive)

### 3. Ad Limits
- Mobile: Max 3 ads
- Desktop: Max 4 ads
- Prevents ad overload

### 4. User Control
- Mobile sticky ad has close button
- Remembers user preference
- Smooth animations

### 5. No Popups/Interstitials
- Zero intrusive ads
- No forced waits
- No blocking overlays

## 🚀 Implementation Steps

### Step 1: Add CSS & JS
```html
<link rel="stylesheet" href="/assets/ads.css">
<script async src="https://a.magsrv.com/ad-provider.js"></script>
<script src="/assets/ads.js"></script>
<script>(AdProvider = window.AdProvider || []).push({"serve": {}});</script>
```

### Step 2: Add Ad Containers
```html
<!-- Top Banner -->
<div class="ad-container ad-top-banner ad-lazy ad-refresh" data-ad-type="banner-top">
  <div class="ad-label">Advertisement</div>
</div>

<!-- Below Converter -->
<div class="ad-container ad-below-converter ad-lazy ad-refresh" data-ad-type="banner-bottom">
  <div class="ad-label">Advertisement</div>
</div>

<!-- Sidebar (Desktop) -->
<div class="ad-container ad-sidebar ad-lazy ad-refresh" data-ad-type="sidebar">
  <div class="ad-label">Advertisement</div>
</div>

<!-- Mobile Sticky -->
<div class="ad-sticky-bottom ad-lazy" data-ad-type="sticky">
  <button class="ad-close-btn" aria-label="Close ad">×</button>
  <div class="ad-label">Advertisement</div>
</div>
```

### Step 3: Add body class for mobile sticky
```html
<body class="has-sticky-ad">
```

## 📊 Expected Performance

### Revenue Estimates (Conservative)

**1,000 daily users:**
- Top Banner: $6-12/day
- Below Converter: $8-15/day
- Sidebar: $5-10/day
- Mobile Sticky: $4-8/day
- **Total: $23-45/day = $690-1,350/month**

**10,000 daily users:**
- **Total: $230-450/day = $6,900-13,500/month**

### UX Metrics (Target)
- ✅ Page load time: < 2.5 seconds
- ✅ Bounce rate: < 45%
- ✅ Ad viewability: > 75%
- ✅ User complaints: < 0.5%

## 🔧 Customization

### Change Refresh Interval
Edit `web/assets/ads.js`:
```javascript
refreshInterval: 45000, // 45 seconds (current)
// Change to 60000 for 60 seconds
```

### Change Max Ads
Edit `web/assets/ads.js`:
```javascript
maxAdsPerPage: {
  mobile: 3,  // Change this
  desktop: 4  // Change this
}
```

### Disable Ads on Specific Pages
Edit `web/assets/ads.js`:
```javascript
const noAdPages = ['/privacy-policy/', '/terms-of-use/'];
// Add more pages to this array
```

## 🎨 Styling

All ad styles are in `web/assets/ads.css`. Key classes:
- `.ad-container` - Base ad container
- `.ad-top-banner` - Top banner specific
- `.ad-sidebar` - Sidebar specific
- `.ad-sticky-bottom` - Mobile sticky
- `.ad-label` - "Advertisement" label

## 📈 Monitoring

Track these metrics weekly:
1. **RPM** (Revenue per 1000 impressions)
2. **Viewability** (% of ads actually seen)
3. **CTR** (Click-through rate)
4. **Bounce Rate** (Are ads driving users away?)
5. **Page Load Time** (Keep under 3 seconds)

## ⚠️ Important Notes

1. **Never block the converter** - Users will leave
2. **Respect mobile data** - Lazy load everything
3. **Test on real devices** - Emulators aren't enough
4. **Monitor bounce rate** - If it spikes, reduce ads
5. **User experience first** - Always

## 🔄 A/B Testing Ideas

1. Test 2 vs 3 ads on mobile
2. Test refresh intervals (30s vs 45s vs 60s)
3. Test with/without sticky bottom ad
4. Test ad label text ("Advertisement" vs "Sponsored")
5. Test sidebar position (left vs right)

## 📞 Support

If ads aren't loading:
1. Check browser console for errors
2. Verify zone IDs are correct
3. Check if ad blocker is active
4. Test in incognito mode
5. Check network tab for failed requests

---

**Remember**: Happy users = repeat users = sustainable revenue 🎯
