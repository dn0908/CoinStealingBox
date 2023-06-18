from imports import *

# Check ON/OFF
def check_on_off(button, display, power_flag, count_for_button, count_threshold):
        count_for_button = 0
        while True:
            if button.pressed:
                print("pressed", count_for_button)
                count_for_button += 1
                if (count_for_button == 100): # Button pressed for 1 second
                    if power_flag:
                        power_flag = False
                    else: 
                        power_flag = True
                    count_for_button = 0
                    set_display(display, power_flag)
                    break
            else:
                count_threshold += 1
                if (count_threshold > 30): # Button not pressed for 0.3 second
                    break
            time.sleep(0.01)

# Set Display Module
def set_display(display, power_flag):
        if power_flag == True:
            display.text = "Hello!!"
            time.sleep(3)
        else:
            display.text = "Bye!!"
            time.sleep(3)
        display.clear()

# Dial Module get limit value
def get_limit_money(dial_module):
    deg = dial_module.degree
    if deg <= 15:
        limit_money = 50
    elif deg <= 29:
        limit_money = 100
    elif deg <= 43:
        limit_money = 500
    elif deg <= 57:
        limit_money = 1000
    elif deg <= 71:
        limit_money = 5000
    elif deg <= 85:
        limit_money = 10000
    elif deg <= 100:
        limit_money = 50000
    else:
        print("[ERROR] Dial Module ERROR !")
    
    return limit_money

# Speacker Module Happy Sound
def happy_tune(speaker_module):
    ###########################################
    speaker_module.tune = Table.SCALE_TABLE['TI5'], 100
    time.sleep(0.1)
    speaker_module.turn_off()
    time.sleep(0.001)
    speaker_module.tune = Table.SCALE_TABLE['TI5'], 100
    time.sleep(0.1)
    speaker_module.turn_off()
    time.sleep(0.001)
    
    speaker_module.tune = Table.SCALE_TABLE['RE#6'], 100
    time.sleep(0.1)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['FA#6'], 100
    time.sleep(0.2)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['RE#6'], 100
    time.sleep(0.1)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['FA#6'], 100
    time.sleep(0.4)
    speaker_module.turn_off()
    time.sleep(0.001)

    ###########################################
    speaker_module.tune = Table.SCALE_TABLE['DO#6'], 100
    time.sleep(0.1)
    speaker_module.turn_off()
    time.sleep(0.001)
    speaker_module.tune = Table.SCALE_TABLE['DO#6'], 100
    time.sleep(0.1)
    speaker_module.turn_off()
    time.sleep(0.001)
    
    speaker_module.tune = Table.SCALE_TABLE['FA6'], 100
    time.sleep(0.1)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['SOL#6'], 100
    time.sleep(0.2)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['FA6'], 100
    time.sleep(0.1)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['SOL#6'], 100
    time.sleep(0.4)
    speaker_module.turn_off()
    time.sleep(0.001)

# Speacker Module Sad Sound
def sad_tune(speaker_module):
    speaker_module.tune = Table.SCALE_TABLE['FA#6'], 100
    time.sleep(0.4)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['FA6'], 100
    time.sleep(0.4)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['MI6'], 100
    time.sleep(0.4)
    speaker_module.turn_off()
    time.sleep(0.001)

    speaker_module.tune = Table.SCALE_TABLE['RE#6'], 100
    time.sleep(1)
    speaker_module.turn_off()
    time.sleep(0.001)
