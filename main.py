"""
Vortex Downloader Automation
Automatically clicks download buttons in Vortex mod manager and Nexus Mods website.
"""

import pyautogui
import cv2
import numpy as np
import time
import sys
import os
from pathlib import Path
from typing import Optional, Tuple

# Fix Windows console encoding for Unicode characters
if sys.platform == 'win32':
    try:
        # Try to set UTF-8 encoding for console output
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except:
        # Fallback: just ensure ASCII-safe output
        pass

# Configure PyAutoGUI
pyautogui.FAILSAFE = True  # Move mouse to corner to stop
pyautogui.PAUSE = 0.5  # Small pause between actions

class VortexDownloader:
    def __init__(self, check_interval: float = 2.0):
        """
        Initialize the Vortex Downloader automation.
        
        Args:
            check_interval: Time in seconds between screen checks
        """
        self.check_interval = check_interval
        self.running = False
        # Get script directory - works both as script and as executable
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            self.script_dir = Path(sys.executable).parent
        else:
            # Running as script
            self.script_dir = Path(__file__).parent if '__file__' in globals() else Path.cwd()
        
    def find_image_on_screen(self, template_path: str, confidence: float = 0.8) -> Optional[Tuple[int, int]]:
        """
        Find an image template on the screen using template matching.
        
        Args:
            template_path: Path to the template image file
            confidence: Minimum confidence level for matching (0.0-1.0)
            
        Returns:
            Center coordinates (x, y) if found, None otherwise
        """
        try:
            # Take a screenshot
            screenshot = pyautogui.screenshot()
            screenshot_np = np.array(screenshot)
            screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
            
            # Load template
            template_path_obj = Path(template_path)
            if not template_path_obj.is_absolute():
                template_path_obj = self.script_dir / template_path_obj
            
            if not template_path_obj.exists():
                print(f"Warning: Template image not found at {template_path_obj}")
                return None
                
            template = cv2.imread(str(template_path_obj), cv2.IMREAD_GRAYSCALE)
            if template is None:
                print(f"Warning: Could not load template image from {template_path_obj}")
                return None
            
            # Perform template matching
            result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            if max_val >= confidence:
                # Calculate center of the matched area
                h, w = template.shape
                center_x = max_loc[0] + w // 2
                center_y = max_loc[1] + h // 2
                return (center_x, center_y)
            
            return None
            
        except Exception as e:
            print(f"Error in find_image_on_screen: {e}")
            return None
    
    def find_button_by_text(self, button_text: str, region: Optional[Tuple[int, int, int, int]] = None) -> Optional[Tuple[int, int]]:
        """
        Find a button by searching for text on the screen.
        
        Args:
            button_text: Text to search for
            region: Optional (x, y, width, height) region to search in
            
        Returns:
            Center coordinates (x, y) if found, None otherwise
        """
        try:
            location = pyautogui.locateOnScreen(
                None,  # We'll use text recognition if available
                region=region,
                confidence=0.8
            )
            
            # Fallback: Use pyautogui's locate with image if we have template images
            # For now, we'll use approximate button positions based on dialog layout
            return None
            
        except Exception as e:
            print(f"Error in find_button_by_text: {e}")
            return None
    
    def find_vortex_download_manually_button(self) -> Optional[Tuple[int, int]]:
        """
        Find the 'Download manually' button in the Vortex dialog.
        Based on the dialog layout, this button is in the left panel, bottom section.
        """
        # Try to find the button using template matching if we have a template
        # For now, we'll search the screen for common button patterns
        
        try:
            # Take screenshot and analyze
            screenshot = pyautogui.screenshot()
            
            # Look for the "Download manually" button
            # This button is typically dark gray and located in the left panel
            # We'll use a color-based approach combined with position estimation
            
            # Method 1: Try using pyautogui's built-in image search if we create templates
            # Method 2: Use approximate coordinates based on screen center
            # Method 3: Search for button-like regions
            
            # For robustness, we'll use a combination approach:
            # - Search for the Vortex dialog window first
            # - Then calculate relative position of the button
            
            # Search in the center-left region of screen (where Vortex dialogs typically appear)
            screen_width, screen_height = pyautogui.size()
            search_region = (
                screen_width // 4,  # Start from 25% from left
                screen_height // 4,  # Start from 25% from top
                screen_width // 2,   # Width: 50% of screen
                screen_height // 2   # Height: 50% of screen
            )
            
            # Try to find common button colors (dark gray buttons)
            # This is a simplified approach - in production, you'd use image templates
            
            # For now, return None and use fallback coordinate-based approach
            return None
            
        except Exception as e:
            print(f"Error finding Vortex button: {e}")
            return None
    
    def find_nexus_slow_download_button(self) -> Optional[Tuple[int, int]]:
        """
        Find the 'Slow download' button on the Nexus Mods webpage.
        """
        try:
            # Search in the center region where download buttons typically appear
            screen_width, screen_height = pyautogui.size()
            search_region = (
                screen_width // 4,
                screen_height // 3,
                screen_width // 2,
                screen_height // 2
            )
            
            # Similar approach - use template matching or coordinate-based search
            return None
            
        except Exception as e:
            print(f"Error finding Nexus button: {e}")
            return None
    
    def click_vortex_manual_download(self, dialog_rect: Optional[Tuple[int, int, int, int]] = None) -> bool:
        """
        Click the 'Download manually' button in the Vortex dialog.
        
        Args:
            dialog_rect: Dialog rectangle (left, top, right, bottom) if known
        
        Returns:
            True if click was successful, False otherwise
        """
        try:
            screen_width, screen_height = pyautogui.size()
            
            # Use provided dialog rect or try to detect it
            if dialog_rect is None:
                dialog_rect = self.detect_vortex_dialog()
            
            if dialog_rect:
                # Calculate button position based on dialog
                left, top, right, bottom = dialog_rect
                dialog_width = right - left
                dialog_height = bottom - top
                
                # Based on the dialog layout:
                # - Dialog is split into left (Free) and right (Premium) panels
                # - "Download manually" button is in the LEFT panel at the bottom
                # - Left panel takes up roughly 50% of dialog width
                # - Button is approximately 80-85% down from the top of dialog
                
                # Button position: in left panel (~25% from left edge), ~82% down from top
                button_x = left + (dialog_width * 0.25)
                button_y = top + (dialog_height * 0.82)
                
                print(f"Dialog rect: {dialog_rect}")
                print(f"Dialog size: {dialog_width}x{dialog_height}")
                print(f"Clicking Vortex 'Download manually' button at ({int(button_x)}, {int(button_y)})")
                
                # Move mouse and click
                pyautogui.moveTo(int(button_x), int(button_y), duration=0.3)
                time.sleep(0.2)
                pyautogui.click()
                time.sleep(2)  # Wait for browser to open
                return True
            else:
                # Fallback: center-based estimation
                dialog_center_x = screen_width // 2
                dialog_center_y = screen_height // 2
                # Dialog is roughly 800x600, button in left panel bottom
                button_x = dialog_center_x - 250  # Left panel, offset from center
                button_y = dialog_center_y + 180  # Below center
                
                print(f"Dialog not detected, using fallback coordinates")
                print(f"Clicking Vortex 'Download manually' button at ({int(button_x)}, {int(button_y)})")
                pyautogui.moveTo(int(button_x), int(button_y), duration=0.3)
                time.sleep(0.2)
                pyautogui.click()
                time.sleep(2)
                return True
            
        except Exception as e:
            print(f"Error clicking Vortex button: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def click_nexus_slow_download(self) -> bool:
        """
        Click the 'Slow download' button on the Nexus Mods webpage.
        
        Returns:
            True if click was successful, False otherwise
        """
        try:
            screen_width, screen_height = pyautogui.size()
            
            # Method 1: Try to find browser window
            browser_rect = None
            if sys.platform == 'win32':
                try:
                    import win32gui
                    
                    def enum_windows_callback(hwnd, windows):
                        if win32gui.IsWindowVisible(hwnd):
                            window_title = win32gui.GetWindowText(hwnd)
                            title_lower = window_title.lower()
                            if any(browser in title_lower for browser in ['chrome', 'firefox', 'edge', 'brave']):
                                if 'nexusmods' in title_lower or 'nexus' in title_lower:
                                    rect = win32gui.GetWindowRect(hwnd)
                                    windows.append(rect)
                    
                    windows = []
                    win32gui.EnumWindows(enum_windows_callback, windows)
                    if windows:
                        browser_rect = windows[0]
                        print(f"Found browser window at {browser_rect}")
                
                except ImportError:
                    pass
            
            # Calculate button position
            if browser_rect:
                # Button is in left download panel, roughly centered vertically
                # Account for browser UI (address bar, tabs, etc.)
                browser_width = browser_rect[2] - browser_rect[0]
                browser_height = browser_rect[3] - browser_rect[1]
                # Content area starts below browser UI (~100px from top)
                content_top = browser_rect[1] + 100
                # Button is in left panel (~25% from left), roughly 60% down in content
                button_x = browser_rect[0] + (browser_width * 0.25)
                button_y = content_top + (browser_height * 0.50)
            else:
                # Fallback: center-based estimation
                button_x = screen_width // 2 - 200  # Left panel, offset from center
                button_y = screen_height // 2 + 100  # Below center (accounting for browser UI)
            
            # Verify coordinates
            if 0 < button_x < screen_width and 0 < button_y < screen_height:
                print(f"Clicking Nexus 'Slow download' button at ({int(button_x)}, {int(button_y)})")
                pyautogui.click(int(button_x), int(button_y))
                time.sleep(1)
                return True
            
            return False
            
        except Exception as e:
            print(f"Error clicking Nexus button: {e}")
            return False
    
    def detect_vortex_dialog(self) -> Optional[Tuple[int, int, int, int]]:
        """
        Detect if the Vortex download dialog is visible on screen.
        
        Returns:
            Dialog rectangle (left, top, right, bottom) if found, None otherwise
        """
        try:
            # Method 1: Use template matching with example image
            vortex_template = self.script_dir / "example" / "vortex-example.png"
            if vortex_template.exists():
                location = self.find_image_on_screen(str(vortex_template), confidence=0.6)
                if location:
                    # Return approximate dialog rectangle centered on found location
                    # Typical dialog size is around 800x600
                    x, y = location
                    dialog_rect = (x - 400, y - 300, x + 400, y + 300)
                    print(f"Vortex dialog found via template matching at {location}")
                    return dialog_rect
            
            # Method 2: Check for Vortex modal dialog windows using Windows API
            if sys.platform == 'win32':
                try:
                    import win32gui
                    import win32con
                    
                    vortex_windows = []
                    dialog_windows = []
                    
                    def enum_windows_callback(hwnd, data):
                        if win32gui.IsWindowVisible(hwnd):
                            window_title = win32gui.GetWindowText(hwnd)
                            class_name = win32gui.GetClassName(hwnd).lower()
                            title_lower = window_title.lower()
                            
                            # Find main Vortex window
                            if 'vortex' in title_lower or 'vortex' in class_name:
                                rect = win32gui.GetWindowRect(hwnd)
                                width = rect[2] - rect[0]
                                height = rect[3] - rect[1]
                                
                                # Check if it's a dialog (smaller than main window, typically 600-900px wide)
                                if 500 <= width <= 1200 and 400 <= height <= 900:
                                    # Check if it has a parent (modal dialog)
                                    parent = win32gui.GetParent(hwnd)
                                    owner = win32gui.GetWindow(hwnd, win32con.GW_OWNER)
                                    if parent or owner or 'download' in title_lower:
                                        dialog_windows.append((hwnd, rect, window_title))
                    
                    win32gui.EnumWindows(enum_windows_callback, None)
                    
                    if dialog_windows:
                        # Use the first dialog found
                        hwnd, rect, title = dialog_windows[0]
                        print(f"Found Vortex dialog window: '{title}' at {rect}")
                        return rect
                    
                    # Alternative: Find main Vortex window and look for child dialogs
                    def find_main_vortex(hwnd, data):
                        if win32gui.IsWindowVisible(hwnd):
                            window_title = win32gui.GetWindowText(hwnd)
                            if 'vortex' in window_title.lower() and 'cyberpunk' in window_title.lower():
                                data.append(hwnd)
                    
                    main_windows = []
                    win32gui.EnumWindows(find_main_vortex, main_windows)
                    
                    if main_windows:
                        # Look for child windows/dialogs
                        main_hwnd = main_windows[0]
                        
                        def enum_child_windows(hwnd, data):
                            if win32gui.IsWindowVisible(hwnd):
                                rect = win32gui.GetWindowRect(hwnd)
                                width = rect[2] - rect[0]
                                height = rect[3] - rect[1]
                                if 500 <= width <= 1200 and 400 <= height <= 900:
                                    data.append(rect)
                        
                        child_dialogs = []
                        win32gui.EnumChildWindows(main_hwnd, enum_child_windows, child_dialogs)
                        
                        if child_dialogs:
                            print(f"Found {len(child_dialogs)} child dialog(s)")
                            return child_dialogs[0]
                        
                        # If no child dialog, check all top-level windows again with relaxed criteria
                        def find_any_dialog(hwnd, data):
                            if win32gui.IsWindowVisible(hwnd):
                                rect = win32gui.GetWindowRect(hwnd)
                                width = rect[2] - rect[0]
                                height = rect[3] - rect[1]
                                # Look for modal-sized windows in center of screen
                                center_x = (rect[0] + rect[2]) // 2
                                center_y = (rect[1] + rect[3]) // 2
                                screen_width, screen_height = pyautogui.size()
                                # Dialog should be roughly centered
                                if (screen_width * 0.2 < center_x < screen_width * 0.8 and
                                    screen_height * 0.2 < center_y < screen_height * 0.8 and
                                    500 <= width <= 1200 and 400 <= height <= 900):
                                    title = win32gui.GetWindowText(hwnd)
                                    # Prioritize windows with empty or short titles (typical for dialogs)
                                    if len(title) < 50:  # Dialogs often have short/no titles
                                        data.append((rect, len(title)))
                        
                        dialogs = []
                        win32gui.EnumWindows(find_any_dialog, dialogs)
                        if dialogs:
                            # Sort by title length (shorter = more likely dialog)
                            dialogs.sort(key=lambda x: x[1])
                            print(f"Found potential dialog at {dialogs[0][0]}")
                            return dialogs[0][0]
                    
                except ImportError:
                    pass
                except Exception as e:
                    print(f"Error in window detection: {e}")
            
            return None
            
        except Exception as e:
            print(f"Error detecting Vortex dialog: {e}")
            return None
    
    def detect_nexus_page(self) -> bool:
        """
        Detect if the Nexus Mods download page is open.
        
        Returns:
            True if Nexus page is detected, False otherwise
        """
        try:
            # Method 1: Use template matching with example image
            nexus_template = self.script_dir / "example" / "web-example.png"
            if nexus_template.exists():
                location = self.find_image_on_screen(str(nexus_template), confidence=0.6)
                if location:
                    print(f"Nexus page found at {location}")
                    return True
            
            # Method 2: Check for browser window with Nexus in title
            if sys.platform == 'win32':
                try:
                    import win32gui
                    
                    def enum_windows_callback(hwnd, windows):
                        if win32gui.IsWindowVisible(hwnd):
                            window_title = win32gui.GetWindowText(hwnd)
                            # Check for common browser windows with Nexus
                            title_lower = window_title.lower()
                            if any(browser in title_lower for browser in ['chrome', 'firefox', 'edge', 'brave']):
                                if 'nexusmods' in title_lower or 'nexus' in title_lower:
                                    windows.append(hwnd)
                    
                    windows = []
                    win32gui.EnumWindows(enum_windows_callback, windows)
                    if windows:
                        print(f"Found {len(windows)} Nexus browser window(s)")
                        return True
                    
                except ImportError:
                    pass
                except Exception as e:
                    print(f"Error in browser window detection: {e}")
            
            return False
            
        except Exception as e:
            print(f"Error detecting Nexus page: {e}")
            return False
    
    def run(self):
        """
        Main loop: Continuously monitor for dialogs and click buttons.
        """
        print("Vortex Downloader Automation Started")
        print("Press Ctrl+C to stop, or move mouse to corner for emergency stop")
        print(f"Checking every {self.check_interval} seconds...\n")
        
        self.running = True
        vortex_clicked = False
        nexus_clicked = False
        last_check_time = 0
        vortex_click_time = 0
        
        try:
            while self.running:
                current_time = time.time()
                
                # Check if enough time has passed for main loop
                if current_time - last_check_time < self.check_interval:
                    time.sleep(0.1)
                    continue
                
                last_check_time = current_time
                
                # Step 1: Check for Vortex dialog
                if not vortex_clicked:
                    dialog_rect = self.detect_vortex_dialog()
                    if dialog_rect:
                        print("Vortex dialog detected!")
                        if self.click_vortex_manual_download(dialog_rect):
                            vortex_clicked = True
                            vortex_click_time = current_time
                            nexus_clicked = False  # Reset for next download
                            print("Clicked 'Download manually' button")
                        else:
                            print("Failed to click Vortex button")
                    else:
                        # Reset if dialog disappeared - but allow it to keep checking
                        pass  # Don't reset vortex_clicked here, let it continue checking
                
                # Step 2: Check for Nexus page after Vortex click
                elif vortex_clicked and not nexus_clicked:
                    # Give browser time to open and load (at least 2 seconds after click)
                    if current_time - vortex_click_time >= 2:
                        if self.detect_nexus_page():
                            print("Nexus page detected!")
                            # Wait for page to fully load
                            time.sleep(1)
                            if self.click_nexus_slow_download():
                                nexus_clicked = True
                                print("Clicked 'Slow download' button")
                                # Reset for next cycle immediately to catch next dialog
                                print("Download cycle complete, ready for next mod...")
                                vortex_clicked = False
                                nexus_clicked = False
                                vortex_click_time = 0
                                # Small delay before checking for next dialog
                                time.sleep(1)
                            else:
                                print("Failed to click Nexus button, will retry...")
                        else:
                            # If we clicked Vortex but no Nexus page yet, keep waiting
                            # Print status every 3 seconds
                            elapsed = int(current_time - vortex_click_time)
                            if elapsed > 0 and elapsed % 3 == 0:
                                print(f"Waiting for Nexus page to open... ({elapsed}s elapsed)")
                            
                            # Timeout after 30 seconds and reset
                            if elapsed > 30:
                                print("Timeout waiting for Nexus page, resetting...")
                                vortex_clicked = False
                                nexus_clicked = False
                                vortex_click_time = 0
                
                # Small delay to prevent CPU spinning
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\n\nStopping automation...")
            self.running = False
        except Exception as e:
            print(f"\n\nError in main loop: {e}")
            self.running = False


def test_detection():
    """Test function to check if dialog detection is working."""
    print("=" * 60)
    print("Testing Vortex Dialog Detection")
    print("=" * 60)
    print()
    
    downloader = VortexDownloader(check_interval=1.0)
    
    print("Looking for Vortex dialog...")
    print("(This will run for 30 seconds, press Ctrl+C to stop early)\n")
    
    import time
    start_time = time.time()
    dialog_rect = None
    
    try:
        while time.time() - start_time < 30:
            dialog_rect = downloader.detect_vortex_dialog()
            if dialog_rect:
                print(f"\n[OK] Dialog detected! Rectangle: {dialog_rect}")
                print(f"  Button would be clicked at approximately: "
                      f"({dialog_rect[0] + int((dialog_rect[2] - dialog_rect[0]) * 0.25)}, "
                      f"{dialog_rect[1] + int((dialog_rect[3] - dialog_rect[1]) * 0.82)})")
                break
            else:
                print(".", end="", flush=True)
            time.sleep(1)
        
        if dialog_rect is None:
            print("\n\n[X] No dialog detected in 30 seconds.")
            print("Make sure:")
            print("  1. Vortex is running")
            print("  2. A 'Download mod' dialog is open")
            print("  3. The dialog is visible on your primary monitor")
    
    except KeyboardInterrupt:
        print("\n\nTest stopped by user.")


def main():
    """Entry point for the application."""
    print("=" * 60)
    print("Vortex Downloader Automation")
    print("=" * 60)
    print()
    
    # Check if test mode requested
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_detection()
        return
    
    downloader = VortexDownloader(check_interval=2.0)
    downloader.run()


if __name__ == "__main__":
    main()
