#!/usr/bin/env python3
"""
Debug script to list all visible windows and help diagnose detection issues.
Run this while the Vortex download dialog is open.
"""

import win32gui
import time

def list_all_windows():
    """List all visible windows with their titles."""
    windows = []
    
    def callback(hwnd, windows_list):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:  # Only non-empty titles
                rect = win32gui.GetWindowRect(hwnd)
                x1, y1, x2, y2 = rect
                windows_list.append({
                    'hwnd': hwnd,
                    'title': title,
                    'x': x1,
                    'y': y1,
                    'width': x2 - x1,
                    'height': y2 - y1
                })
    
    win32gui.EnumWindows(callback, windows)
    return windows

def main():
    print("=" * 70)
    print("  VORTEX DOWNLOADER - WINDOW DEBUG TOOL")
    print("=" * 70)
    print()
    print("This tool will help diagnose window detection issues.")
    print()
    print("Instructions:")
    print("  1. Keep this window open")
    print("  2. Open the Vortex 'Download mod' dialog")
    print("  3. Press ENTER in this window")
    print()
    input("Press ENTER when the Vortex dialog is visible...")
    
    print()
    print("Scanning for windows...")
    print()
    
    windows = list_all_windows()
    
    print(f"Found {len(windows)} visible windows:")
    print("=" * 70)
    
    # Look for potential Vortex windows
    vortex_candidates = []
    download_candidates = []
    
    for i, window in enumerate(windows, 1):
        title_lower = window['title'].lower()
        
        # Check if this might be the Vortex dialog
        if 'download' in title_lower or 'vortex' in title_lower or 'mod' in title_lower:
            marker = " ← POTENTIAL MATCH!"
            if 'download' in title_lower and 'mod' in title_lower:
                download_candidates.append(window)
                marker = " ← EXACT MATCH (Download mod)!"
            elif 'vortex' in title_lower:
                vortex_candidates.append(window)
            
            print(f"\n{i}. {window['title']}{marker}")
        else:
            print(f"\n{i}. {window['title']}")
        
        print(f"   Position: ({window['x']}, {window['y']})")
        print(f"   Size: {window['width']}x{window['height']}")
        print(f"   Handle: {window['hwnd']}")
    
    print()
    print("=" * 70)
    print("ANALYSIS:")
    print("=" * 70)
    
    if download_candidates:
        print(f"\n✓ Found {len(download_candidates)} window(s) matching 'Download mod':")
        for window in download_candidates:
            print(f"  - '{window['title']}'")
            print(f"    Position: ({window['x']}, {window['y']})")
            print(f"    Size: {window['width']}x{window['height']}")
        print("\nThe program SHOULD detect these windows.")
        print("If it's not working, the issue is likely with button detection.")
        
    elif vortex_candidates:
        print(f"\n⚠ Found {len(vortex_candidates)} Vortex-related window(s):")
        for window in vortex_candidates:
            print(f"  - '{window['title']}'")
        print("\nBut none match 'Download mod' exactly.")
        print("The window title might be different than expected.")
        
    else:
        print("\n✗ No windows found containing 'download', 'mod', or 'vortex'")
        print("\nPossible issues:")
        print("  1. The dialog is not actually visible (minimized/hidden)")
        print("  2. The dialog is in a different window/iframe")
        print("  3. The dialog title is completely different")
        print("\nTry these steps:")
        print("  1. Make sure the dialog is NOT minimized")
        print("  2. Make sure it's a separate window (not embedded)")
        print("  3. Take a screenshot and check the window title bar")
    
    print()
    print("=" * 70)
    print()
    
    # Additional check for browser windows (for second step)
    browser_candidates = []
    for window in windows:
        title_lower = window['title'].lower()
        if any(browser in title_lower for browser in ['chrome', 'firefox', 'edge', 'opera', 'brave']):
            if 'nexusmods' in title_lower or 'download' in title_lower:
                browser_candidates.append(window)
    
    if browser_candidates:
        print("BROWSER WINDOWS (for step 2 - Slow download button):")
        print("=" * 70)
        for window in browser_candidates:
            print(f"\n- {window['title']}")
            print(f"  Position: ({window['x']}, {window['y']})")
            print(f"  Size: {window['width']}x{window['height']}")
        print()
    
    print("=" * 70)
    print("\nFor more help:")
    print("  1. Check USAGE.md for troubleshooting tips")
    print("  2. Enable debug screenshots in config.py")
    print("  3. Check logs/ folder for error messages")
    print("=" * 70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    except Exception as e:
        print(f"\n\nError: {e}")
        import traceback
        traceback.print_exc()


