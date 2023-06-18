from imports import *

def get_limit_money(self, dial_module):
    deg = dial_module.degree
    print(deg)
    
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
        print("Something gone wrong with the dial")
    
    return limit_money

def happy_tune(self, speaker_module):
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

def sad_tune(self, speaker_module):
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
