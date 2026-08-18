# 🚀 GitHub Pages Deployment Guide

Complete guide to deploying Thaumcraft Aspects Search to GitHub Pages.

## 📋 Prerequisites

- GitHub account
- Git installed locally
- Your static site files ready

## 🎯 Quick Deploy (5 minutes)

### Step 1: Create Repository

1. Go to https://github.com/new
2. Repository name: `thaumcraft-aspects` (or your choice)
3. Description: "Thaumcraft Aspects Search - Client-side web app"
4. Set to **Public** (required for free GitHub Pages)
5. **Do not** initialize with README, .gitignore, or license
6. Click "Create repository"

### Step 2: Push Your Code

```bash
cd static-site

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Thaumcraft Aspects Search static site"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/thaumcraft-aspects.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. In left sidebar, click **Pages**
4. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
5. Click **Save**

### Step 4: Wait & Access

- Wait 1-2 minutes for deployment
- Your site will be live at:
  ```
  https://YOUR_USERNAME.github.io/thaumcraft-aspects/
  ```

✅ **Done!** Your site is now live.

---

## 🔧 Advanced Options

### Option A: Custom Domain

1. Buy a domain (e.g., from Namecheap, Google Domains)
2. In GitHub Pages settings, add your custom domain
3. In your domain registrar, add DNS records:
   ```
   Type: A
   Host: @
   Value: 185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
   ```
   ```
   Type: CNAME
   Host: www
   Value: YOUR_USERNAME.github.io
   ```
4. Wait for DNS propagation (5-60 minutes)
5. Enable "Enforce HTTPS" in GitHub Pages settings

### Option B: GitHub Actions (Automatic Deployment)

The included `.github/workflows/deploy.yml` will automatically deploy on every push to `main`.

**To enable:**
1. Push the `.github` folder with your code
2. Go to repository Settings → Pages
3. Change source to **GitHub Actions**
4. Next push will trigger automatic deployment

**Benefits:**
- Automatic deployment on push
- Build logs and error messages
- No manual deployment needed

### Option C: Use Main Repository

If you want to deploy from your main project folder (not static-site subfolder):

1. Move contents of `static-site/` to root of repository
2. Commit and push
3. Enable Pages as above

---

## 🧪 Testing Before Deployment

### Local Testing

Always test locally before deploying:

```bash
# In static-site directory
python -m http.server 8000

# Open http://localhost:8000/
```

**Test checklist:**
- ✅ Data loads without errors
- ✅ Search works with text input
- ✅ @modid syntax works
- ✅ Aspect filtering works
- ✅ Sorting works on all columns
- ✅ Pagination controls work
- ✅ No console errors (F12 → Console)

### Performance Testing

Open `performance-test.html` before deploying:

```bash
# Open http://localhost:8000/performance-test.html
```

Run all tests and verify:
- Load time < 2 seconds
- Search time < 100ms
- Memory < 50MB
- No errors

---

## 🐛 Troubleshooting

### Problem: 404 Error on GitHub Pages

**Solution:**
- Wait 5 minutes, GitHub Pages can be slow initially
- Check repository is Public (Settings → General)
- Verify `index.html` exists in root
- Check Settings → Pages shows green "Your site is live at..."

### Problem: JSON Not Loading (CORS Error)

**Solution:**
- Make sure `thaumcraft_aspects.json` is in same directory as `index.html`
- Check file is committed: `git ls-files` should show the JSON file
- Verify file size < 100MB (GitHub limit)

### Problem: Slow Loading

**Solution:**
- Enable "Enforce HTTPS" in Pages settings
- Consider enabling Cloudflare (free CDN)
- Compress JSON with gzip (server-side)
- Use jsDelivr CDN:
  ```javascript
  fetch('https://cdn.jsdelivr.net/gh/YOUR_USERNAME/thaumcraft-aspects@main/thaumcraft_aspects.json')
  ```

### Problem: Large JSON File (>100MB)

**Solution:**
- GitHub has 100MB file limit
- Use Git LFS (Large File Storage):
  ```bash
  git lfs install
  git lfs track "*.json"
  git add .gitattributes
  git add thaumcraft_aspects.json
  git commit -m "Add large JSON file"
  git push
  ```

### Problem: Site Not Updating

**Solution:**
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
- Check GitHub Actions tab for deployment status
- Force redeploy: Settings → Pages → "Re-run deployment"

---

## 📊 Monitoring & Analytics

### Add Google Analytics

Add before `</head>` in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Monitor Usage

GitHub provides basic stats:
- Go to repository Insights → Traffic
- See visitors, views, clones
- Track referrers

---

## 🔒 Security Best Practices

### HTTPS

Always enable "Enforce HTTPS" in Pages settings.

### Content Security Policy

Add to `<head>` for extra security:

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'unsafe-inline'; script-src 'unsafe-inline';">
```

