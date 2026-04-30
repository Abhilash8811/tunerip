# Ad System Testing Guide

## 🧪 Quick Testing Checklist

Use this guide to verify ads are working correctly after deployment.

## 1. Desktop Testing (≥1024px)

### Open any page on desktop browser

**Expected Ad Placements:**
- [ ] **Top Banner** (728x90) - Visible after header
- [ ] **Below Converter** (728x90) - Visible after hero/converter section
- [ ] **Sidebar** (300x250) - Visible on right side, sticky
- [ ] **In-Content** (300x250) - Visible between content sections
- [ ] **No Sticky Bottom** - Should NOT appear on desktop

**Verify:**
- [ ] Total ads visible: 4 maximum
- [ ] Ads don't break page layout
- [ ] Sidebar stays visible when scrolling
- [ ] Ads have "Advertisement" label
- [ ] Page loads smoothly

## 2. Mobile Testing (<768px)

### Open any page on mobile device or browser dev tools

**Expected Ad Placements:**
- [ ] **Top Banner** (300x100) - Visible after header
- [ ] **Below Converter** (300x100) - Visible after converter
- [ ] **In-Content** (300x250) - Visible between sections
- [ ] **Sticky Bottom** (300x50) - Fixed at bottom with close button
- [ ] **No Sidebar** - Should NOT appear on mobile

**Verify:**
- [ ] Total ads visible: 3 maximum
- [ ] Sticky ad has X close button
- [ ] Clicking X closes sticky ad
- [ ] Closed sticky ad stays closed (session storage)
- [ ] Content is not obscured by sticky ad
- [ ] Page is scrollable with sticky ad

## 3. Lazy Loading Test

### Scroll behavior test

**Steps:**
1. Open a page
2. Note which ads are visible immediately
3. Scroll down slowly
4. Watch for ads loading as they come into view

**Verify:**
- [ ] Ads load ~300px before becoming visible
- [ ] Loading state appears briefly
- [ ] No layout shift when ads load
- [ ] Console shows no errors

## 4. Ad Network Integration Test

### Check ad provider is working

**Open Browser Console (F12) and check:**

```javascript
// Check if AdProvider is loaded
console.log(window.AdProvider);

// Check if ad containers exist
console.log(document.querySelectorAll('.ad-container').length);

// Check if ads are marked as loaded
console.log(document.querySelectorAll('[data-loaded="true"]').length);
```

**Verify:**
- [ ] AdProvider object exists
- [ ] Ad containers are present
- [ ] Ads are marked as loaded
- [ ] No JavaScript errors in console

## 5. Device Detection Test

### Test responsive behavior

**Resize browser window:**
1. Start at desktop size (>1024px)
2. Resize to tablet (768-1023px)
3. Resize to mobile (<768px)

**Verify:**
- [ ] Ad sizes change appropriately
- [ ] Sidebar disappears on mobile
- [ ] Sticky bottom appears on mobile
- [ ] Layout remains intact at all sizes

## 6. Privacy Pages Test

### Check ad-free pages

**Open these pages:**
- `/privacy-policy/`
- `/terms-of-use/`

**Verify:**
- [ ] No ads visible on privacy policy
- [ ] No ads visible on terms of use
- [ ] Pages still load normally
- [ ] No console errors

## 7. Multi-Language Test

### Test different language versions

**Open pages in different languages:**
- `/` (English)
- `/es/` (Spanish)
- `/fr/` (French)
- `/ar/` (Arabic - RTL layout)
- `/ja/` (Japanese)

**Verify:**
- [ ] Ads appear on all language versions
- [ ] RTL languages (Arabic) display correctly
- [ ] Ad labels are in English (standard)
- [ ] No layout issues in any language

## 8. Auto-Refresh Test

### Verify ad network auto-refresh

**Steps:**
1. Open a page with ads
2. Wait 30 seconds
3. Watch for ad refresh (handled by ad network)

**Note:** Auto-refresh is handled by the ad network (a.magsrv.com), not our code.

**Verify:**
- [ ] Ads refresh automatically after ~30s
- [ ] No page reload required
- [ ] No console errors during refresh

## 9. Performance Test

### Check page load performance

**Use Browser DevTools > Network tab:**

**Verify:**
- [ ] Ad provider script loads asynchronously
- [ ] ads.css loads quickly (<100ms)
- [ ] ads.js loads quickly (<100ms)
- [ ] Page is interactive before ads load
- [ ] Total page load time is acceptable

## 10. Cross-Browser Test

### Test on multiple browsers

**Test on:**
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari (Mac/iOS)
- [ ] Mobile browsers (Chrome, Safari)

**Verify:**
- [ ] Ads display correctly in all browsers
- [ ] No browser-specific layout issues
- [ ] JavaScript works in all browsers

## 🐛 Common Issues & Solutions

### Issue: Ads not showing
**Check:**
- Ad provider script loaded? (Check Network tab)
- Console errors? (Check Console tab)
- Ad blocker enabled? (Disable and test)
- Zone IDs correct? (Check ads.js)

### Issue: Too many ads on mobile
**Check:**
- Device detection working? (Check console: `window.AdManager.isMobile`)
- Ad limit enforced? (Max 3 on mobile)

### Issue: Sticky ad won't close
**Check:**
- Close button visible?
- JavaScript errors in console?
- Event listener attached? (Check ads.js)

### Issue: Layout broken
**Check:**
- CSS loaded? (Check Network tab for ads.css)
- Content-with-sidebar wrapper present?
- Sidebar only on desktop?

### Issue: Ads not lazy loading
**Check:**
- IntersectionObserver supported? (Check browser compatibility)
- Fallback working? (Older browsers)
- Console errors?

## 📊 Success Criteria

✅ **All tests pass if:**
- Ads display on desktop (4 max) and mobile (3 max)
- No layout issues or content obscured
- Sticky ad is closeable on mobile
- Ads lazy-load smoothly
- No JavaScript errors
- Page performance is good
- Works across all browsers and languages

## 🚨 If Ads Don't Show

1. **Check ad network status** - Visit a.magsrv.com
2. **Verify zone IDs** - Check `web/assets/ads.js`
3. **Check account status** - Log into ad network dashboard
4. **Review approval status** - Ads may need approval
5. **Test with different content** - Some content may be filtered

## 📞 Support

If issues persist:
1. Check ad network documentation
2. Review `AD_IMPLEMENTATION_GUIDE.md`
3. Check browser console for errors
4. Verify all files deployed correctly

---

**Last Updated:** April 30, 2026
