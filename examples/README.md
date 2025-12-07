# Droidrun Examples

This directory contains standalone example scripts that demonstrate how to use droidrun without modifying the package itself.

## Available Examples

### basic_adb_control.py

A simple example showing how to:
- Connect to an Android device
- Start and stop apps
- Create custom functions using droidrun's ADB tools
- Get device information

**Usage:**
```bash
# Make sure you have droidrun installed
pip install droidrun

# Connect your Android device or start an emulator
adb devices

# Run the example
python examples/basic_adb_control.py
```

**What it demonstrates:**
- Using `AdbTools` class without modifying droidrun
- Creating a custom `stop_app()` function
- Basic ADB shell commands
- Error handling and device connection

## Creating Your Own Functions

You can create your own automation functions by:

1. **Import the AdbTools class:**
```python
from droidrun.tools.adb import AdbTools
```

2. **Initialize and connect:**
```python
tools = AdbTools()
await tools.connect()
```

3. **Use the device object for ADB commands:**
```python
# Execute shell commands
await tools.device.shell("am force-stop com.example.app")

# Use built-in methods
await tools.start_app("com.android.chrome")
```

4. **Create standalone functions:**
```python
async def my_custom_function(tools: AdbTools):
    # Your custom logic here
    result = await tools.device.shell("your-adb-command")
    return result
```

## Prerequisites

- Python 3.11 or higher
- Android device or emulator with USB debugging enabled
- ADB working on your system (`adb devices` should show your device)
- Droidrun installed (`pip install droidrun`)

## Getting Help

- Documentation: https://docs.droidrun.ai
- Issues: https://github.com/droidrun/droidrun/issues
- Discord: https://discord.gg/ZZbKEZZkwK
