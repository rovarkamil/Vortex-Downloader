# Usage Guide - Vortex Auto Downloader

## Quick Start

### Step 1: Install Dependencies

Open PowerShell or Command Prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

### Step 2: Start the Program

**Option A: Using the batch script (Recommended)**
```bash
run.bat
```

**Option B: Direct Python command**
```bash
python main.py
```

### Step 3: Let It Run

Once started, the program will:
1. Monitor for Vortex download dialogs
2. Automatically click through the download process
3. Log all actions to the `logs` folder

## How to Use with Vortex

1. **Start the Auto Downloader**: Run the program using one of the methods above
2. **Use Vortex Normally**: In Vortex Mod Manager, start downloading mods as you normally would
3. **Hands Off**: When the "Download mod" dialog appears, the program will automatically:
   - Click "Download manually"
   - Wait for the browser to open
   - Click "Slow download" on the Nexus Mods page
4. **Multiple Downloads**: The program will handle multiple downloads automatically

## Stopping the Program

You have two options:

1. **Ctrl+C**: Press `Ctrl+C` in the terminal/command prompt window
2. **Mouse Failsafe**: Move your mouse cursor to the top-left corner of your screen

## Configuration

### Adjusting Settings

Edit `config.py` to customize the behavior:

#### Timing Settings
```python
CHECK_INTERVAL = 1          # How often to check for dialogs (seconds)
COOLDOWN_PERIOD = 10        # Wait time between downloads (seconds)
BROWSER_LOAD_WAIT = 3       # Wait for browser to load (seconds)
BUTTON_CLICK_DELAY = 2      # Delay after clicking buttons (seconds)
```

#### Button Position Adjustments

If the program can't find buttons, adjust these percentages:

```python
# For Vortex dialog button
VORTEX_BUTTON_X_PERCENT = 0.25  # 25% from left
VORTEX_BUTTON_Y_PERCENT = 0.75  # 75% from top

# For browser button
BROWSER_BUTTON_X_PERCENT = 0.25  # 25% from left
BROWSER_BUTTON_Y_PERCENT = 0.50  # 50% from top
```

#### Debug Mode

Enable debug screenshots to troubleshoot:

```python
SAVE_DEBUG_SCREENSHOTS = True   # Save screenshots for debugging
```

Screenshots will be saved to `debug_screenshots/` folder.

## Typical Workflow

### Example: Downloading a Mod Collection

1. **Prepare**:
   ```bash
   # Start the auto downloader
   python main.py
   ```

2. **In Vortex**: 
   - Click "Download" on a mod collection
   - The program detects the dialog and clicks "Download manually"

3. **Browser Opens**:
   - The program waits for the page to load
   - Automatically clicks "Slow download"

4. **Download Starts**:
   - The mod begins downloading
   - Program waits for the next download dialog

5. **Repeat**: The program continues monitoring and will handle the next download automatically

## Monitoring Progress

### Console Output

The program displays real-time information:
```
============================================================
Vortex Auto Downloader Started
============================================================
Monitoring for Vortex download dialogs...
Move mouse to top-left corner to stop (FAILSAFE)
------------------------------------------------------------
2025-11-01 18:30:45 - INFO - Detected Vortex download dialog!
2025-11-01 18:30:45 - INFO - Checking for Vortex download dialog...
2025-11-01 18:30:46 - INFO - Clicking 'Download manually' at (450, 620)
2025-11-01 18:30:48 - INFO - Successfully clicked 'Download manually'
2025-11-01 18:30:51 - INFO - Clicking 'Slow download' at (380, 540)
2025-11-01 18:30:52 - INFO - Successfully clicked 'Slow download'
2025-11-01 18:30:52 - INFO - Download process completed!
```

### Log Files

Check the `logs/` folder for detailed logs:
- Each run creates a new log file with timestamp
- Format: `vortex_auto_downloader_YYYYMMDD_HHMMSS.log`

## Troubleshooting

### Issue: Buttons Not Detected

