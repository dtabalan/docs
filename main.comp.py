import display
import touch
import time
import device

def change_text(button):
    display.show(display.Text((f"Button {button} touched!", 0, 0, 0xffffff)))
    single_button_flag = 1

'''
def tap_text():
    display.show(display.Text("Tap a touch button", 0, 0, 0xffffff))

def exit_tap(button):
    Both_button_text = display.Text(f"Button {button} touched!", 0, 0, 0xffffff)
    exit = 1



def update_display():
    if single_button_flag == 1:
        display.show(single_text)
'''

def delay():
    time.sleep_ms(100)

display.show(display.Text("Tap a touch button", 0, 0, 0xffffff), display.Text(f"Battery is {battery}%", 200, 200, 0xffffff))

sleep = 0
exit = 0

while TRUE:
    battery = device.battery_level()
    touch.callback(touch.BOTH, exit_tap)
    touch.callback(touch.A, change_text)
    touch.callback(touch.B, change_text)
    print(sleep)
    delay()
    if exit == 1:
        continue

    display.show(display.Text("Program All Done", 0, 0, 0xffffff))

#main()


