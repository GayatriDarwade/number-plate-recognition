# ✅ Deployment Checklist

## Files Modified/Created

### Core Fixes
- [x] `Procfile` - Fixed port binding with `--bind 0.0.0.0:$PORT`
- [x] `app.py` - Added lazy loading, health endpoint, better error handling
- [x] `config.py` - Already existed
- [x] `requirements.txt` - Already optimal

### New Files Created
- [x] `.slugignore` - Exclude unnecessary files from deployment
- [x] `render.yaml` - Render deployment configuration
- [x] `app_tesseract.py` - Alternative Pytesseract version (free tier compatible)
- [x] `requirements_tesseract.txt` - Dependencies for Pytesseract version
- [x] `DEPLOYMENT_GUIDE.md` - Detailed deployment instructions
- [x] `QUICK_FIX.md` - Quick decision guide
- [x] `switch_to_pytesseract.bat` - Script to switch to free version
- [x] `switch_to_easyocr.bat` - Script to switch back

### Updated Documentation
- [x] `README.md` - Added deployment section and warnings

---

## Pre-Deployment Checklist

### For EasyOCR Version (Paid Plan Required)
- [ ] Render plan upgraded to Standard ($25/mo) or higher
- [ ] Current code committed to git
- [ ] Pushed to GitHub
- [ ] Connected repository to Render
- [ ] Deployment initiated

### For Pytesseract Version (Free Tier Compatible)
- [ ] Run `switch_to_pytesseract.bat` OR manually copy files
- [ ] Committed changes to git
- [ ] Pushed to GitHub
- [ ] Added environment variable in Render: `APT_PACKAGES=tesseract-ocr`
- [ ] Deployment initiated

---

## Post-Deployment Checklist

- [ ] Deployment completed without errors
- [ ] Service is running (check Render dashboard)
- [ ] Health endpoint responding: `https://your-app.onrender.com/health`
- [ ] Homepage loads: `https://your-app.onrender.com/`
- [ ] Image upload works
- [ ] Number plate detection working
- [ ] OCR text recognition working

---

## Common Issues & Solutions

### Issue: Still getting "Out of memory"
**If using EasyOCR:**
- ❌ Render plan not upgraded
- ✅ Upgrade to Standard plan ($25/mo, 2GB RAM)

**If using Pytesseract:**
- ❌ Still using old requirements.txt
- ✅ Make sure you switched files correctly

### Issue: "No open ports detected"
**Status:** ✅ FIXED in updated Procfile
- Old: `web: gunicorn app:app`
- New: `web: gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --preload`

### Issue: First request times out (EasyOCR)
**Status:** ⚠️ EXPECTED BEHAVIOR
- EasyOCR downloads models on first request (~200MB)
- Takes 1-2 minutes
- Subsequent requests are fast
- **Solution:** Increase timeout or be patient

### Issue: Tesseract not found (Pytesseract version)
**Status:** ❌ Missing environment variable
- ✅ Add `APT_PACKAGES=tesseract-ocr` in Render environment

---

## Verification Commands

### Test Locally Before Deploying

**Test EasyOCR version:**
```bash
python app.py
# Visit: http://localhost:5000
```

**Test Pytesseract version:**
```bash
python app_tesseract.py
# Visit: http://localhost:5000
```

### Check Git Status
```bash
git status
git log --oneline -5
```

### Check Which Version is Active
```bash
# Check first few lines of app.py
head -n 20 app.py

# If you see "easyocr" → EasyOCR version
# If you see "pytesseract" → Pytesseract version
```

---

## Quick Reference

### Switch to Pytesseract (Free)
```bash
.\switch_to_pytesseract.bat
git add .
git commit -m "Switch to Pytesseract"
git push origin main
```

### Switch to EasyOCR (Paid)
```bash
.\switch_to_easyocr.bat
git add .
git commit -m "Switch to EasyOCR"
git push origin main
```

### Current Status
- ✅ Port binding: FIXED
- ✅ EasyOCR lazy loading: IMPLEMENTED
- ✅ Health endpoint: ADDED
- ✅ Pytesseract alternative: CREATED
- ⚠️ Memory issue: Choose your solution (Free vs Paid)

---

## Decision Time

**You need to pick ONE option:**

### Option A: Keep EasyOCR
- Costs $25/month
- Best accuracy
- Redeploy as-is (fixes already applied)

### Option B: Switch to Pytesseract
- FREE forever
- Good accuracy
- Run switch script and add env var

**Both will work. Which do you choose?**

---

**Next:** Open [QUICK_FIX.md](QUICK_FIX.md) for step-by-step instructions based on your choice.
