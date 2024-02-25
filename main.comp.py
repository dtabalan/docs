import display
import touch
import time
import device



display.show(display.Text("Hello World", 200, 200, 0xffffff))
time.sleep(3)

battery = device.battery_level()
display.show(display.Text(f"Battery is {battery}%", 0, 0, 0xffffff), display.Text("Tap a button!", 200, 200, 0xffffff))
timer = 0

def main():
    print("In Main")

main()



