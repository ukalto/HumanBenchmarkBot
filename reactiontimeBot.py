from PIL import ImageGrab
import pyautogui


def get_pixel_color(x, y):
    image = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
    color = image.getpixel((0, 0))
    return color


def click_at_position(x, y):
    pyautogui.click(x, y)


def monitor_pixel_change(target_x, target_y):
    while True:
        # Get the current pixel color
        current_color = get_pixel_color(target_x, target_y)

        # Check if the color has changed from red to green
        if current_color == (75, 219, 106):
            print("Pixel changed from red to green. Performing click.")

            # Perform a mouse click at a certain x and y position (modify as needed)
            click_at_position(target_x, target_y)
            if get_pixel_color(target_x, target_y) == (43, 135, 209):
                click_at_position(target_x, target_y)


if __name__ == "__main__":
    # Specify the target pixel position (modify as needed)
    target_x = 700
    target_y = 470

    # Start monitoring for pixel changes
    monitor_pixel_change(target_x, target_y)
