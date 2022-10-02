# pixel_monitor

Monitors a pixel on your screen and sends an e-mail when the pixel has changed color.
Currently only supporting Windows.

# dependencies

[yagmail](https://pypi.org/project/yagmail/)

[pyautogui](https://pyautogui.readthedocs.io/en/latest)

[dotenv](https://pypi.org/project/python-dotenv/)

# setup

1. install python 3.9
2. install the dependencies
3. make sure your gmail account is set to allow application logins [following this guide](https://support.google.com/accounts/answer/185833)
4. create file `.env` in the root folder based on `.env.example`
5. run screen.py
6. select a pixel on your screen
7. enjoy
