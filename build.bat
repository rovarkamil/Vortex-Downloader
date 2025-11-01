@echo off
echo Building Vortex Downloader executable...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created.
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1

REM Install/upgrade dependencies
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

REM Build executable with PyInstaller
echo.
echo Creating executable...
pyinstaller --onefile --console --name "VortexDownloader" --icon=NONE main.py

if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)

REM Deactivate virtual environment (optional, script will end anyway)
call venv\Scripts\deactivate.bat >nul 2>&1

echo.
echo ========================================
echo Build successful!
echo Executable location: dist\VortexDownloader.exe
echo ========================================
echo.
pause

