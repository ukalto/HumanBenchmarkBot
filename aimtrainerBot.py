import pyautogui
import time
from PIL import ImageGrab
from pynput import mouse
import numpy as np

start_script = False


def on_click(x, y, button, pressed):
    global start_script
    if pressed:
        start_script = True


def take_screenshot(left, top, width, height):
    screenshot = ImageGrab.grab(bbox=(left, top, left + width, top + height))
    return screenshot


def check_color(image, target_color):
    image_array = np.array(image)
    target_array = np.array(target_color)

    match_coordinates = np.argwhere(np.all(image_array == target_array, axis=-1))

    if match_coordinates.size > 0:
        x, y = match_coordinates[0]
        return int(y) + 840, int(x) + 250

    return None


def main():
    global start_script

    # Define the area to capture
    capture_area = (840, 225, 1060, 455)  # (left, top, width, height)

    # Define the target color to check for
    target_color = (149, 195, 232)  # RGB value

    listener = mouse.Listener(on_click=on_click)
    listener.start()

    try:
        print("waiting...")
        while not start_script:
            time.sleep(0.01)

        print("Script started.")

        for _ in range(35):
            # Take a screenshot of the specified area
            screenshot = take_screenshot(*capture_area)

            # Check if the target color appears in the screenshot
            pixel_position = check_color(screenshot, target_color)

            if pixel_position:
                pyautogui.click(pixel_position)
                print(f"Clicked at ({pixel_position[0]}, {pixel_position[1]})")

            # Wait for a short duration before taking the next screenshot
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("Script terminated by user.")
    finally:
        listener.stop()
        listener.join()


if __name__ == "__main__":
    main()
