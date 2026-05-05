#!/bin/bash
# Verification script to check if canonical tags are removed from Vercel deployment

echo "🔍 Verifying Canonical Tag Removal on Vercel Deployment"
echo "========================================================="
echo ""

# Wait a moment for user to confirm deployment is complete
echo "⏳ Make sure Vercel deployment is complete before running this check."
echo "   Check: https://vercel.com/dashboard"
echo ""
read -p "Press Enter when deployment is ready..."
echo ""

# Test pages
PAGES=(
  "/"
  "/youtube-mp3/"
  "/ytmp3/"
  "/youtube-audio-download-mp3/"
  "/youtube-to-mp4-converter/"
  "/youtube-shorts-downloader/"
  "/youtube-playlist-downloader/"
)

VERCEL_DOMAIN="https://tunerip.vercel.app"
CPANEL_DOMAIN="https://yt2mp3.lol"

echo "📋 Checking Vercel deployment (should have NO canonical tags):"
echo "----------------------------------------------------------------"
for page in "${PAGES[@]}"; do
  echo -n "Checking $page ... "
  RESULT=$(curl -s "${VERCEL_DOMAIN}${page}" | grep -i 'rel="canonical"')
  if [ -z "$RESULT" ]; then
    echo "✅ PASS (no canonical tag)"
  else
    echo "❌ FAIL (canonical tag found)"
    echo "   Found: $RESULT"
  fi
done

echo ""
echo "📋 Checking cPanel deployment (should HAVE canonical tags):"
echo "----------------------------------------------------------------"
for page in "${PAGES[@]}"; do
  echo -n "Checking $page ... "
  RESULT=$(curl -s "${CPANEL_DOMAIN}${page}" | grep -i 'rel="canonical"')
  if [ -n "$RESULT" ]; then
    echo "✅ PASS (canonical tag present)"
  else
    echo "❌ FAIL (canonical tag missing)"
  fi
done

echo ""
echo "🔍 Checking Google Verification Tag on Vercel:"
echo "----------------------------------------------------------------"
VERIFICATION=$(curl -s "${VERCEL_DOMAIN}/" | grep -i 'google-site-verification')
if [ -n "$VERIFICATION" ]; then
  echo "✅ PASS - Google verification tag found"
  echo "   $VERIFICATION"
else
  echo "❌ FAIL - Google verification tag NOT found"
fi

echo ""
echo "📊 Summary:"
echo "----------------------------------------------------------------"
echo "If all Vercel pages show ✅ PASS (no canonical tag), you're ready to:"
echo "1. Go to Google Search Console"
echo "2. Add property: https://tunerip.vercel.app"
echo "3. Verify using HTML tag method"
echo "4. Submit sitemap: https://tunerip.vercel.app/sitemap-vercel.xml"
echo ""
echo "Done! 🎉"