### No Secrets

Never commit:
- API keys
- Passwords
- Personal data
- Private information

---

## 📱 Mobile Optimization

The site is responsive, but test on mobile:

1. Use Chrome DevTools (F12 → Toggle Device Toolbar)
2. Test on iPhone, iPad, Android
3. Verify touch interactions work
4. Check aspect picker opens correctly

---

## 🎨 Customization Post-Deploy

### Update Data

1. Replace `thaumcraft_aspects.json` locally
2. Commit and push:
   ```bash
   git add thaumcraft_aspects.json
   git commit -m "Update data"
   git push
   ```
3. Wait 1-2 minutes for redeployment

### Change Colors

Edit CSS in `index.html`:
- Primary yellow: `#FFEB3B`
- Primary cyan: `#00E5FF`
- Accent pink: `#FF4081`

### Add Footer

Before `</div>` closing container:

```html
<footer style="padding: 30px; text-align: center; border-top: 6px solid #000;">
  <p>Built with ❤️ for the Thaumcraft community</p>
  <p><a href="https://github.com/YOUR_USERNAME/thaumcraft-aspects">View on GitHub</a></p>
</footer>
```

---

## 📈 Performance Optimization

### Enable Compression

GitHub Pages automatically serves with gzip/brotli compression.

Verify compression:
```bash
curl -H "Accept-Encoding: gzip" -I https://YOUR_USERNAME.github.io/thaumcraft-aspects/thaumcraft_aspects.json
```

Should see: `Content-Encoding: gzip`

### CDN (Optional)

Use jsDelivr for faster worldwide access:

```javascript
// Change in index.html
fetch('https://cdn.jsdelivr.net/gh/YOUR_USERNAME/thaumcraft-aspects@latest/thaumcraft_aspects.json')
```

**Benefits:**
- Global CDN
- Faster for international users
- Automatic compression

---

## ✅ Deployment Checklist

Before going live:

- [ ] Test locally (`python -m http.server 8000`)
- [ ] Run performance tests (all passing)
- [ ] No console errors (F12 → Console)
- [ ] All features working (search, filter, sort, pagination)
- [ ] Mobile responsive (test on phone or DevTools)
- [ ] README updated with correct URLs
- [ ] Repository is Public
- [ ] `index.html` in root directory
- [ ] `thaumcraft_aspects.json` committed
- [ ] Git remote added
- [ ] Code pushed to GitHub
- [ ] Pages enabled in Settings
- [ ] Site accessible at github.io URL
- [ ] HTTPS enforced

---

## 🎉 Success!

Your site is now live and accessible worldwide for free!

Share your URL:
```
https://YOUR_USERNAME.github.io/thaumcraft-aspects/
```

**Next steps:**
- Share on Reddit, Discord, forums
- Add to modpack documentation
- Create a custom domain (optional)
- Monitor usage with analytics

---

## 📞 Need Help?

- **GitHub Pages Docs**: https://docs.github.com/pages
- **GitHub Community**: https://github.com/orgs/community/discussions
- **Stack Overflow**: Tag questions with `github-pages`

---

Built with ⚡ for the Thaumcraft community
