# Examples and Tutorials

## Example 1: Basic Usage

### Scenario
You want to download a single mod from Nexus Mods using Vortex.

### Steps
1. Start the auto downloader:
```bash
python main.py
```

2. In Vortex, click the download button for your mod

3. The program automatically:
   - Detects the "Download mod" dialog
   - Clicks "Download manually"
   - Clicks "Slow download" in the browser

4. Your download starts!

### Expected Output
```
============================================================
Vortex Auto Downloader Started
============================================================
Monitoring for Vortex download dialogs...
...
INFO - Detected Vortex download dialog!
INFO - Clicking 'Download manually' at (450, 620)
INFO - Successfully clicked 'Download manually'
INFO - Clicking 'Slow download' at (380, 540)
INFO - Successfully clicked 'Slow download'
INFO - Download process completed!
```

---

## Example 2: Downloading a Mod Collection

### Scenario
You want to download a collection with 50+ mods without clicking each one manually.

### Steps
1. Start the auto downloader first:
```bash
python main.py
```

2. In Vortex:
   - Go to Collections tab
   - Choose a collection
   - Click "Download"

3. Vortex will show multiple download dialogs, one for each mod

4. The program handles each dialog automatically with a 10-second cooldown between them

### Tips
- Don't move your mouse over the buttons (it won't interfere, but it's distracting)
- You can do other work on a second monitor
- Check the logs folder for a record of all downloads

---

## Example 3: Customizing for Your Screen Resolution

### Scenario
You have a 2560x1440 monitor and the default button positions aren't working.

### Steps
1. Enable debug mode in `config.py`:
```python
SAVE_DEBUG_SCREENSHOTS = True
```

2. Run the program and let it process one download

3. Check the `debug_screenshots` folder

4. Open the most recent screenshot and measure where the button is

5. Adjust `config.py` based on your measurements:

```python
# If button is at 640 pixels from left on a 2560-wide screen:
# 640 / 2560 = 0.25 (already correct)
VORTEX_BUTTON_X_PERCENT = 0.25

# If button is at 800 pixels from top on a 1440-tall screen:
# 800 / 1440 = 0.556
VORTEX_BUTTON_Y_PERCENT = 0.556  # Changed from 0.75
```

6. Save and test again

---

## Example 4: Adjusting Timing for Slow Internet

### Scenario
Your internet is slow and pages take longer to load. The program clicks before the page is ready.

### Solution
Increase wait times in `config.py`:

```python
# Give browser more time to load the page
BROWSER_LOAD_WAIT = 5  # Changed from 3 seconds

# Add extra delay after clicking buttons
BUTTON_CLICK_DELAY = 3  # Changed from 2 seconds

# Increase cooldown to avoid overwhelming your connection
COOLDOWN_PERIOD = 15  # Changed from 10 seconds
```

---

## Example 5: Troubleshooting Detection Issues

### Scenario
The program runs but never detects the buttons.

### Debugging Steps

**Step 1**: Verify window detection
```python
# In test_window_detection.py (create this file)
import win32gui

def list_windows():
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            windows.append(win32gui.GetWindowText(hwnd))
    
    windows = []
    win32gui.EnumWindows(callback, windows)
    for w in windows:
        if w:  # Only non-empty titles
            print(f"- {w}")

list_windows()
```

Run this when the Vortex dialog is open to see if it's detected.

**Step 2**: Check button detection parameters

Create a test script `test_detection.py`:

```python
import cv2
import numpy as np
from PIL import ImageGrab
import config

# Take a screenshot
screenshot = ImageGrab.grab()
screenshot_np = np.array(screenshot)
screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

# Apply edge detection
edges = cv2.Canny(screenshot_gray, config.CANNY_THRESHOLD_1, config.CANNY_THRESHOLD_2)

# Save for inspection
cv2.imwrite('test_edges.png', edges)
print("Edge detection image saved to test_edges.png")
```

Run this and check the output image to see if buttons are visible.

**Step 3**: Adjust detection sensitivity

If buttons aren't visible in the edge detection:
```python
# In config.py
CANNY_THRESHOLD_1 = 30  # Lower = more sensitive (was 50)
CANNY_THRESHOLD_2 = 100  # Lower = more sensitive (was 150)
```

---

## Example 6: Multiple Monitor Setup

### Scenario
You have 3 monitors and want to use the program while working on other screens.

### Best Practice Setup

1. **Primary Monitor**: Vortex and browser
   - This is where the program works best
   - Set this as your main display in Windows

2. **Secondary Monitors**: Your other work
   - You can work here without interfering

3. **Configuration**:
```python
# Keep default settings for primary monitor
# Don't adjust unless needed
```

### If Detection Fails on Secondary Monitors

The program works best on the primary monitor. If you need to use a secondary monitor:

1. Manually set the display as primary temporarily
2. Or adjust the coordinates in code (advanced)

