import pyautogui,time
from pynput.keyboard import Key, Controller

#pyautogui.mouseInfo()

time.sleep(4)

#pyautogui.displayMousePosition()
#pyautogui.mouseInfo()

def fallguys():

    while True:

        time.sleep(3)

        pyautogui.rightClick(x=1688,y=1003)
        time.sleep(1)
        pyautogui.rightClick(x=1688,y=1003)
        time.sleep(1)
        keyboard = Controller()

#keyboard.press(Key.esc)
#keyboard.release(Key.esc)
#time.sleep(1)
#keyboard.press(Key.space)
#keyboard.release(Key.space)
#time.sleep()

        keyboard.press(Key.space)
        keyboard.release(Key.space)

        for i in range(9999999999999999):

            im = pyautogui.screenshot()
            px = pyautogui.pixel(x=1596, y=1046)

            time.sleep(2)

            if px == (255, 255, 255):

                keyboard.press(Key.esc)
                keyboard.release(Key.esc)

                pyautogui.rightClick(x=1688, y=1003)

                keyboard.press(Key.space)
                keyboard.release(Key.space)

                print("Mr.Lgzey Target detected !!")
                time.sleep(12)

                keyboard.press(Key.space)
                keyboard.release(Key.space)

                break
            else:
                continue

fallguys()

#key = "spacebar"
#keyboard.press(key)
#keyboard.release(key)
#time.sleep(3)
#keyboard.type('Welcome Mr.Lgzey , We are fsociety We are her for help you')