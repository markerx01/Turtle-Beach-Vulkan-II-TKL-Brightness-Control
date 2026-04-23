import keyboard
import screen_brightness_control as sbc
import threading
import queue

STEP = 5

# Create a queue to hold brightness commands
action_queue = queue.Queue()


# Background worker that actually talks to the monitor
def brightness_worker():
    while True:
        # This will wait here until a command is dropped into the queue
        direction = action_queue.get()

        try:
            current_levels = sbc.get_brightness()
            if current_levels:
                current = current_levels[0]

                if direction == 'up':
                    new_level = min(current + STEP, 100)
                else:
                    new_level = max(current - STEP, 0)

                sbc.set_brightness(new_level)
                print(f"Success: Brightness changed to {new_level}%")
        except Exception as e:
            print(f"ERROR: {e}")

        # Tell the queue we finished the task
        action_queue.task_done()


# Start the background worker thread
worker_thread = threading.Thread(target=brightness_worker, daemon=True)
worker_thread.start()


# These are our ultra-fast keyboard interceptors.
# They just drop a note in the queue and finish instantly.
def scroll_up():
    action_queue.put('up')


def scroll_down():
    action_queue.put('down')


# Bind the hotkeys
keyboard.add_hotkey(-175, scroll_up, suppress=True)
keyboard.add_hotkey(-174, scroll_down, suppress=True)

print("Listening for scroll wheel... (Press Ctrl+C to stop)")
# Keep the main script running
keyboard.wait()