---

## Example 7: Batch Processing with Logging

### Scenario
You're downloading 100+ mods overnight and want a detailed log.

### Setup
1. Enable detailed logging:
```python
# In config.py
LOG_LEVEL = "DEBUG"  # Maximum detail
```

2. Start the program:
```bash
python main.py > output.txt 2>&1
```

3. Start your downloads in Vortex

4. Let it run overnight

5. In the morning, check:
   - `logs/` folder for detailed logs
   - `output.txt` for console output

### Analyzing Logs

```bash
# Count successful downloads
grep "Download process completed" logs/vortex_auto_downloader_*.log | wc -l

# Find any errors
grep "ERROR" logs/vortex_auto_downloader_*.log

# See timing information
grep "Waiting" logs/vortex_auto_downloader_*.log
```

---

## Example 8: Creating a Custom Configuration

### Scenario
You have two computers with different screen setups and want separate configs.

### Solution

**Computer 1** (1920x1080, desktop):
```python
# config_desktop.py
CHECK_INTERVAL = 1
VORTEX_BUTTON_X_PERCENT = 0.25
VORTEX_BUTTON_Y_PERCENT = 0.75
BROWSER_BUTTON_X_PERCENT = 0.25
BROWSER_BUTTON_Y_PERCENT = 0.50
```

**Computer 2** (1366x768, laptop):
```python
# config_laptop.py
CHECK_INTERVAL = 1
VORTEX_BUTTON_X_PERCENT = 0.28  # Slightly different
VORTEX_BUTTON_Y_PERCENT = 0.78
BROWSER_BUTTON_X_PERCENT = 0.27
BROWSER_BUTTON_Y_PERCENT = 0.52
```

**Modify main.py**:
```python
# Change line 11 from:
import config
# To:
import config_desktop as config  # Or config_laptop
```

---

## Example 9: Safety Testing

### Scenario
You want to test the program safely before using it for real.

### Safe Testing Procedure

1. **Test the failsafe**:
   - Start the program
   - Immediately move mouse to top-left corner
   - Verify it stops

2. **Test with one mod**:
   - Start program
   - Download a single small mod
   - Watch the console output
   - Check if it works correctly

3. **Test the stop mechanism**:
   - Start program
   - Download a mod
   - Press Ctrl+C during the process
   - Verify it stops gracefully

4. **Review logs**:
   - Check `logs/` folder
   - Ensure all actions are logged
   - Verify error handling works

---

## Example 10: Performance Optimization

### Scenario
You want to maximize download speed while staying safe.

### Optimal Configuration

```python
# Faster checking
CHECK_INTERVAL = 0.5  # Check twice per second

# Faster response (if your system is fast)
BROWSER_LOAD_WAIT = 2
BUTTON_CLICK_DELAY = 1

# Shorter cooldown (but not too short!)
COOLDOWN_PERIOD = 5  # Minimum recommended

# Less sensitive detection (fewer false positives)
CONFIDENCE_THRESHOLD = 0.85  # Higher = more strict
```

### Warning
Don't set values too low:
- `COOLDOWN_PERIOD` < 5: May cause issues
- `BROWSER_LOAD_WAIT` < 2: May click before page loads
- `CHECK_INTERVAL` < 0.5: Unnecessary CPU usage

---

## Common Patterns

### Pattern 1: First Time Setup
1. Run `python test_setup.py`
2. Fix any missing dependencies
3. Run `python main.py` with one mod
4. Adjust config if needed
5. Use for collections

### Pattern 2: Regular Use
1. Start program: `python main.py`
2. Minimize window (don't close)
3. Use Vortex normally
4. Check logs periodically
5. Stop with Ctrl+C when done

### Pattern 3: Troubleshooting
1. Enable debug screenshots
2. Let program handle one download
3. Check screenshots
4. Adjust config
5. Test again
6. Disable debug screenshots when working

---

## Tips and Tricks

### Tip 1: Use the Batch File
The `run.bat` file handles errors better than running Python directly.

### Tip 2: Check Logs First
Before changing config, check logs to see what's actually happening.

### Tip 3: One Change at a Time
When troubleshooting, only change one config value at a time.

### Tip 4: Keep Default Config
Before editing `config.py`, make a copy called `config.backup.py`.

### Tip 5: Use Debug Mode Sparingly
Debug screenshots fill up disk space. Only enable when troubleshooting.

### Tip 6: Monitor Resource Usage
The program is lightweight but check Task Manager if you notice slowness.

### Tip 7: Regular Breaks
For large collections, the program handles everything, but Nexus might rate-limit. Take breaks between collections.

### Tip 8: Update Dependencies
Occasionally run `pip install -r requirements.txt --upgrade`.

### Tip 9: Clean Up Logs
Periodically delete old log files from the `logs/` folder.

### Tip 10: Read Error Messages
The program has detailed error messages. Read them before asking for help!

