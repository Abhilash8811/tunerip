# Downloader Pages Translation Plan

## Objective
Create translated versions of 3 downloader pages for 17 languages (excluding English which already exists).

## Pages to Create
1. **youtube-multi-downloader** - Batch download multiple videos
2. **youtube-shorts-downloader** - Download YouTube Shorts
3. **youtube-playlist-downloader** - Download entire playlists

## Languages (17 total)
- ar (Arabic) - RTL
- bn (Bengali)
- de (German)
- es (Spanish)
- fil (Filipino)
- fr (French)
- hi (Hindi)
- id (Indonesian)
- it (Italian)
- ja (Japanese)
- ko (Korean)
- pt (Portuguese)
- ru (Russian)
- th (Thai)
- tr (Turkish)
- ur (Urdu) - RTL
- vi (Vietnamese)

## Total Files to Create
17 languages × 3 pages = **51 files**

## Ad Implementation (Must Match Homepage)
Each page MUST include these ad placements:

1. **Top Banner** - `ad-top-banner` with `data-ad-type="banner-top"`
2. **Below Converter** - `ad-below-converter` with `data-ad-type="banner-bottom"`
3. **In-Content Native** - `ad-native` with `data-ad-type="in-content"`
4. **Adsterra Native Banner** - Inline script with container
5. **Sidebar** - `ad-sidebar` with `data-ad-type="sidebar"` (desktop only)
6. **Mobile Sticky Bottom** - `ad-sticky-bottom` with `data-ad-type="sticky"`

## Required Scripts
- `/assets/app.js?v=2`
- `/assets/ads-adsterra.js`

## Required Stylesheets
- `/assets/style.css?v=2`
- `/assets/ads.css`

## Status
- ✅ English versions exist
- ⏳ Creating translated versions...

## Approach
Create files systematically, language by language, ensuring:
1. Perfect ad placement matching homepage
2. Proper language codes and hreflang tags
3. Correct RTL support for Arabic and Urdu
4. Working language switcher with all routes
5. Proper meta tags and SEO
