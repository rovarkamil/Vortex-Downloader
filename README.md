# Vortex Downloader Automation

Automatically clicks download buttons in Vortex mod manager and Nexus Mods website to streamline the mod collection download process.

## Features

- Automatically detects when the Vortex "Download mod" dialog appears
- Clicks the "Download manually" button in Vortex
- Detects when the Nexus Mods download page opens
- Clicks the "Slow download" button on Nexus Mods
- Runs continuously in the background
- Safe emergency stop (move mouse to screen corner)

## Requirements

- Python 3.8 or higher
- Windows 10/11 (for Windows API features)
- Vortex mod manager
- A web browser (Chrome, Firefox, Edge, or Brave)

## Installation

### Option 1: Run from Source

1. Install Python 3.8+ if not already installed
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python main.py
   ```

### Option 2: Build Executable (Recommended)

The build scripts automatically create and use a virtual environment to keep dependencies isolated from your system Python.

**Windows:**
```bash
build.bat
```

**Linux/Mac:**
```bash
chmod +x build.sh
./build.sh
```

The executable will be created in the `dist` folder:
- Windows: `dist\VortexDownloader.exe`
- Linux/Mac: `dist/VortexDownloader`

**Note:** The build scripts will create a `venv` folder in the project directory. This virtual environment contains all dependencies and is separate from your system Python installation.

## Usage

1. **Start the automation:**
   - Double-click `VortexDownloader.exe` (or run `python main.py`)

2. **Use Vortex normally:**
   - When a "Download mod" dialog appears, the script will automatically:
     - Detect the dialog
     - Click "Download manually"
     - Wait for the browser to open
     - Click "Slow download" on the Nexus Mods page

3. **Stop the automation:**
   - Press `Ctrl+C` in the console window, OR
   - Move your mouse to any corner of the screen (emergency stop)

## How It Works

The automation uses:
- **Window detection**: Finds Vortex and browser windows using Windows API
- **Image matching**: Uses template matching with example screenshots (optional)
- **Smart clicking**: Calculates button positions based on window locations
- **Continuous monitoring**: Checks every 2 seconds for dialogs

## Configuration

You can adjust the check interval by modifying `main.py`:

```python
downloader = VortexDownloader(check_interval=2.0)  # Check every 2 seconds
```

## Troubleshooting

### Button not being clicked
- Make sure Vortex and your browser are not minimized
- Ensure windows are visible on the primary monitor
- The script needs to detect windows, so they must be active/visible

### False detections
- The script uses multiple detection methods (window titles, template matching)
- If issues persist, you may need to adjust button position calculations in the code

### Import errors
- Install missing dependencies: `pip install -r requirements.txt`
- On Windows, `pywin32` is required for window detection

## Notes

- The script uses relative button positions based on typical dialog layouts
- First run may require calibration if your screen resolution or UI scaling differs
- Works best on single-monitor setups (primary monitor)
- The automation respects system failsafe (move mouse to corner to stop)

## License

This project is provided as-is for personal use.

