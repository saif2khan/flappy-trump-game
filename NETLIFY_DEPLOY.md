# Deploying FlapPyBird to Netlify

## Quick Deploy (Easiest Method)

### Step 1: Build the Game
```bash
cd /Users/saifkhan/Desktop/games/FlapPyBird
make web-build
```

### Step 2: Deploy via Netlify Dashboard

1. **Go to Netlify Drop**: https://app.netlify.com/drop
   - No account needed for first deploy, but you'll want to sign up to manage it later

2. **Drag and Drop**:
   - Open Finder
   - Navigate to: `/Users/saifkhan/Desktop/games/FlapPyBird/build/web`
   - Drag the entire `web` folder onto the Netlify drop zone

3. **Wait for Deployment**:
   - Netlify will upload and deploy your files
   - You'll get a URL like: `https://random-name-12345.netlify.app`

4. **Customize Your Site** (Optional):
   - Click on your site in Netlify dashboard
   - Go to "Site settings" → "Change site name"
   - Choose a custom name like `flappy-trump-game`
   - Your new URL will be: `https://flappy-trump-game.netlify.app`

---

## Advanced: Deploy via Netlify CLI

### Step 1: Install Netlify CLI
```bash
npm install -g netlify-cli
```

### Step 2: Login to Netlify
```bash
netlify login
```

### Step 3: Deploy
```bash
cd /Users/saifkhan/Desktop/games/FlapPyBird/build/web
netlify deploy --prod
```

This will:
- Create a new site (first time)
- Upload your files
- Give you a deployment URL

---

## Continuous Deployment (Recommended)

### Option 1: Connect to GitHub

1. **Push your code to GitHub** (if not already):
   ```bash
   git add .
   git commit -m "Add custom sprites and game over meme"
   git push origin master
   ```

2. **In Netlify Dashboard**:
   - Click "Add new site" → "Import an existing project"
   - Connect to GitHub
   - Select your repository
   - Set build settings:
     - **Build command**: `make web-build`
     - **Publish directory**: `build/web`
     - **Base directory**: (leave empty or set to project root)

3. **Deploy**:
   - Netlify will automatically build and deploy on every push to master

### Option 2: Manual Deploy Script

Create a script to build and deploy:

```bash
#!/bin/bash
cd /Users/saifkhan/Desktop/games/FlapPyBird
make web-build
cd build/web
netlify deploy --prod
```

---

## Important Notes

1. **Build Directory**: Always deploy from `build/web/`, not the project root
2. **File Size**: The WebAssembly build can be large (~5-10MB), but Netlify handles it fine
3. **Custom Domain**: You can add your own domain in Netlify settings
4. **HTTPS**: Netlify provides free SSL certificates automatically

---

## Troubleshooting

### If the game doesn't load:
- Check browser console for errors
- Ensure all files in `build/web/` are uploaded
- Verify the `index.html` file is in the root of the deployed folder

### If assets don't load:
- Check that asset paths are relative (they should be)
- Clear browser cache and try again

### Build Issues:
- Make sure you run `make web-build` before deploying
- Check that all sprite files exist in `assets/sprites/`

---

## Quick Reference

**Build Command:**
```bash
make web-build
```

**Deploy Directory:**
```
/Users/saifkhan/Desktop/games/FlapPyBird/build/web
```

**Netlify Drop URL:**
https://app.netlify.com/drop

