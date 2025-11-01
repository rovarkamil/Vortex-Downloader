@echo off
echo ============================================================
echo   VORTEX AUTO DOWNLOADER
echo ============================================================
echo.
echo Starting the Vortex Auto Downloader...
echo.
echo To stop the program:
echo   - Press Ctrl+C in this window, or
echo   - Move your mouse to the top-left corner of your screen
echo.
echo ============================================================
echo.

python main.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ============================================================
    echo ERROR: Failed to run the program
    echo ============================================================
    echo.
    echo Please make sure you have:
    echo   1. Python 3.8 or higher installed
    echo   2. Installed all requirements: pip install -r requirements.txt
    echo.
    pause
)

