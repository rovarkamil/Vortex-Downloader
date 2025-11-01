#!/usr/bin/env python3
"""
Test script to verify that all dependencies are installed correctly
and that the program can run.
"""

import sys
import importlib

def test_import(module_name, display_name=None):
    """Test if a module can be imported."""
    if display_name is None:
        display_name = module_name
    
    try:
        importlib.import_module(module_name)
        print(f"✓ {display_name} is installed")
        return True
    except ImportError as e:
        print(f"✗ {display_name} is NOT installed: {e}")
        return False

def main():
    """Run all setup tests."""
    print("=" * 60)
    print("  VORTEX AUTO DOWNLOADER - SETUP TEST")
    print("=" * 60)
    print()
    print("Testing Python version...")
    
    # Check Python version
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} (OK)")
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} (Need 3.8+)")
        print()
        print("Please upgrade Python to version 3.8 or higher")
        return False
    
    print()
    print("Testing required packages...")
    
    # Test all required packages
    all_ok = True
    packages = [
        ("pyautogui", "PyAutoGUI"),
        ("cv2", "OpenCV"),
        ("PIL", "Pillow"),
        ("numpy", "NumPy"),
    ]
    
    # Test win32gui on Windows
    if sys.platform == "win32":
        packages.append(("win32gui", "PyWin32"))
    
    for module, display in packages:
        if not test_import(module, display):
            all_ok = False
    
    print()
    print("Testing configuration...")
    
    try:
        import config
        print("✓ config.py is accessible")
    except ImportError:
        print("✗ config.py not found")
        all_ok = False
    
    print()
    print("Testing main program...")
    
    try:
        import main
        print("✓ main.py can be imported")
    except Exception as e:
        print(f"✗ main.py has errors: {e}")
        all_ok = False
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("  ✓ ALL TESTS PASSED!")
        print("=" * 60)
        print()
        print("Your setup is ready! You can now run:")
        print("  python main.py")
        print()
        print("Or use the batch script:")
        print("  run.bat")
        print()
    else:
        print("  ✗ SOME TESTS FAILED")
        print("=" * 60)
        print()
        print("Please install missing dependencies:")
        print("  pip install -r requirements.txt")
        print()
    
    return all_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

