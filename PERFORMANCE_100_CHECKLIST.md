# Performance 100/100 Checklist

## Current Status
- **Performance**: 86/100 → Target: 100/100
- **Issues**: 
  - Render blocking CSS (400ms savings)
  - Layout shift (CLS: 0.274 → Target: <0.1)

## Files Created
1. ✅ `web/assets/critical.css` - Minified critical CSS for inlining
2. ✅ `scripts/optimize_performance.py` - Automation script
3. ✅ `PERFORMANCE_OPTIMIZATION_GUIDE.md` - Detailed guide

## Quick Implementation (Manual - 1 File Test)

### Test on `web/index.html` first:

1. **Add Resource Hints** (after `<head>` tag):
```html
<head>
<!-- Performance: DNS Prefetch & Preconnect -->
<link rel="dns-prefetch" href="https://pl29304694.profitablecpmratenetwork.com">
<link rel="preconnect" href="https://pl29304694.profitablecpmratenetwork.com" crossorigin>
<link rel="preload" href="/assets/favicon.svg" as="image" type="image/svg+xml">
<link rel="preload" href="/assets/app.js?v=2" as="script">
```

2. **Replace CSS Loading** (find these lines):
```html
<!-- REMOVE THESE -->
<link rel="stylesheet" href="/assets/style.css?v=2">
<link rel="stylesheet" href="/assets/ads.css">
```

**Replace with**:
```html
<!-- Critical CSS inlined for performance -->
<style>
/* Copy entire content from web/assets/critical.css here */
:root{--bg:#ffffff;--bg-2:#f8f9fa;--card:#ffffff;--card-2:#f1f3f5;--text:#111111;--muted:#333333;--border:#e1e4e8;--border-2:#d1d5da;--accent:#2d5cf7;--accent-text:#ffffff;--radius:18px;--radius-sm:12px;--shadow:0 4px 12px rgba(0,0,0,0.05);--max:900px;--tap:44px}
[data-theme="dark"]{--bg:#0b0d14;--bg-2:#161a24;--card:#1c212e;--card-2:#262a36;--text:#f3f4f9;--muted:#a0a8c0;--border:#2d3446;--border-2:#353948;--accent:#4a7fff;--accent-text:#0b0d14;--shadow:0 8px 24px rgba(0,0,0,0.3)}
*,*::before,*::after{box-sizing:border-box}
html,body{margin:0;padding:0}
html{color-scheme:dark}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.55;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:100%;min-height:100vh}
a{color:var(--text);text-decoration:none}
button{font:inherit;color:inherit}
img,svg{max-width:100%;display:block}
.container{max-width:var(--max);margin:0 auto;padding:0 16px;width:100%}
.sr-only{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:-9999px}
.skip:focus{left:16px;top:16px;background:var(--accent);color:var(--accent-text);padding:8px 12px;border-radius:8px;z-index:9999}
.site-header{padding:24px 0}
.header-row{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.brand{font-weight:900;font-size:clamp(26px,4.6vw,36px);letter-spacing:-.02em;color:var(--text);line-height:1}
.brand-dot{color:var(--accent);font-weight:900}
.header-actions{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end}
.btn-supporter{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:var(--accent-text);border:0;border-radius:var(--radius-sm);padding:10px 16px;font-weight:700;font-size:14px;cursor:pointer;min-height:var(--tap)}
.btn-lang,.btn-theme{background:transparent;border:1px solid var(--border-2);border-radius:var(--radius-sm);color:var(--text);padding:9px 14px;font-size:14px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;min-height:var(--tap)}
.btn-theme{padding:0;width:var(--tap);height:var(--tap);justify-content:center}
.btn-theme .icon-sun{display:none}
html[data-theme="light"] .btn-theme .icon-moon{display:none}
html[data-theme="light"] .btn-theme .icon-sun{display:block}
.hero{padding:8px 0 40px;min-height:420px}
.converter-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:32px;box-shadow:var(--shadow);min-height:320px}
.converter-title{margin:0 0 24px;text-align:center;font-weight:800;letter-spacing:-.015em;font-size:clamp(22px,4vw,30px)}
.url-wrap{position:relative;margin-bottom:16px}
#yt-url{width:100%;background:var(--bg-2);color:var(--text);border:1px solid var(--border-2);border-radius:var(--radius-sm);padding:16px 56px 16px 22px;font-size:15px;outline:none;min-height:var(--tap);position:relative;z-index:1}
#yt-url::placeholder{color:#7a8094}
#paste-btn{position:absolute;right:8px;top:50%;transform:translateY(-50%);background:transparent;border:0;color:var(--muted);cursor:pointer;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;z-index:2}
.controls-row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.seg{display:inline-flex;background:var(--bg-2);border:1px solid var(--border-2);border-radius:var(--radius-sm);padding:4px;gap:2px}
.seg-btn{background:transparent;border:0;color:var(--muted);cursor:pointer;padding:8px 18px;border-radius:var(--radius-sm);font-weight:600;font-size:14px;min-height:36px}
.seg-btn.active{background:var(--text);color:var(--accent-text)}
.select-pill{background:var(--bg-2);border:1px solid var(--border-2);border-radius:var(--radius-sm);color:var(--text);padding:9px 36px 9px 16px;font-weight:500;font-size:14px;cursor:pointer;appearance:none;-webkit-appearance:none;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'><path d='M2 4l4 4 4-4' stroke='%23a3a8b8' stroke-width='1.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>");background-repeat:no-repeat;background-position:right 14px center;background-size:12px;min-height:var(--tap)}
.spacer{flex:1;min-width:0}
#convert-btn{margin-left:auto;background:var(--text);color:var(--accent-text);border:0;border-radius:var(--radius-sm);padding:12px 32px;font-weight:700;font-size:15px;cursor:pointer;min-height:var(--tap)}
html[data-theme="light"]{--bg:#f3f4f9;--bg-2:#ffffff;--card:#ffffff;--card-2:#f6f7fb;--text:#11131a;--muted:#4a5168;--border:#e3e6ef;--border-2:#d2d6e3;--accent-text:#1a1d28}
html[data-theme="light"] #convert-btn{background:#11131a;color:#fff}
html[data-theme="light"] .seg-btn.active{background:#11131a;color:#fff}
@media (max-width:560px){
.container{padding:0 12px}
.converter-card{padding:20px 16px;border-radius:14px}
.header-row{gap:8px}
.brand{font-size:24px}
.btn-supporter{padding:8px 12px;font-size:13px}
.btn-supporter span.s-label{display:none}
.btn-lang span.l-label{display:none}
.controls-row{gap:8px}
#convert-btn{margin-left:0;width:100%;order:99}
}
</style>

<!-- Load full CSS asynchronously (non-blocking) -->
<link rel="preload" href="/assets/style.css?v=2" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/assets/style.css?v=2"></noscript>

<!-- Load ads CSS with low priority -->
<link rel="stylesheet" href="/assets/ads.css" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="/assets/ads.css"></noscript>
```