**Solution 1**: Check debug screenshots
```python
# In config.py
SAVE_DEBUG_SCREENSHOTS = True
```
Look in `debug_screenshots/` to see what the program is seeing.

**Solution 2**: Adjust button detection ranges
```python
# In config.py
# Make the search area larger
VORTEX_SEARCH_TOP = 0.5  # Start searching earlier (was 0.6)
BROWSER_SEARCH_TOP = 0.2  # Start searching earlier (was 0.3)
```

**Solution 3**: Adjust button size filters
```python
# In config.py
# Make the acceptable button size range wider
VORTEX_BUTTON_MIN_WIDTH = 80    # Smaller minimum (was 100)
VORTEX_BUTTON_MAX_WIDTH = 350   # Larger maximum (was 300)
```

### Issue: Clicking in Wrong Location

**Solution**: Manually adjust fallback positions
1. Note where the button actually is on your screen
2. Adjust the percentage values in `config.py`:
```python
VORTEX_BUTTON_X_PERCENT = 0.30  # Adjust if button is more right/left
VORTEX_BUTTON_Y_PERCENT = 0.80  # Adjust if button is more up/down
```

### Issue: Program Runs but Does Nothing

**Checklist**:
1. Is the Vortex "Download mod" dialog visible on screen?
2. Is the dialog window not minimized?
3. Are you on the primary monitor? (works best on main display)
4. Check the logs for error messages

### Issue: Multiple Monitors

**Solution**: Move Vortex and browser windows to your primary monitor for best results.

### Issue: High DPI / Scaling

If you have display scaling (150%, 200%, etc.):

1. Run Python with DPI awareness:
   - Right-click `python.exe`
   - Properties → Compatibility
   - Check "Override high DPI scaling behavior"
   - Scaling performed by: Application

2. Or adjust the button size filters in `config.py` to match your scaling.

## Performance Tips

### For Collections with Many Mods

1. **Increase Cooldown**: Give more time between downloads
```python
COOLDOWN_PERIOD = 15  # Wait 15 seconds instead of 10
```

2. **Increase Wait Times**: Give pages more time to load
```python
BROWSER_LOAD_WAIT = 5  # Wait 5 seconds for browser (was 3)
```

### For Faster Systems

1. **Decrease Wait Times**: Speed up the process
```python
BROWSER_LOAD_WAIT = 2
BUTTON_CLICK_DELAY = 1
```

## Advanced Usage

### Running in Background

You can minimize the command prompt window and let it run in the background. Just remember:
- Don't close the window
- The program can still be stopped with the mouse failsafe

### Logging Different Levels

For more detailed logs:
```python
# In config.py
LOG_LEVEL = "DEBUG"  # Options: DEBUG, INFO, WARNING, ERROR
```

### Multiple Configurations

Create different config files for different setups:
1. Copy `config.py` to `config_1920x1080.py`, `config_2560x1440.py`, etc.
2. Modify `main.py` to import your desired config

## Safety Features

### Failsafe Protection
- Move mouse to corner to emergency stop
- Prevents accidental infinite loops

### Window Title Verification
- Only acts on windows titled "Download mod"
- Won't interfere with other applications

### Cooldown Period
- Prevents rapid repeated actions
- Gives you time to intervene if needed

### Error Handling
- Comprehensive error catching
- Detailed logging of all issues
- Graceful degradation to fallback positions

## Tips for Best Results

1. **Keep Windows Visible**: Don't minimize Vortex or browser windows
2. **Use Primary Monitor**: Best detection on main display
3. **Check Logs First**: Always check logs when troubleshooting
4. **Start with Defaults**: Try default settings before adjusting
5. **One Change at a Time**: When adjusting config, change one value at a time
6. **Test with One Mod**: Verify it works with a single mod before trying collections

## Support

If you encounter issues:
1. Check the `logs/` folder for error messages
2. Enable debug screenshots in `config.py`
3. Review the troubleshooting section above
4. Adjust configuration values one at a time

