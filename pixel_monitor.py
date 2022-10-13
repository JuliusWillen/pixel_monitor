import ctypes
import time
import pyautogui
import time
import sys
import os
import random

from notify import Notify


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
        self.notify("SESSION_STARTED")
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
                    self.notify("SCREEN_CHANGED")
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
                    self.notify("SESSION_RESTARTED")
                else:
                    time.sleep(3)
        except:
            print("Something went wrong")
            self.notify("SESSION_STOPPED")


if __name__ == '__main__':
    input("Press ENTER to start the script...\n")
    pos = None
    press_enter = False
    if len(sys.argv) > 2:
        try:
            pos = pyautogui.Point(int(sys.argv[1]), int(sys.argv[2]))
            print("Got position from argument: ", pos)
        except:
            print("Invalid arguments.")
    if len(sys.argv) > 3:
        try:
            if sys.argv[3] == "True":
                print("Pressing enter after screen change")
                press_enter = True
        except:
            print("Invalid arguments.")

    pixel_monitor = PixelMonitor()
    if not pos:
        pos = pixel_monitor.get_mouse_position()
    # print the current time
    print(time.ctime())
    pixel_monitor.monitor_pixel(pos, press_enter)