3. **Test with Lighthouse**:
```bash
# Open Chrome DevTools
# Go to Lighthouse tab
# Run audit for Performance
# Should see 100/100 with CLS < 0.1
```

## Automated Implementation (All Files)

### Run the Python script:

```bash
# From project root
python3 scripts/optimize_performance.py
```

This will:
- ✅ Inline critical CSS in all HTML files
- ✅ Convert CSS loading to async
- ✅ Add resource hints
- ✅ Fix layout shifts with min-height
- ✅ Optimize ~93 HTML files automatically

## Verification Steps

After optimization, verify on multiple pages:

1. **Homepage** (`/`)
   - Performance: 100/100
   - CLS: <0.1
   - FCP: <1.8s
   - LCP: <2.5s

2. **Language Pages** (`/es/`, `/hi/`, etc.)
   - Same metrics as homepage

3. **Downloader Pages** (`/youtube-shorts-downloader`, etc.)
   - Same metrics across all variants

4. **Special Pages** (`/ytmp3`, `/youtube-mp3`, etc.)
   - Verify no regressions

## Expected Improvements

| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Performance | 86 | 100 | 100 |
| CLS | 0.274 | <0.05 | <0.1 |
| FCP | ~1.2s | <0.9s | <1.8s |
| LCP | ~2.0s | <1.5s | <2.5s |
| TBT | ~150ms | <100ms | <200ms |
| Blocking Time | 400ms | 0ms | 0ms |

## Rollback Plan

If issues occur:
1. Keep backup of original files
2. Script creates `.bak` files automatically
3. Revert with: `git checkout web/`

## Production Deployment

1. ✅ Test locally first
2. ✅ Verify on staging
3. ✅ Deploy to production
4. ✅ Monitor Core Web Vitals
5. ✅ Check Google Search Console

## Additional Optimizations (Optional)

For even better performance:

1. **Enable HTTP/2 Server Push**
2. **Add Service Worker for caching**
3. **Implement Brotli compression**
4. **Use CDN for static assets**
5. **Optimize images with WebP**

## Support

If you encounter issues:
- Check `PERFORMANCE_OPTIMIZATION_GUIDE.md` for details
- Review Lighthouse report for specific issues
- Test on incognito mode (no extensions)
- Clear cache and test again
