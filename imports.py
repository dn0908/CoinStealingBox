import serial
import time

from video_coin_count import get_money_value_index_manual

import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder

import modi

import modi_control as MODI

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