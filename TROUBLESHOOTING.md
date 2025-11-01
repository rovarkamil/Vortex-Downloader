# Troubleshooting Guide

## Program Doesn't Detect the Vortex Dialog

### IMPORTANT DISCOVERY

The Vortex "Download mod" dialog is **NOT a separate window** - it's an embedded overlay/modal inside the main Vortex window! This is why the program was updated to use **screen-based detection** instead of window title detection.

The current version (after the update) uses screen-based button detection which works with embedded dialogs.

If the program runs but doesn't detect the download dialog, follow these steps:

### Step 1: Run the Window Debug Tool

```bash
python debug_windows.py
```

**Instructions:**
1. Run the command above
2. Open the Vortex "Download mod" dialog
3. Press ENTER in the debug tool window
4. Review the output

**What to look for:**
- Does it show "EXACT MATCH (Download mod)!"?
  - **YES**: Window detection works! The issue is with button detection (see Step 3)
  - **NO**: The window title is different (see Step 2)

### Step 2: Check Window Title

The debug tool will show you the actual window titles. Look for the Vortex dialog in the list.

**If the title is different:**

1. Note the exact window title from the debug tool output
2. Open `config.py`
3. Change this line:
```python
VORTEX_WINDOW_TITLE = "Download mod"
```
To match the actual title, for example:
```python
VORTEX_WINDOW_TITLE = "Vortex - Download"  # Use your actual title
```

**Common variations:**
- "Download mod"
- "Vortex - Download"
- "Download Mod"
- "Vortex Mod Manager - Download"

### Step 3: Check Button Detection

If the window IS detected but buttons aren't clicked:

1. Enable debug screenshots in `config.py`:
```python
SAVE_DEBUG_SCREENSHOTS = True
```

2. Run the program again

3. Check the `debug_screenshots/` folder for captured images

4. Open the screenshots and see where the buttons actually are

5. Adjust button positions in `config.py` based on the screenshots

### Step 4: Verify Verbose Logging

The program now logs more details. When you run it, you should see:

```
Looking for windows containing: 'Download mod'
```

Every 30 seconds, it will log all visible windows:
```
[Cycle 30] Performing verbose window check...
Checking window: 'Visual Studio Code'
Checking window: 'Chrome - New Tab'
...
```

**If you DON'T see your Vortex dialog in this list:**
- The window might be minimized (restore it)
- It might be a child window/embedded (not detectable)
- The window might not have a title bar

### Step 5: Check if Dialog is Visible

Make sure:
- ✅ The Vortex dialog is NOT minimized
- ✅ It's a separate window (has its own title bar)
- ✅ It's on your primary monitor
- ✅ It's not covered by other windows

### Step 6: Manual Button Position Calibration

If automatic detection fails, you can use fallback positions:

1. Take a screenshot of your screen with the Vortex dialog open
2. Note the button positions (pixel coordinates)
3. Calculate percentages:
   - X percent = button_x / screen_width
   - Y percent = button_y / screen_height
4. Update `config.py`:

```python
# Example: Button at 480px on a 1920px wide screen
# 480 / 1920 = 0.25
VORTEX_BUTTON_X_PERCENT = 0.25

# Example: Button at 900px on a 1080px tall screen  
# 900 / 1080 = 0.833
VORTEX_BUTTON_Y_PERCENT = 0.833
```

## Quick Diagnostic Checklist

Run through this checklist:

- [ ] I ran `python debug_windows.py` with the dialog open
- [ ] The debug tool shows my Vortex dialog window
- [ ] The window title in debug tool matches config.py
- [ ] The Vortex dialog is NOT minimized
- [ ] I enabled DEBUG logging in config.py
- [ ] I enabled debug screenshots in config.py
- [ ] I checked the logs/ folder for error messages
- [ ] I checked debug_screenshots/ folder for captured images

## Common Issues and Solutions

### Issue: Dialog appears but nothing happens

**Solution:**
```python
# In config.py, increase wait times
BROWSER_LOAD_WAIT = 5  # Give more time
BUTTON_CLICK_DELAY = 3
```

### Issue: Program clicks but in wrong location

**Solution:**
1. Check your screen scaling (Windows Display Settings)
2. If scaling is 150% or 200%, you may need to adjust coordinates
3. Run Python with DPI awareness (see USAGE.md)

### Issue: Works once, then stops

**Solution:**
```python
# In config.py, increase cooldown
COOLDOWN_PERIOD = 15  # Wait longer between downloads
```

### Issue: Browser button not found

**Solution:**
The "Slow download" button is on a web page. Make sure:
1. The browser window is NOT minimized
2. The page has finished loading
3. You're not using an ad blocker that hides the button
4. The page isn't showing a different layout

Try increasing the wait time:
```python
BROWSER_LOAD_WAIT = 5  # Wait 5 seconds instead of 3
```

## Advanced Debugging

### Enable Maximum Logging

```python
# config.py
LOG_LEVEL = "DEBUG"
SAVE_DEBUG_SCREENSHOTS = True
```

### Check Log Files

```bash
# View the latest log
cd logs
notepad vortex_auto_downloader_YYYYMMDD_HHMMSS.log
```

Look for:
- "Found window" messages (means detection works)
- "No window found" warnings (means detection fails)  
- "Clicking" messages (means it's trying to click)
- "ERROR" messages (something went wrong)

### Test Button Detection Manually

Create a test file `test_button_detection.py`:

```python
import pyautogui
import time

print("Move your mouse to the 'Download manually' button")
print("and leave it there...")
time.sleep(5)

x, y = pyautogui.position()
print(f"Button position: ({x}, {y})")
print(f"Screen size: {pyautogui.size()}")

screen_width, screen_height = pyautogui.size()
x_percent = x / screen_width
y_percent = y / screen_height

print(f"\nAdd to config.py:")
print(f"VORTEX_BUTTON_X_PERCENT = {x_percent:.3f}")
print(f"VORTEX_BUTTON_Y_PERCENT = {y_percent:.3f}")
```

Run this, position your mouse, and it will tell you the exact percentages to use.

## Still Not Working?

### Last Resort: Check These

1. **Antivirus/Security Software**: Some security software blocks PyAutoGUI
2. **Windows UAC**: Run PowerShell/CMD as administrator
3. **Python Version**: Make sure you have Python 3.8+
4. **Dependencies**: Run `python test_setup.py` to verify all packages
5. **Screen Setup**: Try using only your primary monitor

### Get More Help

If you've tried everything above:

1. Check the logs in `logs/` folder
2. Check debug screenshots in `debug_screenshots/` folder
3. Run `debug_windows.py` and note the output
4. Check what error messages appear

### Create a Detailed Report

Include:
- Python version: `python --version`
- Windows version
- Screen resolution
- Output from `debug_windows.py`
- Recent log file contents
- Debug screenshots (if any)
- Exact steps you followed

## Success Indicators

When it's working correctly, you'll see:

```
Looking for windows containing: 'Download mod'
Found window 'Download mod' at (x, y, w, h)
Detected Vortex download dialog!
Clicking 'Download manually' at (x, y)
Successfully clicked 'Download manually'
Clicking 'Slow download' at (x, y)
Successfully clicked 'Slow download'
Download process completed!
```

If you see this, everything is working! 🎉

