# Turtle-Beach-Vulkan-II-TKL-Brightness-Control

Let's your volume scroll turn from volume control to brightness control.

## Overview
This Python script specifically targets the volume scroll wheel on the **Turtle Beach Vulcan II TKL** keyboard. By default, the scroll wheel controls the system volume. This project intercepts those specific hardware signals (scan codes), blocks them from changing the volume, and reroutes them to adjust your monitor's screen brightness instead. 

It uses multithreading to ensure smooth operation without throwing Windows COM errors, allowing it to run silently in the background as a lightweight executable.

## Features
* **Hardware-Specific Interception:** Listens for the exact negative scan codes (`-175` for Up, `-174` for Down) sent by the Turtle Beach keyboard.
* **Volume Blocking:** Completely suppresses the default Windows volume adjustment when the wheel is scrolled.
* **Smooth Brightness Control:** Adjusts monitor brightness in 5% increments.
* **Background Execution:** Can be compiled into a hidden, windowless `.exe` that runs silently on startup.

## Prerequisites
* **OS:** Windows
* **Monitor:** A laptop display or a desktop monitor with **DDC/CI enabled** in its physical settings menu.
* **Python:** Python 3.x (if running from source).

## Installation & Setup

### 1. Install Dependencies
If you are running the script from source or plan to compile it yourself, install the required Python libraries:
```bash
pip install keyboard screen_brightness_control pyinstaller
