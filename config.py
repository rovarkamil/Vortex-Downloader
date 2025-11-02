# Vortex Auto Downloader Configuration

# Timing Settings
CHECK_INTERVAL = 1  # How often to check for dialogs (seconds)
COOLDOWN_PERIOD = 10  # Time to wait between processing downloads (seconds)
BROWSER_LOAD_WAIT = 3  # Time to wait for browser page to load (seconds)
BUTTON_CLICK_DELAY = 2  # Delay after clicking buttons (seconds)
DOWNLOAD_CONFIRMATION_WAIT = 2  # Wait after clicking download button for confirmation page (seconds)
TAB_CLOSE_DELAY = 6  # Wait this many seconds before closing tab after clicking download (seconds)
                        # Nexus Mods has a 5-second countdown, so wait at least that long + buffer

# Detection Settings
CONFIDENCE_THRESHOLD = 0.8  # Image matching confidence (0.0 to 1.0)
MIN_BUTTON_AREA = 1000  # Minimum pixel area for button detection

# Button Position Fallbacks (as percentage of window/screen dimensions)
# Vortex Dialog "Download manually" button
VORTEX_BUTTON_X_PERCENT = 0.25  # 25% from left
VORTEX_BUTTON_Y_PERCENT = 0.75  # 75% from top

# Browser "Slow download" button  
BROWSER_BUTTON_X_PERCENT = 0.638  # 63.8% from left
BROWSER_BUTTON_Y_PERCENT = 0.558  # 55.8% from top

# Search Regions (as percentage of window/screen dimensions)
# For "Download manually" button in Vortex dialog
VORTEX_SEARCH_TOP = 0.6  # Start searching at 60% from top
VORTEX_SEARCH_LEFT = 0.0  # Start from left edge
VORTEX_SEARCH_RIGHT = 0.5  # Search up to 50% of width (left half)

# For "Slow download" button in browser
BROWSER_SEARCH_TOP = 0.3  # Start searching at 30% from top
BROWSER_SEARCH_BOTTOM = 0.7  # Stop searching at 70% from top
BROWSER_SEARCH_LEFT = 0.0  # Start from left edge
BROWSER_SEARCH_RIGHT = 0.5  # Search up to 50% of width (left half)

# Button Size Filters (pixels)
# Vortex dialog button dimensions
VORTEX_BUTTON_MIN_WIDTH = 100
VORTEX_BUTTON_MAX_WIDTH = 300
VORTEX_BUTTON_MIN_HEIGHT = 30
VORTEX_BUTTON_MAX_HEIGHT = 60

# Browser button dimensions
BROWSER_BUTTON_MIN_WIDTH = 150
BROWSER_BUTTON_MAX_WIDTH = 400
BROWSER_BUTTON_MIN_HEIGHT = 40
BROWSER_BUTTON_MAX_HEIGHT = 80

# Edge Detection Settings
CANNY_THRESHOLD_1 = 50
CANNY_THRESHOLD_2 = 150

# Threshold Settings for Dark Button Detection
BUTTON_THRESHOLD_VALUE = 80  # Pixels darker than this are considered button areas

# Window Title Keywords
VORTEX_WINDOW_TITLE = "Download mod"

# Browser Tab Management
AUTO_CLOSE_DOWNLOAD_TABS = True  # Automatically close browser tabs after download starts
                                  # This prevents too many tabs from opening
KEEP_ONE_TAB_OPEN = True  # After closing first tab, keep subsequent tabs open
                          # This keeps the browser window open and ready

# Debug Settings
SAVE_DEBUG_SCREENSHOTS = True  # Save screenshots for debugging
DEBUG_SCREENSHOT_DIR = "debug_screenshots"

# PyAutoGUI Settings
PYAUTOGUI_PAUSE = 0.5  # Pause between PyAutoGUI actions (seconds)
PYAUTOGUI_FAILSAFE = True  # Enable failsafe (move mouse to corner to stop)

# Logging Settings
LOG_DIR = "logs"
LOG_LEVEL = "DEBUG"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
                     # Use DEBUG for troubleshooting, INFO for normal operation
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Manual Button Position (from calibration)
# These are used as fallback if automatic detection fails
# Percentages of screen size - adjust if your screen resolution changes
MANUAL_BUTTON_X_PERCENT = 0.167  # 16.7% from left (button at x=321 on 1920px screen)
MANUAL_BUTTON_Y_PERCENT = 0.413  # 41.3% from top (button at y=446 on 1080px screen)

