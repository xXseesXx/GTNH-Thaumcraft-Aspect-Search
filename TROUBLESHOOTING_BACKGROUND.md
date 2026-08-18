# 🔧 Troubleshooting: Aspect Background Not Showing

## Issues Fixed

### ✅ Issue 1: Opening HTML locally doesn't load data
**Problem:** CORS restrictions prevent loading JSON files locally  
**Solution:** Must use a local web server

### ✅ Issue 2: GitHub Pages not showing background
**Problem:** 
1. GitHub Pages takes 2-5 minutes to rebuild after branch change
2. Browser cache may show old version
3. Opacity was too low (15% → 25%)
4. Background was loading with 1 second delay

**Solutions Applied:**
1. Increased opacity to 25% (more visible)
2. Changed to load immediately (no delay)
3. Added extensive logging for debugging

---

## ✅ Testing Locally (Required!)

You **cannot** open the HTML file directly (file:// protocol). You **must** use a web server:

### Method 1: Python HTTP Server (Recommended)
```bash
cd C:\Users\fabib\Documents\Minecraft\1.7.10\ThaumicJade\webdb\static-site

# Make sure you're on experimental branch
git checkout experimental-aspect-background

# Start server
python -m http.server 8000

# Open in browser:
# http://localhost:8000/
# or
# http://localhost:8000/test-aspect-background.html
```

### Method 2: Node.js (if installed)
```bash
npx http-server -p 8000
```

### Method 3: VS Code Live Server
If you have VS Code with Live Server extension:
1. Open static-site folder in VS Code
2. Right-click index.html
3. Select "Open with Live Server"

---

## 🧪 Debug Test Page

I've created a dedicated test page to help debug:

**URL:** http://localhost:8000/test-aspect-background.html

This page shows:
- ✅ Status indicator (green = working, red = error)
- 📋 Real-time log of what's happening
- 🎨 The aspect background pattern

**What to check:**
1. Status should turn green
2. Log should show successful loading
3. Background should have colored aspect icons

---

## 🌐 GitHub Pages Debugging

### Step 1: Verify Branch is Set
1. Go to: https://github.com/xXseesXx/GTNH-Thaumcraft-Aspect-Search/settings/pages
2. Verify "Branch" is set to `experimental-aspect-background`
3. Verify "Folder" is set to `/ (root)`

### Step 2: Check Build Status
1. Go to: https://github.com/xXseesXx/GTNH-Thaumcraft-Aspect-Search/actions
2. Look for latest "pages build and deployment" workflow
3. Should have green checkmark
4. If red X, click to see error details

### Step 3: Force Refresh Browser
Clear cache completely:
- **Chrome/Edge:** Ctrl+Shift+Delete → Clear cache
- **Firefox:** Ctrl+Shift+Delete → Clear cache
- **Or:** Use incognito/private mode

### Step 4: Wait Longer
GitHub Pages can take 5-10 minutes sometimes. Be patient!

---

## 🔍 Console Debugging

Open browser console (F12 → Console tab) and look for:

### ✅ Success Messages:
```
[Aspect BG] Starting initialization...
[Aspect BG] Loaded 69 aspects
[Aspect BG] Canvas size: 1920x1080
[Aspect BG] Loaded 10/69...
[Aspect BG] Loaded 20/69...
...
[Aspect BG] Loaded 69/69 aspect images
[Aspect BG] Drawing pattern...
[Aspect BG] Drew 342 aspect icons
[Aspect BG] Initialization complete!
```

### ❌ Error Messages to Watch For:
```
Failed to fetch aspect registry: 404
→ aspect_registry.json not found (file path issue)

Failed to load aer.png
→ aspect_images/ folder not found or files missing

CORS policy error
→ Opening file directly (need web server)

Canvas element not found
→ HTML structure issue
```

---

## 📋 Checklist

### Local Testing:
- [ ] On `experimental-aspect-background` branch
- [ ] Using web server (not file://)
- [ ] Server running on port 8000
- [ ] Opened http://localhost:8000/
- [ ] Console shows no errors
- [ ] Background pattern visible

### GitHub Pages:
- [ ] Branch set to `experimental-aspect-background` in settings
- [ ] Waited at least 5 minutes after changing branch
- [ ] Checked Actions tab for successful build
- [ ] Cleared browser cache
- [ ] Visited site in incognito mode
- [ ] Checked console for errors (F12)

---

## 🎨 Visual Verification

### What You Should See:
- **Background:** Subtle colored dots (aspect icons)
- **Colors:** Various colors (yellow, green, orange, cyan, purple, etc.)
- **Pattern:** Random scattered placement
- **Rotation:** Icons at different angles
- **Opacity:** 25% opacity (subtle but visible)
- **White container:** Main content box on top

### What You Should NOT See:
- All black icons (color tinting failed)
- No icons at all (loading failed)
- Error messages in console
- Blank white background (pattern not rendering)

---

## 🚀 Current Status

**Latest Push:** Just now (cc7fc97 → c8dfebb)

**Changes:**
1. ✅ Opacity increased: 15% → 25% (more visible)
2. ✅ Load immediately (removed 1 second delay)
3. ✅ Added extensive logging
4. ✅ Added timeout handling (5 seconds per image)
5. ✅ Created test-aspect-background.html for debugging

**GitHub Pages:**
- Build should complete in ~2-5 minutes
- URL: https://xXseesXx.github.io/GTNH-Thaumcraft-Aspect-Search/
- Test page: https://xXseesXx.github.io/GTNH-Thaumcraft-Aspect-Search/test-aspect-background.html

---

## 🔧 Quick Fixes

### If background is too subtle:
Edit `index.html`, line ~17:
```css
opacity: 0.25;  /* Try 0.35 or 0.45 */
```

### If icons are too small:
Edit `index.html`, line ~1324:
```javascript
const size = 48;  /* Try 64 or 72 */
```

### If pattern is too dense:
Edit `index.html`, line ~1325:
```javascript
const spacing = 80;  /* Try 100 or 120 */
```

---

## 📞 Still Not Working?

1. **Test with test-aspect-background.html first**
   - If test page works → main page should work
   - If test page fails → check console errors

2. **Verify files exist:**
   ```bash
   ls static-site/aspect_images/  # Should show 69 PNG files
   ls static-site/aspect_registry.json  # Should exist
   ```

3. **Check browser compatibility:**
   - Chrome/Edge recommended
   - Firefox works
   - Safari may have issues with canvas blend modes

4. **Try different browser:**
   - If it works in one browser but not another → browser issue

---

**Current time:** ~15:35
**Expected GitHub Pages update:** ~15:40 (5 minutes after last push)

**Try the test page first:** http://localhost:8000/test-aspect-background.html
