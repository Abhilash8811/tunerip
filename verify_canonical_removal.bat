@echo off
REM Verification script to check if canonical tags are removed from Vercel deployment

echo.
echo Verifying Canonical Tag Removal on Vercel Deployment
echo =========================================================
echo.
echo Make sure Vercel deployment is complete before running this check.
echo Check: https://vercel.com/dashboard
echo.
pause
echo.

echo Checking Vercel deployment (should have NO canonical tags):
echo ----------------------------------------------------------------
curl -s "https://tunerip.vercel.app/" | findstr /i "canonical" >nul
if %errorlevel% equ 0 (
    echo Homepage: FAIL - canonical tag found
) else (
    echo Homepage: PASS - no canonical tag
)

curl -s "https://tunerip.vercel.app/youtube-mp3/" | findstr /i "canonical" >nul
if %errorlevel% equ 0 (
    echo youtube-mp3: FAIL - canonical tag found
) else (
    echo youtube-mp3: PASS - no canonical tag
)

curl -s "https://tunerip.vercel.app/youtube-to-mp4-converter/" | findstr /i "canonical" >nul
if %errorlevel% equ 0 (
    echo youtube-to-mp4-converter: FAIL - canonical tag found
) else (
    echo youtube-to-mp4-converter: PASS - no canonical tag
)

echo.
echo Checking Google Verification Tag on Vercel:
echo ----------------------------------------------------------------
curl -s "https://tunerip.vercel.app/" | findstr /i "google-site-verification" >nul
if %errorlevel% equ 0 (
    echo PASS - Google verification tag found
) else (
    echo FAIL - Google verification tag NOT found
)

echo.
echo Summary:
echo ----------------------------------------------------------------
echo If all checks show PASS, you're ready to:
echo 1. Go to Google Search Console
echo 2. Add property: https://tunerip.vercel.app
echo 3. Verify using HTML tag method
echo 4. Submit sitemap: https://tunerip.vercel.app/sitemap-vercel.xml
echo.
echo Done!
pause
