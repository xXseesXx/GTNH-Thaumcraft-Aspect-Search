# Thaumcraft Aspects Search - Static Site

A fully client-side web application for searching and filtering Thaumcraft aspects. Built with vanilla JavaScript and designed for GitHub Pages hosting.

## 🎯 Features

- **11,512 items** indexed from Thaumcraft and compatible mods
- **70 unique aspects** with full filtering support
- **No backend required** - runs entirely in the browser
- **Fast search** - <50ms average search time
- **Low memory** - ~15-20MB total usage
- **@modid syntax** - Search by mod ID with `@minecraft`, `@thaumcraft`, etc.
- **Aspect filtering** - Select multiple aspects to find items containing ALL of them
- **Sortable columns** - Click headers to sort by mod, name, aspect count, or total amount
- **Pagination** - 20-1000 items per page

## 📦 Files

```
static-site/
├── index.html                  # Main application (standalone, ~1200 lines)
├── thaumcraft_aspects.json     # Data file (~2.9MB, 11,512 items)
├── performance-test.html       # Performance benchmark tool
└── README.md                   # This file
```

## 🚀 Quick Start

### Local Testing

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (with npx)
npx http-server -p 8000

# PHP
php -S localhost:8000
```

Then open: **http://localhost:8000/**

### GitHub Pages Deployment

1. **Create a new GitHub repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/thaumcraft-aspects.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main`
   - Folder: `/ (root)`
   - Save

3. **Access your site**
   - URL: `https://YOUR_USERNAME.github.io/thaumcraft-aspects/`
   - Usually live within 1-2 minutes

## 🧪 Performance Testing

Open `performance-test.html` in your browser to run comprehensive benchmarks:

- **Data Loading**: Measures fetch, parse, and indexing time
- **Search Speed**: Tests various filter combinations
- **Memory Usage**: Tracks heap memory consumption
- **Render Speed**: Measures DOM rendering performance

Expected results:
- Load time: < 2 seconds
- Search time: < 50ms average
- Memory usage: < 50MB
- Render 100 items: < 50ms

## 🎨 Design

**Neo-Brutalist Theme**
- Bold colors: Yellow (#FFEB3B), Cyan (#00E5FF), Pink (#FF4081)
- Thick black borders (4-6px)
- Hard shadows (6-12px offset)
- Uppercase typography
- High contrast for accessibility

## 🔍 Usage Examples

### Basic Search
```
diamond          → All items with "diamond" in name
stone            → All items with "stone" in name
dmnd             → Fuzzy: matches "diamond"
stone|iron|gold  → OR search: items with stone OR iron OR gold
^stone           → Regex: items starting with "stone"
```

### Mod Filtering
```
@minecraft       → All Minecraft items
@thaumcraft      → All Thaumcraft items
stone @minecraft → Stone items from Minecraft
```

### Advanced Search
**Fuzzy Matching**: Type abbreviated characters in order
- `dmnd` → diamond
- `stn` → stone
- `irningot` → iron ingot

**OR Search**: Use `|` to match multiple terms
- `stone|iron|gold` → items with any of these
- `sword|axe|pickaxe @minecraft` → tools from Minecraft

**Regex**: Use regex patterns for complex searches
- `^stone` → starts with "stone"
- `.*ore.*` → contains "ore"
- `(iron|gold).*ingot` → iron or gold ingots

### Aspect Filtering
1. Click "Click to select aspects..." input
2. Type to filter (e.g., "terra")
3. Click aspects to select them
4. Selected aspects are pinned to top
5. Click outside to close dropdown

### Sorting
- Click any column header to sort
- Click again to reverse direction
- Default: Fewest aspects → Highest total → Name A-Z

## 📊 Technical Details

### Data Structure
```javascript
{
  "exportDate": "2026-08-17 20:56:50",
  "totalItems": 11512,
  "items": [
    {
      "modId": "minecraft",
      "displayName": "Stone",
      "aspects": {
        "terra": 2
      }
    }
  ]
}
```

### Client-Side Architecture
```javascript
// Data loaded once on page load
dataStore = {
  items: [],           // All 11,512 items
  aspectsSet: new Set() // 70 unique aspects
}

// Filtering happens in-memory
search() → filter() → render()
```

### Browser Support
- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera
- ⚠️ IE11 (may need polyfills)

### Performance Characteristics
| Operation | Time | Memory |
|-----------|------|--------|
| Initial load | ~1-2s | ~15-20MB |
| Search (simple) | <20ms | No additional |
| Search (complex) | <50ms | No additional |
| Render 100 items | <30ms | No additional |

## 🛠️ Customization

### Change Default Page Size
```javascript
// Line ~805
let itemsPerPage = 100; // Change to 20, 50, 250, or 1000
```

### Modify Colors
```css
/* Primary yellow */
background: #FFEB3B;

/* Primary cyan */
background: #00E5FF;

/* Accent pink */
background: #FF4081;
```

### Update Data
Replace `thaumcraft_aspects.json` with your own data matching the same structure.

## 📝 Development Notes

### Why No Framework?
- **Zero dependencies** for maximum compatibility
- **Fast load time** - no framework overhead
- **Simple deployment** - just HTML/CSS/JS
- **Easy to audit** - all code in one file

### Why Inline Everything?
- **Single file deployment** - easier to host
- **No build step** - works immediately
- **Portable** - can be saved and run offline
- **CDN-free** - no external dependencies

### Future Optimizations
If needed (current performance is excellent):
- Gzip compression on server
- Web Worker for filtering large datasets
- Virtual scrolling for 1000+ results
- IndexedDB caching
- Service Worker for offline support

## 📄 License

MIT License - free to use and modify.

## 🙏 Credits

Built for the Thaumcraft Minecraft modding community.

Data extracted from Thaumcraft 4 and compatible mods for Minecraft 1.7.10.

---

**Need help?** Check `performance-test.html` to diagnose any issues.

**Want the Flask version?** See the parent directory for the full-stack Python implementation.
