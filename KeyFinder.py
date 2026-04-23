import keyboard

def on_key_event(e):
    print(f"Detected Key -> Name: '{e.name}', Scan code: {e.scan_code}, Event: {e.event_type}")

print("Listening for keys... Press ESC to stop.")
keyboard.hook(on_key_event)
keyboard.wait('esc')
