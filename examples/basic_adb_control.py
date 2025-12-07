"""
Basic ADB Control Example

This script demonstrates how to use droidrun's ADB tools to control an Android device
without modifying the droidrun package itself. This is a standalone example that shows
the most basic operations like starting and stopping apps.

Prerequisites:
1. Install droidrun: pip install droidrun
2. Connect an Android device or emulator
3. Enable USB debugging on the device

Usage:
    python basic_adb_control.py
"""

import asyncio
from droidrun.tools.adb import AdbTools


async def stop_app(tools: AdbTools, package: str) -> str:
    """
    Stop (force-close) an app on the device.

    This is a basic example function that uses the same ADB connection
    as droidrun, but without modifying the droidrun package.

    Args:
        tools: An initialized AdbTools instance
        package: Package name of the app to stop (e.g., "com.android.chrome")

    Returns:
        Result message indicating success or error
    """
    try:
        print(f"Stopping app: {package}")
        # Use the device's shell method to execute the force-stop command
        await tools.device.shell(f"am force-stop {package}")
        print(f"✓ App stopped: {package}")
        return f"App stopped: {package}"
    except Exception as e:
        error_msg = f"Error stopping app: {str(e)}"
        print(f"✗ {error_msg}")
        return error_msg


async def main():
    """
    Main function demonstrating basic ADB operations.
    """
    print("=" * 60)
    print("Basic ADB Control Example")
    print("=" * 60)

    # Initialize ADB tools
    # If you have multiple devices, specify serial like: AdbTools(serial="emulator-5554")
    tools = AdbTools()

    try:
        # Connect to the device
        print("\n1. Connecting to device...")
        await tools.connect()
        print("✓ Connected to device")

        # Example 1: Start an app
        print("\n2. Starting Chrome browser...")
        package = "com.android.chrome"
        result = await tools.start_app(package)
        print(f"✓ {result}")

        # Wait a few seconds
        print("\n3. Waiting 3 seconds...")
        await asyncio.sleep(3)

        # Example 2: Stop the app using our custom function
        print("\n4. Stopping Chrome using custom stop_app function...")
        await stop_app(tools, package)

        # Example 3: Get device info
        print("\n5. Getting device information...")
        device_info = await tools.device.shell("getprop ro.product.model")
        print(f"✓ Device model: {device_info.strip()}")

        # Example 4: Check if app is installed
        print("\n6. Checking if Chrome is installed...")
        app_list = await tools.device.shell(f"pm list packages | grep {package}")
        if package in app_list:
            print(f"✓ {package} is installed")
        else:
            print(f"✗ {package} is not installed")

        print("\n" + "=" * 60)
        print("Example completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        print("\nMake sure you have:")
        print("  1. An Android device or emulator connected")
        print("  2. USB debugging enabled")
        print("  3. ADB working (try 'adb devices' in terminal)")

    finally:
        # Cleanup
        if tools.device:
            print("\nDisconnecting...")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
