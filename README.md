# Vortex Auto Downloader

Automates the Nexus Mods download process when using Vortex Mod Manager without a Premium account. The program automatically detects the Vortex download dialog and clicks through the "Download manually" button and then the "Slow download" button in the browser.

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the program
python main.py

# 3. Use Vortex normally - the program handles downloads automatically!
```

**That's it!** The program will monitor for download dialogs and automatically click through them.

## Features

- 🔍 **Auto-Detection**: Monitors for Vortex "Download mod" dialogs
- 🖱️ **Auto-Click**: Automatically clicks "Download manually" and "Slow download" buttons
- 📝 **Logging**: Comprehensive logging to track all actions
- 🛡️ **Failsafe**: Move mouse to top-left corner to stop the program
- ⏱️ **Smart Cooldown**: 10-second cooldown between processes to avoid issues
- 🔄 **Continuous Monitoring**: Runs in the background and handles multiple downloads

## Requirements

- Python 3.8 or higher
- Windows OS (uses win32gui for window detection)
- All dependencies listed in `requirements.txt`

## Installation

1. Clone or download this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running from Python

```bash
python main.py
```

### Building Executable (Optional)

If you want to create a standalone executable:

```bash
pyinstaller --onefile --windowed --name VortexAutoDownloader main.py
```

The executable will be in the `dist` folder.

## How It Works

1. **Monitoring Phase**: The program continuously monitors for windows with "Download mod" in the title
2. **Dialog Detection**: When a Vortex download dialog is detected, it analyzes the window
3. **Click Download Manually**: Uses computer vision to locate and click the "Download manually" button
4. **Wait for Browser**: Waits for the browser page to load (3 seconds)
5. **Click Slow Download**: Locates and clicks the "Slow download" button on the Nexus Mods page
6. **Cooldown**: Waits 10 seconds before checking for the next download

## Configuration

You can modify these settings in the `VortexAutoDownloader` class:

- `check_interval`: How often to check for dialogs (default: 1 second)
- `confidence`: Image matching confidence threshold (default: 0.8)
- `cooldown`: Time to wait between processes (default: 10 seconds)

## Stopping the Program

You can stop the program in two ways:
1. Press `Ctrl+C` in the terminal
2. Move your mouse to the top-left corner of the screen (PyAutoGUI failsafe)

## Troubleshooting

### Button Not Detected

If the program can't find the buttons:
1. Check the `debug_screenshots` folder for captured screenshots
2. Review the logs in the `logs` folder
3. Adjust the button detection thresholds in the code

### Clicks in Wrong Location

- The program uses fallback positions based on typical button locations
- You may need to adjust the percentage values in `click_download_manually()` and `click_slow_download()` methods

### Multiple Monitors

- The program works with multiple monitors
- Make sure the Vortex dialog and browser are on your primary monitor for best results

## Logs

Logs are automatically saved to the `logs` folder with timestamps:
- Format: `vortex_auto_downloader_YYYYMMDD_HHMMSS.log`
- Contains detailed information about detection and clicking actions

## Safety Features

- **PyAutoGUI Failsafe**: Move mouse to corner to emergency stop
- **Cooldown Period**: Prevents rapid repeated actions
- **Window Title Verification**: Only acts on windows with "Download mod" in title
- **Error Handling**: Comprehensive error handling with logging

## Technical Details

### Detection Methods

1. **Window Detection**: Uses win32gui to find windows by title
2. **Button Detection**: Uses OpenCV for computer vision-based button detection
3. **Edge Detection**: Canny edge detection to find button boundaries
4. **Contour Analysis**: Finds button-sized rectangles within the interface
5. **Fallback Positions**: Uses expected button positions as fallback

### Image Processing

- Converts screenshots to grayscale for analysis
- Uses Canny edge detection for button boundaries
- Applies thresholding to find dark buttons on light backgrounds
- Filters contours by size to match button dimensions

## Limitations

- Only works on Windows (uses win32gui)
- Requires visible windows (doesn't work with minimized windows)
- May need adjustment for different screen resolutions or DPI settings
- Works best when Vortex and browser are on primary monitor

## Disclaimer

This tool is for educational purposes and personal use only. Respect Nexus Mods' terms of service and consider supporting them with a Premium membership if you download mods frequently.

## License

MIT License - Feel free to modify and use as needed.
