import ctypes
import time
import pyautogui
import yagmail
import settings
import time
import sys


MAIL_SCREEN_CHANGED = (settings.TO_MAIL, "Screen changed!",
                       ["Screen has changed. Please check your computer. Script is paused for 60 seconds!", "ss.png"])
MAIL_SESSION_STARTED = (settings.TO_MAIL, "Screen monitor session started!",
                        ["Screen is being monitored. You will receive a mail when the screen updates!"])
MAIL_SESSION_STOPPED = (settings.TO_MAIL, "Screen monitor session stopped!",
                        ["Something went wrong."])


def send_mail(yag, mail):
    print("Sending mail:", mail)
    yag.send(mail[0], mail[1], mail[2])


def get_mouse_position(watchtime=60):
    start = time.time()
    while True:
        # 0x01 is left mouse button
        if ctypes.windll.user32.GetKeyState(0x01) not in [0, 1]:
            return pyautogui.position()
        elif time.time() - start >= watchtime:
            break
        time.sleep(0.001)
    return False


def monitor_pixel(pos, yag):
    # get color of position
    color = pyautogui.pixel(pos.x, pos.y)
    print("Got color of chosen position: ", pos, color)
    try:
        while True:
            new_color = pyautogui.pixel(pos.x, pos.y)
            print("Color on chosen position:", new_color)
            time.sleep(3)  # wait for 3 seconds
            if new_color != color:
                print("Color mismatch: ", new_color, color)
                pyautogui.screenshot('ss.png')
                send_mail(yag, MAIL_SCREEN_CHANGED)
                time.sleep(60)  # wait 60 seconds
    except:
        print("Something went wrong")
        send_mail(yag, MAIL_SESSION_STOPPED)


if __name__ == '__main__':
    input("Press ENTER to start the script...\n")
    pos = None
    if len(sys.argv) > 2:
        pos = pyautogui.Point(int(sys.argv[1]), int(sys.argv[2]))
        print("Got position from argument: ", pos)
    else:
        pos = get_mouse_position()
    yag = yagmail.SMTP(settings.USERNAME, settings.PASSWORD)
    send_mail(yag, MAIL_SESSION_STARTED)
    monitor_pixel(pos, yag)
