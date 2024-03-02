import display
import touch
import time
import device
import uasynchio



display.show(display.Text("Hello World", 200, 200, 0xffffff), display.Rectangle(150, 150, 500, 300, display.CYAN))
time.sleep(3)

battery = device.battery_level()
display.show(display.Text(f"Battery is {battery}%", 0, 0, 0xffffff), display.Text("Tap a button!", 100, 200, 0xffffff))
timer = 0
    

def main(button):
    if button == "BOTH":
        #print("Exit")
        test = display.Text("Bye Bye",100, 100, 0xffffff)
    else:
        test = display.Text("",100, 100, 0xffffff)
    
    display.show(display.Text(f"Battery is {battery}%", 0, 0, 0xffffff), display.Text(f"Button {button} was pressed", 100, 200, 0xffffff), test)

#print("In Main")
touch.callback(touch.A, main)
touch.callback(touch.B, main)
touch.callback(touch.BOTH, main)