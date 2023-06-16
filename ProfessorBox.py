from imports import *

from video_coin_count import get_money_value_index_manual
from serial_to_arduino import arduino_uno, SerialWrapper

SCALE_TABLE = {
    'FA5': 698,
    'SOL5': 783,
    'LA5': 880,
    'TI5': 988,
    'DO#5': 554,
    'RE#5': 622,
    'FA#5': 739,
    'SOL#5': 830,
    'LA#5': 932,
    'DO6': 1046,
    'RE6': 1174,
    'MI6': 1318,
    'FA6': 1397,
    'SOL6': 1567,
    'LA6': 1760,
    'TI6': 1975,
    'DO#6': 1108,
    'RE#6': 1244,
    'FA#6': 1479,
    'SOL#6': 1661,
    'LA#6': 1864,
    'DO7': 2093,
    'RE7': 2349,
    'MI7': 2637
}

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


    def get_limit_money(self):
        deg = self.dial.degree
        print(deg)

        if deg <= 15:
            self.limit_money = 50
        elif deg <= 29:
            self.limit_money = 100
        elif deg <= 43:
            self.limit_money = 500
        elif deg <= 57:
            self.limit_money = 1000
        elif deg <= 71:
            self.limit_money = 5000
        elif deg <= 85:
            self.limit_money = 10000
        elif deg <= 100:
            self.limit_money = 50000
        else:
            print("Something gone wrong with the dial")


    def check_on_off(self):
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

                    
    def happy_tune(self):
        ###########################################
        self.speaker.tune = SCALE_TABLE['TI5'], 100
        time.sleep(0.1)
        self.speaker.turn_off()
        time.sleep(0.001)
        self.speaker.tune = SCALE_TABLE['TI5'], 100
        time.sleep(0.1)
        self.speaker.turn_off()
        time.sleep(0.001)
        
        self.speaker.tune = SCALE_TABLE['RE#6'], 100
        time.sleep(0.1)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['FA#6'], 100
        time.sleep(0.2)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['RE#6'], 100
        time.sleep(0.1)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['FA#6'], 100
        time.sleep(0.4)
        self.speaker.turn_off()
        time.sleep(0.001)

        ###########################################
        self.speaker.tune = SCALE_TABLE['DO#6'], 100
        time.sleep(0.1)
        self.speaker.turn_off()
        time.sleep(0.001)
        self.speaker.tune = SCALE_TABLE['DO#6'], 100
        time.sleep(0.1)
        self.speaker.turn_off()
        time.sleep(0.001)
        
        self.speaker.tune = SCALE_TABLE['FA6'], 100
        time.sleep(0.1)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['SOL#6'], 100
        time.sleep(0.2)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['FA6'], 100
        time.sleep(0.1)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['SOL#6'], 100
        time.sleep(0.4)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.led1.turn_off()
        self.led2.turn_off()

    def sad_tune(self):
        self.speaker.tune = SCALE_TABLE['FA#6'], 100
        time.sleep(0.4)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['FA6'], 100
        time.sleep(0.4)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['MI6'], 100
        time.sleep(0.4)
        self.speaker.turn_off()
        time.sleep(0.001)

        self.speaker.tune = SCALE_TABLE['RE#6'], 100
        time.sleep(1)
        self.speaker.turn_off()
        time.sleep(0.001)


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
                self.get_limit_money()
                print("limit:", self.limit_money)

                # Do action
                if money_value < self.limit_money:
                    self.display.text = "NO !!!!!!!! GO AWAY !!!"
                    self.led1.red = 100
                    self.led2.red = 100
                    
                    self.arduino.send_flag("1")
                    
                    self.sad_tune()
                    self.led1.turn_off()
                    self.led2.turn_off()
                else:
                    self.display.text = "YES !!!!!!! GIVE ME !!!"
                    self.current_money += money_value
                    self.led1.green = 50
                    self.led2.green = 50
                    
                    self.arduino.send_flag("2")

                    self.happy_tune()
                    self.led1.turn_off()
                    self.led2.turn_off()

                self.display.clear()


if __name__ == "__main__":
    print("dd")

    Box = ProffesorBox()

    Box.run()
    Box.run()

