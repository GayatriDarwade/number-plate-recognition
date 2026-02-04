@echo off
REM Switch back to EasyOCR version

echo ================================
echo Switching to EasyOCR Version
echo ================================
echo.

REM Check if backups exist
if not exist app_easyocr_backup.py (
    echo Error: Backup files not found!
    echo Using original app.py...
    pause
    exit /b 1
)

REM Restore from backup
echo Restoring EasyOCR version...
copy /Y app_easyocr_backup.py app.py
copy /Y requirements_easyocr_backup.txt requirements.txt
echo.

echo ================================
echo Switch Complete!
echo ================================
echo.
echo IMPORTANT: EasyOCR requires more memory!
echo - Free tier (512MB): Will likely FAIL
echo - Upgrade to Standard plan ($25/mo, 2GB RAM) recommended
echo.
echo Next steps:
echo 1. Test locally: python app.py
echo 2. Commit changes: git add . ^&^& git commit -m "Switch to EasyOCR"
echo 3. Push to deploy: git push origin main
echo 4. Upgrade Render plan if needed
echo.
pause
