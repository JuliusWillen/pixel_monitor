# pixel_monitor

Monitors a pixel on your screen and sends an e-mail when the pixel has changed color.
Currently only supporting Windows.

# dependencies

[yagmail](https://pypi.org/project/yagmail/)

[pyautogui](https://pyautogui.readthedocs.io/en/latest)

[dotenv](https://pypi.org/project/python-dotenv/)

# prerequisites

1. a google account
2. python 3.9
3. windows

# setup

1. install the dependencies
2. make sure your google account is set to allow application logins [following this guide](https://support.google.com/accounts/answer/185833)
3. create file `.env` in the root folder based on `.env.example`
4. run `pixel_monitor.py`
5. follow the instructions in the application
