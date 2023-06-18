from imports import *

class arduino_uno:
    port = "COM14"
    baudrate = 9600

class SerialWrapper():
    def __init__(self, device, timeout=1):
        # Open device communication
        try:
            self.device = serial.Serial(device.port, device.baudrate, timeout=1)
            time.sleep(1)
        except:
            print("[ERROR] Device can not be found or can not be configured.")

        # Flags
        self.init_flag : bool = False

        # Flush buffer
        self.device.reset_input_buffer()
        
        while(self.init_flag == False):
            line = self.read_line()
            print(line)
            if (line == "3.stop"):
                self.init_flag = True

    def read_line(self):
        if self.device.readable():
            line = self.device.readline().decode('utf-8').rstrip()

            return line      
    
    def send_flag(self, flag):
        self.device.write(flag.encode())

if __name__ == "__main__":
    device = SerialWrapper(arduino_uno)
    device.read_line()
