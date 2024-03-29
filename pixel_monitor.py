import ctypes
import time
import pyautogui
import time
import sys
import random

from notify import Notify
from message import Message


class PixelMonitor:
    def __init__(self):
        self.n = Notify()

    def notify(self, message):
        self.n.notify(message)

    def get_mouse_position(self):
        print("Choose position on screen to monitor")
        while True:
            # 0x01 is left mouse button
            if ctypes.windll.user32.GetKeyState(0x01) not in [0, 1]:
                pos = pyautogui.position()
                print("Chosen position:", pos)
                return pos

    def get_random_seconds(self):
        return random.randint(1, 60)

    def monitor_pixel(self, pos, press_enter=False):
        self.notify(Message.SESSION_STARTED)
        # get color of position
        color = pyautogui.pixel(pos.x, pos.y)
        print("Got color of chosen position: ", pos, color)
        try:
            while True:
                new_color = pyautogui.pixel(pos.x, pos.y)
                if new_color != color:
                    print("Color mismatch: ", new_color, color)
                    # print the current time
                    print(time.ctime())
                    pyautogui.screenshot('ss.png')
                    self.notify(Message.SCREEN_CHANGED)
                    seconds = self.get_random_seconds()
                    if press_enter:
                        print("Pressing enter after " +
                              str(seconds) + " seconds")
                        time.sleep(seconds)
                        pyautogui.press("enter")
                    print("Waiting 20 seconds before restarting script")
                    time.sleep(20)
                    print("Script restarted")
                    pyautogui.screenshot('ss.png')
                    self.notify(Message.SESSION_RESTARTED)
                else:
                    time.sleep(3)
        except:
            print("Something went wrong")
            self.notify(Message.SESSION_STOPPED)


if __name__ == '__main__':
    input("Press ENTER to start the script...\n")
    pos = None
    press_enter = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "enter":
            print("Pressing enter after screen change")
            press_enter = True

    pixel_monitor = PixelMonitor()
    if not pos:
        pos = pixel_monitor.get_mouse_position()
    # print the current time
    print(time.ctime())
    pixel_monitor.monitor_pixel(pos, press_enter)
