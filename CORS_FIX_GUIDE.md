# CORS Issue Fix Guide

## What Was Fixed

### 1. Enhanced CORS Middleware in FastAPI
- Added `allow_credentials=False`
- Added `expose_headers=["*"]`
- Added `max_age=3600` for preflight caching

### 2. Added OPTIONS Handler
- Explicit OPTIONS endpoint to handle CORS preflight requests
- Returns proper CORS headers for all routes

### 3. Updated .htaccess
- Added Apache-level CORS headers
- Ensures CORS headers are sent even before reaching Python

## Deployment Steps

### Step 1: Pull Latest Changes on Server
```bash
cd ~/tunerip
git pull origin main
```

### Step 2: Restart API Server
```bash
cd ~/tunerip/api
./stop_api.sh
./deploy_cpanel.sh
```

Or manually:
```bash
# Stop old process
pkill -f "uvicorn main:app"

# Start new process
cd ~/tunerip/api
source venv/bin/activate
nohup uvicorn main:app --host 0.0.0.0 --port 8001 --workers 4 > api.log 2>&1 &
```

### Step 3: Verify API is Running
```bash
# Check process
ps aux | grep uvicorn

# Test health endpoint
curl http://localhost:8001/healthz

# Test CORS headers
curl -I -X OPTIONS http://localhost:8001/api/convert
```

## Troubleshooting

### Issue 1: Still Getting 403 Forbidden

**Possible Causes:**
1. API subdomain (`api.yt2mp3.lol`) is not configured in DNS
2. SSL certificate not configured for API subdomain
3. Firewall blocking port 8001
4. Apache proxy not configured correctly

**Solutions:**

#### Option A: Configure API Subdomain (Recommended)
1. Go to cPanel → Subdomains
2. Create subdomain: `api` → `api.yt2mp3.lol`
3. Point document root to: `~/tunerip/api`
4. Install SSL certificate for `api.yt2mp3.lol`
5. Ensure `.htaccess` is in place (already done)

#### Option B: Use Same Domain with Path
Update `web/assets/app.js`:
```javascript
var API_BASE = "https://yt2mp3.lol/api";
```

Then create `.htaccess` in web root:
```apache
# Proxy /api/* to Python backend
RewriteEngine On
RewriteRule ^api/(.*)$ http://127.0.0.1:8001/api/$1 [P,L]
```

#### Option C: Use Direct IP (Testing Only)
Update `web/assets/app.js`:
```javascript
var API_BASE = "http://YOUR_SERVER_IP:8001";
```

**Note:** This won't work with HTTPS frontend due to mixed content.

### Issue 2: API Not Responding

**Check if API is running:**
```bash
ps aux | grep uvicorn
netstat -tulpn | grep 8001
```

**Check logs:**
```bash
cd ~/tunerip/api
tail -f api.log
```

**Restart API:**
```bash
cd ~/tunerip/api
./restart_api_complete.sh
```

### Issue 3: CORS Headers Not Being Sent

**Verify Apache modules are enabled:**
```bash
# Check if mod_headers is enabled
apachectl -M | grep headers

# Check if mod_proxy is enabled
apachectl -M | grep proxy
```

If not enabled, contact your hosting provider to enable:
- `mod_headers`
- `mod_proxy`
- `mod_proxy_http`

### Issue 4: Mixed Content (HTTP/HTTPS)

If your frontend is HTTPS but API is HTTP, browsers will block the request.

**Solution:** Ensure API also uses HTTPS:
1. Configure SSL for `api.yt2mp3.lol`
2. Or use same domain with proxy (Option B above)

## Testing CORS

### Test from Browser Console
```javascript
fetch('https://api.yt2mp3.lol/healthz')
  .then(r => r.json())
  .then(console.log)
  .catch(console.error);
```

### Test with curl
```bash
# Test OPTIONS (preflight)
curl -X OPTIONS https://api.yt2mp3.lol/api/convert \
  -H "Origin: https://yt2mp3.lol" \
  -H "Access-Control-Request-Method: POST" \
  -v

# Should see:
# Access-Control-Allow-Origin: *
# Access-Control-Allow-Methods: GET, POST, OPTIONS
```

## Quick Fix: Temporary Solution

If you need a quick fix while configuring the subdomain, you can temporarily use a CORS proxy:

### Update app.js temporarily:
```javascript
var API_BASE = "https://corsproxy.io/?https://api.yt2mp3.lol";
```

**Warning:** This is NOT recommended for production! Only for testing.

## Recommended Production Setup

1. ✅ Configure `api.yt2mp3.lol` subdomain in cPanel
2. ✅ Install SSL certificate for API subdomain
3. ✅ Ensure `.htaccess` proxies to port 8001
4. ✅ Keep API running with process manager (screen/systemd)
5. ✅ Monitor API logs regularly

## Current Status

- ✅ CORS middleware configured in FastAPI
- ✅ OPTIONS handler added
- ✅ .htaccess updated with CORS headers
- ⏳ Need to deploy to server
- ⏳ Need to verify API subdomain is configured

## Next Steps

1. Deploy changes to server (pull + restart API)
2. Verify `api.yt2mp3.lol` is accessible
3. Test from browser
4. Monitor for any remaining issues

## Support

If issues persist after following this guide:
1. Check API logs: `tail -f ~/tunerip/api/api.log`
2. Check Apache error logs: `tail -f ~/logs/error_log`
3. Verify DNS: `nslookup api.yt2mp3.lol`
4. Test connectivity: `curl -I https://api.yt2mp3.lol/healthz`
