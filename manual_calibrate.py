#!/usr/bin/env python3
"""
Manual button position calibration tool.
Use this to manually set the exact button position.
"""

import pyautogui
import time
from PIL import ImageGrab
import cv2
import numpy as np

print("=" * 70)
print("  MANUAL BUTTON POSITION CALIBRATION")
print("=" * 70)
print()
print("This tool will help you manually set the button position.")
print()
print("Instructions:")
print("  1. Open the Vortex 'Download mod' dialog NOW")
print("  2. This script will wait 5 seconds")
print("  3. Move your mouse EXACTLY over the 'Download manually' button")
print("  4. Leave it there - don't move!")
print()

input("Press ENTER when ready...")

print("\nStarting in:")
for i in range(5, 0, -1):
    print(f"  {i}...")
    time.sleep(1)

print("\nCapturing mouse position...")
x, y = pyautogui.position()
screen_width, screen_height = pyautogui.size()

# Calculate percentages
x_percent = x / screen_width
y_percent = y / screen_height

print()
print("=" * 70)
print("  RESULTS")
print("=" * 70)
print()
print(f"Mouse Position: ({x}, {y})")
print(f"Screen Size: {screen_width}x{screen_height}")
print(f"Position as Percentage: ({x_percent:.3f}, {y_percent:.3f})")
print()

# Also capture and analyze the button color
screenshot = ImageGrab.grab()
screenshot_np = np.array(screenshot)

# Get a small region around the mouse
region_size = 50
x1 = max(0, x - region_size)
y1 = max(0, y - region_size)
x2 = min(screen_width, x + region_size)
y2 = min(screen_height, y + region_size)

button_region = screenshot_np[y1:y2, x1:x2]
button_hsv = cv2.cvtColor(button_region, cv2.COLOR_RGB2HSV)

# Get average color
avg_color_bgr = np.mean(button_region, axis=(0, 1))
avg_hsv = np.mean(button_hsv, axis=(0, 1))

print("Button Color Analysis:")
print(f"  RGB: ({avg_color_bgr[0]:.0f}, {avg_color_bgr[1]:.0f}, {avg_color_bgr[2]:.0f})")
print(f"  HSV: (H:{avg_hsv[0]:.0f}, S:{avg_hsv[1]:.0f}, V:{avg_hsv[2]:.0f})")
print()

print("=" * 70)
print("  CONFIGURATION CODE")
print("=" * 70)
print()
print("Add this to your config.py:")
print()
print(f"# Manual button position")
print(f"MANUAL_BUTTON_X = {x}")
print(f"MANUAL_BUTTON_Y = {y}")
print()
print("Or use percentages in main.py fallback:")
print()
print(f"click_x = int(screen_width * {x_percent:.3f})")
print(f"click_y = int(screen_height * {y_percent:.3f})")
print()
print("=" * 70)
print()
print("Would you like to test clicking this position? (y/n): ", end="")
test = input().strip().lower()

if test == 'y':
    print("\nClicking in 3 seconds...")
    time.sleep(3)
    pyautogui.click(x, y)
    print(f"Clicked at ({x}, {y})!")
    print("\nDid it click the correct button?")

print()
print("Done! Use the configuration code above to set the exact position.")


