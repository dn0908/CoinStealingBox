from imports import *
from imports import SCALE_TABLE

class ProffesorBox:
    def __init__(self):
        # Arduino serial connection
        self.arduino = SerialWrapper(device=arduino_uno)

        # Set up MODI
        self.bundles = modi.MODI()
        print("\nStarting modi!")
        self.bundles.print_topology_map()

        self.led1 = self.bundles.leds[0]          # Led for left eye
        self.led2 = self.bundles.leds[1]          # Led for right eye
        self.display = self.bundles.displays[0]   # Display
        self.button = self.bundles.buttons[0]     # Button for turning on/off
        self.dial = self.bundles.dials[0]         # Dial for limit of receiving money
        self.speaker = self.bundles.speakers[0]   # Speaker for tunes

        # Flags
        self.power_flag : bool = False
        # Variables
        self.current_money = 0
        self.limit_money = 0
        self.count_for_button = 0
        self.count_threshold = 0
        self.money_list = [50, 100, 500, 1000, 5000, 10000, 50000]
    
    def check_on_off(self):
        self.count_for_button = 0
        while True:
            if self.button.pressed:
                print("pressed", self.count_for_button)
                self.count_for_button += 1
                if (self.count_for_button == 100): # Button pressed for 1 second
                    if self.power_flag:
                        self.power_flag = False
                    else: 
                        self.power_flag = True
                    self.count_for_button = 0

                    self.set_display()
                    break
            else:
                self.count_threshold += 1
                if (self.count_threshold > 20): # Button not pressed for 0.3 second
                    break
            time.sleep(0.01)

    def set_display(self):
        if self.power_flag == True:
            self.display.text = "Hello!!"
            time.sleep(3)
        else:
            self.display.text = "Bye!!"
            time.sleep(3)

            self.display.clear()

    def run(self):
        while True:
            if self.button.pressed: # check on/off when the button is pushed
                self.check_on_off()
            
            elif self.power_flag: # button is not pushed & device on
                self.display.text = "You have  " + str(self.current_money) + " Won!!"
                
                # Get money value from detection
                money_value = get_money_value_index_manual(self.button)
                
                # Search for money index
                money_index = 0
                for i in range(len(self.money_list)):
                    if money_value == self.money_list[i]:
                        money_index = i
                        break

                # Display
                money_str_list = ["   50", "  100", "  500", " 1000", " 5000", "10000", "50000"]
                display_str = "MONEY!!       " + money_str_list[money_index] + " W_W"
                self.display.text = display_str
                time.sleep(2)

                # Get limit money
                self.limit_money = MODI.get_limit_money(self.dial)
                print("limit:", self.limit_money)

                # Do action
                if money_value < self.limit_money:
                    self.display.text = "NO !!!!!!!! GO AWAY !!!"
                    self.led1.red = 100
                    self.led2.red = 100
                    
                    self.arduino.send_flag("1")
                    
                    MODI.sad_tune(self.speaker)
                    self.led1.turn_off()
                    self.led2.turn_off()
                else:
                    self.display.text = "YES !!!!!!! GIVE ME !!!"
                    self.current_money += money_value
                    self.led1.green = 50
                    self.led2.green = 50
                    
                    self.arduino.send_flag("2")

                    MODI.happy_tune(self.speaker, self.led1, self.led2)
                    self.led1.turn_off()
                    self.led2.turn_off()

                self.display.clear()


if __name__ == "__main__":
    print("HELLO WORLD")

    Box = ProffesorBox()

    Box.run()
    Box.run()

