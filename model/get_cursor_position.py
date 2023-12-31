from pynput.mouse import Listener, Button

class CursorPosition:
    def submit_clicked(self):
        # Start a MouseListener
        with Listener(on_click=self.on_click) as listener:
            # Wait for the user to click
            listener.join()

    def on_click(self, x, y, button, pressed):
        # If the left button is pressed
        if button == Button.left and pressed:
            # Print the position of the cursor
            self.mouse_position = x,y

            #return the position of the cursor then stop the listener
            return False

