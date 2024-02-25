import display
import touch
import time
import device

def change_text(button):
    display.show(display.Text(f"Button {button} touched!", 0, 0, 0xffffff))
    button_flag = 1

def tap_text():
    display.show(display.Text("Tap a touch button", 0, 0, 0xffffff))

battery = device.battery_level()

display.show(display.Text("Tap a touch button", 0, 0, 0xffffff), display.Text(f"Battery is {battery}%", 200, 200, 0xffffff))

sleep = 0

while sleep<100:
    touch.callback(touch.BOTH, change_text)
    touch.callback(touch.A, change_text)
    touch.callback(touch.B, change_text)
    print(sleep)
    time.sleep_ms(100)
    sleep += 1

display.show(display.Text("Program All Done", 0, 0, 0xffffff))