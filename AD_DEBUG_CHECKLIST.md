# Ad Loading Debug Checklist

## 🔍 Quick Debug Steps

Use these steps to verify ads are loading correctly on your site.

### Step 1: Open Browser Console

1. Open your site: https://yt2mp3.lol
2. Press **F12** to open Developer Tools
3. Go to **Console** tab

### Step 2: Check for Errors

Look for any red error messages. Common issues:

❌ **"Failed to load resource: ad-provider.js"**
- Ad network script is blocked or unavailable
- Check if ad blocker is enabled

❌ **"AdProvider is not defined"**
- Ad provider script didn't load
- Check network tab for failed requests

✅ **No errors = Good!**

### Step 3: Verify Scripts Loaded

In the Console, type these commands:

```javascript
// Check if AdProvider exists
console.log(window.AdProvider);
// Should show: Array or Object (not undefined)

// Check if ads.js loaded
console.log(window.AdManager);
// Should show: Object with loadAd and isMobile properties

// Check how many ad containers exist
console.log(document.querySelectorAll('.ad-container').length);
// Should show: 3-4 (depending on device)

// Check how many ads were loaded
console.log(document.querySelectorAll('[data-loaded="true"]').length);
// Should show: 3-4 (same as containers)

// Check if ins tags were created
console.log(document.querySelectorAll('ins.eas6a97888e2').length);
// Should show: 3-4 (one per ad container)

// Check zone IDs being used
document.querySelectorAll('ins.eas6a97888e2').forEach(ins => {
  console.log('Zone ID:', ins.getAttribute('data-zoneid'));
});
// Should show your zone IDs: 5914450, 5914446, 5914458, etc.
```

### Step 4: Check Network Tab

1. Go to **Network** tab in DevTools
2. Reload the page (Ctrl+R or Cmd+R)
3. Look for these requests:

✅ **ad-provider.js** - Status 200 (loaded successfully)
✅ **ads.css** - Status 200
✅ **ads.js** - Status 200

If any show **Status 404** or **Failed**, there's a problem with file paths.

### Step 5: Inspect Ad Containers

In the Console, run:

```javascript
// Get detailed info about each ad container
document.querySelectorAll('.ad-container').forEach((container, index) => {
  console.log(`Ad ${index + 1}:`, {
    type: container.dataset.adType,
    loaded: container.dataset.loaded,
    zoneId: container.dataset.zoneId,
    hasIns: container.querySelector('ins') !== null,
    visible: container.offsetHeight > 0
  });
});
```

**Expected output for each ad:**
```javascript
{
  type: "banner-top",
  loaded: "true",
  zoneId: "5914450",
  hasIns: true,
  visible: true
}
```

### Step 6: Check Ad Network Response

The ad network should inject content into the `<ins>` tags. Check if this happened:

```javascript
// Check if ad network added content
document.querySelectorAll('ins.eas6a97888e2').forEach((ins, index) => {
  console.log(`Ad ${index + 1} content:`, {
    zoneId: ins.getAttribute('data-zoneid'),
    hasChildren: ins.children.length > 0,
    innerHTML: ins.innerHTML.substring(0, 100) // First 100 chars
  });
});
```

**If `hasChildren: false` or `innerHTML` is empty:**
- Ad network hasn't filled the ad yet
- Could be due to:
  - Account not approved
  - Zone not active
  - No ad inventory available
  - Geographic restrictions

### Step 7: Check Lazy Loading

Scroll down the page and watch the Console. You should see:

```
Ad System Initialized: {device: "desktop", maxAds: 4, autoRefresh: "Handled by ad network (30s)"}
```

### Step 8: Mobile Testing

1. Open DevTools
2. Click the **device toggle** icon (or press Ctrl+Shift+M)
3. Select a mobile device (e.g., iPhone 12)
4. Reload the page
5. Check Console for:

```javascript
console.log(window.AdManager.isMobile);
// Should show: true
```

## 🐛 Common Issues & Solutions

### Issue: "ADVERTISEMENT" placeholder shows but no actual ad

**Possible causes:**
1. ✅ **Account pending approval** - Wait for ad network approval
2. ✅ **Zone not activated** - Check ad network dashboard
3. ✅ **No ad inventory** - Ad network has no ads to serve
4. ✅ **Geographic restrictions** - Ads may not serve in your location
5. ✅ **Low traffic** - Some networks require minimum traffic

**Solution:** Check your ad network dashboard for account status and zone activation.

### Issue: Console shows "AdProvider is not defined"

**Cause:** Ad provider script didn't load

**Solution:**
```javascript
// Check if script tag exists
console.log(document.querySelector('script[src*="ad-provider.js"]'));
// Should show: <script> element

// Check if it loaded
console.log(window.AdProvider);
// Should NOT be undefined
```

If undefined, check:
- Ad blocker is disabled
- Script URL is correct: `https://a.magsrv.com/ad-provider.js`
- Network connection is working

### Issue: No ins tags created

**Cause:** ads.js didn't run or failed

**Solution:**
```javascript
// Check if ads.js loaded
console.log(window.AdManager);
// Should show: Object

// Manually trigger ad load (for testing)
document.querySelectorAll('.ad-container').forEach(container => {
  if (window.AdManager && window.AdManager.loadAd) {
    window.AdManager.loadAd(container);
  }
});
```

### Issue: Ads show on desktop but not mobile

**Cause:** Device detection issue

**Solution:**
```javascript
// Check device detection
console.log({
  isMobile: window.AdManager.isMobile,
  windowWidth: window.innerWidth,
  expected: window.innerWidth < 768 ? 'mobile' : 'desktop'
});
```

### Issue: Too many ads showing

**Cause:** Ad limit not enforced

**Solution:**
```javascript
// Check ad limit
console.log({
  adsLoaded: document.querySelectorAll('[data-loaded="true"]').length,
  maxAllowed: window.AdManager.isMobile ? 3 : 4
});
```

## ✅ Success Indicators

Your ads are working correctly if:

1. ✅ No console errors
2. ✅ `window.AdProvider` exists
3. ✅ `window.AdManager` exists
4. ✅ All ad containers have `data-loaded="true"`
5. ✅ All ad containers have `<ins>` tags with zone IDs
6. ✅ Ad network has injected content into `<ins>` tags
7. ✅ Ads are visible on the page (not just placeholders)

## 📞 Still Not Working?

If ads still don't show after all checks:

1. **Contact ad network support** with:
   - Your site URL
   - Zone IDs you're using
   - Console output from Step 5 above
   - Screenshot of Network tab

2. **Verify account status** in ad network dashboard:
   - Account approved?
   - Zones active?
   - Payment info added?
   - Site verified?

3. **Test with different zone IDs** - Try creating a test zone in your dashboard

4. **Check ad network status** - Visit their status page to see if there are any outages

---

**Last Updated:** April 30, 2026

**Need Help?** Check the ad network's documentation or support forum.
