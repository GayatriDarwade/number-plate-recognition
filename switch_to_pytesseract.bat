@echo off
REM Switch to Pytesseract version for free deployment

echo ================================
echo Switching to Pytesseract Version
echo ================================
echo.

REM Backup current files
echo Backing up current files...
copy app.py app_easyocr_backup.py
copy requirements.txt requirements_easyocr_backup.txt
echo.

REM Switch to Pytesseract
echo Switching to Pytesseract version...
copy /Y app_tesseract.py app.py
copy /Y requirements_tesseract.txt requirements.txt
echo.

echo ================================
echo Switch Complete!
echo ================================
echo.
echo Next steps:
echo 1. Test locally: python app.py
echo 2. Commit changes: git add . ^&^& git commit -m "Switch to Pytesseract"
echo 3. Push to deploy: git push origin main
echo 4. In Render, add environment variable: APT_PACKAGES=tesseract-ocr
echo.
echo To revert to EasyOCR:
echo Run: switch_to_easyocr.bat
echo.
pause
