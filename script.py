import time
import win32api, win32con
import keyboard
import pyautogui


if __name__ == "__main__":
    while not (keyboard.is_pressed("q")):
        try:
            points = pyautogui.locateOnScreen("icon.png",
                                            confidence=0.8,
                                            region=(197, 125, 825, 864),
                                            grayscale=True)
            win32api.SetCursorPos((points.left + points.width // 2 - 10,
                                points.top + points.height // 2))
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        except Exception as error:
            print(error)



