# Vercel Canonical Tag Fix - Google Search Console Setup

## Problem
When trying to add `https://tunerip.vercel.app/` to Google Search Console, canonical tags in all HTML pages pointed to `https://yt2mp3.lol/*`, causing Google to treat Vercel pages as duplicates rather than independent pages. This prevented proper indexing of the Vercel domain.

## Solution Implemented
Modified the build process to **conditionally remove canonical tags** when building for Vercel deployment. This allows:
- **yt2mp3.lol** (cPanel): Keeps canonical tags for SEO consistency
- **tunerip.vercel.app** (Vercel): No canonical tags, treated as independent site

## Changes Made

### 1. `web/build.js`
- Added `IS_VERCEL_BUILD` flag that detects Vercel environment
- Modified `renderLandingPage()` to conditionally include canonical tags
- Added post-processing step to remove canonical tags from static HTML files (index.html, youtube-mp3, ytmp3, etc.)

### 2. `vercel.json`
- Updated `buildCommand` to pass `--vercel` flag: `node web/build.js --vercel`

## How It Works

### Detection Methods
The build script detects Vercel deployment through:
1. `process.env.VERCEL === '1'` (automatically set by Vercel)
2. `--vercel` command-line flag (explicitly passed in vercel.json)

### Build Behavior
- **Regular build** (cPanel): `node web/build.js` → Includes canonical tags
- **Vercel build**: `node web/build.js --vercel` → Removes canonical tags

## Next Steps for Google Search Console

### 1. Deploy to Vercel
```bash
git add .
git commit -m "Fix: Remove canonical tags for Vercel deployment to enable independent indexing"
git push origin main
```

Wait for Vercel to deploy (automatic on push).

### 2. Verify Canonical Tags Removed
Visit any page on tunerip.vercel.app and check the HTML source:
- ✅ Should NOT see: `<link rel="canonical" href="https://yt2mp3.lol/...">`
- ✅ Should see: Google verification meta tag

### 3. Add to Google Search Console
1. Go to [Google Search Console](https://search.google.com/search-console)
2. Click "Add Property"
3. Enter: `https://tunerip.vercel.app`
4. Verification method: **HTML tag** (already added: `TBnLVB-TJRIeGQ-TVk5LxtJaBEacG12ucglN0YCedVI`)
5. Click "Verify"

### 4. Submit Sitemap
Once verified, submit the Vercel-specific sitemap:
```
https://tunerip.vercel.app/sitemap-vercel.xml
```

This sitemap contains all URLs with `tunerip.vercel.app` domain (already created in `public/sitemap-vercel.xml`).

## Benefits

### Independent Indexing
- **tunerip.vercel.app** will be indexed separately from yt2mp3.lol
- Leverages Vercel's high domain authority (DA/PA)
- No duplicate content issues

### Dual Domain Strategy
- **yt2mp3.lol**: Primary brand domain with canonical tags
- **tunerip.vercel.app**: Secondary domain for Vercel DA benefits
- Both sites have identical content but are treated as independent by Google

## Testing

### Verify Canonical Tags
```bash
# Check yt2mp3.lol (should have canonical)
curl -s https://yt2mp3.lol/ | grep canonical

# Check tunerip.vercel.app (should NOT have canonical after deployment)
curl -s https://tunerip.vercel.app/ | grep canonical
```

### Local Testing
```bash
# Test Vercel build locally
node web/build.js --vercel
grep -r "canonical" web/index.html
# Should return nothing or empty
```

## Rollback (if needed)
If you want to revert and keep canonical tags on Vercel:
1. Remove `--vercel` flag from `vercel.json` buildCommand
2. Remove `IS_VERCEL_BUILD` logic from `web/build.js`
3. Redeploy

## Notes
- The Google verification meta tag is already in `web/index.html`
- The Vercel sitemap (`public/sitemap-vercel.xml`) is already created
- Both files are copied to `dist/` during Vercel build
- No changes needed to cPanel deployment (it continues to use canonical tags)
