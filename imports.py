import serial
import time
import cv2
import numpy as np
import modi
from skimage import measure 
import modi_control
from arduino_connect import arduino_uno, SerialWrapper
from video_processing import Video

class Table:
    # Scale Table
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
