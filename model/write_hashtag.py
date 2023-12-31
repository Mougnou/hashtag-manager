from pynput.mouse import Button, Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
from view.alerte_box import AlerteBox
import time

class ClickAndType:
    def __init__(self):
        self.mouse = Controller()
        self.keyboard = KeyboardController()
        self.alerte_box = AlerteBox()

    def click_and_type(self, text, waiting_time, x, y):
        #sleep for x seconds
        old_position = self.mouse.position
        if waiting_time == '' and x == '' and y == '':
            self.alerte_box.setting_alert()
            return None
        if waiting_time != '':
            time.sleep(int(waiting_time))

        # Get the current cursor position
        if x != '' and y != '':
            current_position = int(x),int(y)
        else:
            current_position = self.mouse.position

        # Move the cursor back to the original position
        self.mouse.position = current_position

        # Click at the current cursor position
        self.mouse.click(Button.left)

        # Type the given text using the keyboard
        for word in text:
            self.keyboard.type(word)
            self.keyboard.press(Key.space)
            self.keyboard.release(Key.space)
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)
            
        

        self.mouse.position = old_position
