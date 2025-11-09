# Converting FlapPyBird to HTML5

There are two main approaches to run this game in a web browser:

## Option 1: Using Pygbag (Easiest - Already Set Up!)

**Pygbag** compiles your Python/Pygame code to WebAssembly, allowing it to run in the browser with minimal changes.

### Quick Start:

1. **Run in browser (development mode):**
   ```bash
   make web
   ```
   This will start a local server and open the game in your browser.

2. **Build for production:**
   ```bash
   make web-build
   ```
   This creates static files in `build/web/` that you can deploy to any web server.

### Deploying the Build:

After running `make web-build`, you'll have:
- `build/web/index.html` - The main HTML file
- `build/web/` - All necessary assets and WebAssembly files

You can deploy this to:
- **GitHub Pages** (already configured in `.github/workflows/deploy.yaml`)
- **Netlify** - Drag and drop the `build/web` folder
- **Vercel** - Point to the `build/web` directory
- **Any static hosting** - Upload the `build/web` folder

### Pros:
- ✅ No code changes needed
- ✅ Works with existing Python code
- ✅ Already configured

### Cons:
- ⚠️ Larger file size (WebAssembly)
- ⚠️ Slightly slower startup time
- ⚠️ Requires WebAssembly support in browser

---

## Option 2: Native HTML5/JavaScript Version (Better Performance)

For a true HTML5 game, you'd need to rewrite the game in JavaScript. Here's what that would involve:

### Architecture:

1. **HTML5 Canvas** instead of Pygame
2. **JavaScript** instead of Python
3. **Web Audio API** for sounds
4. **RequestAnimationFrame** for game loop

### Key Components to Port:

- `src/flappy.py` → `game.js` (main game loop)
- `src/entities/player.py` → `player.js` (bird physics)
- `src/entities/pipe.py` → `pipe.js` (obstacles)
- `src/entities/floor.py` → `floor.js` (ground)
- `src/entities/background.py` → `background.js`
- `src/utils/` → `utils.js` (helpers, collision detection)

### Technologies to Use:

- **Canvas API** - For rendering
- **Web Audio API** - For sound effects
- **ES6 Classes** - For entity structure
- **RequestAnimationFrame** - For game loop
- **Webpack/Vite** - For bundling (optional)

### Example Structure:

```
flappy-html5/
├── index.html
├── js/
│   ├── game.js
│   ├── player.js
│   ├── pipe.js
│   ├── floor.js
│   ├── background.js
│   └── utils.js
├── assets/
│   ├── sprites/ (same as current)
│   └── audio/ (convert to .mp3/.ogg)
└── css/
    └── style.css
```

### Pros:
- ✅ Better performance
- ✅ Smaller file size
- ✅ Native browser support
- ✅ Better mobile performance

### Cons:
- ⚠️ Requires rewriting all code
- ⚠️ More development time
- ⚠️ Need to handle asset loading differently

---

## Recommendation

**Start with Option 1 (Pygbag)** - It's already set up and works immediately. If you need better performance or want to learn HTML5 game development, then consider Option 2.

---

## Testing Pygbag

To test if pygbag works:

```bash
cd /Users/saifkhan/Desktop/games/FlapPyBird
make web
```

This should:
1. Compile the Python code to WebAssembly
2. Start a local web server
3. Open your browser to `http://localhost:8000`

If you encounter issues, check:
- Pygbag is installed: `python3 -m pip show pygbag`
- All assets are accessible
- Browser console for errors

