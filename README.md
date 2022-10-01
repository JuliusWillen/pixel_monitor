# pixel_monitor
Monitors a pixel on your screen and sends an e-mail when the pixel has changed color. 
Currently only supporting Windows.

# dependencies
[yagmail](https://pypi.org/project/yagmail/)

[pyautogui](https://pyautogui.readthedocs.io/en/latest)

# setup
1. install python 3.9
2. install the dependencies
3. make sure your gmail account is set to allow application logins [following this guide](https://support.google.com/accounts/answer/185833)  
4. create a file "settings.py" in the root folder
5. set USERNAME=[your gmail address you want to send mails from]
6. set PASSWORD=[your gmail password you created in step 3]
7. set TO_MAIL=[your desired target e-mail address, can be the same as your USERNAME]
9. run screen.py
10. select a pixel on your screen
11. enjoy


