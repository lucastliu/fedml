import sys
import serial
import struct
import time


class H7Camera():
    """
    OpenMV Cam H7 Host Device Side Camera Object

    WIP
    """
    def __init__(self, port_name="/dev/ttyS4"):
        self.port_name = port_name
        self.test = 0.0

    def cam_mand(self, serialcmd):
        sp = serial.Serial(self.port_name,
                           baudrate=115200,
                           bytesize=serial.EIGHTBITS,
                           parity=serial.PARITY_NONE,
                           xonxoff=False, rtscts=False,
                           stopbits=serial.STOPBITS_ONE,
                           timeout=None,
                           dsrdtr=True)
        try:
            sp.setDTR(True)  # dsrdtr is ignored on Windows.
            sp.write(serialcmd.encode())
            sp.flush()
            result = struct.unpack('<L', sp.read(4))[0]
            sp.close()
            return result

        except Exception as ex:
            print("Serial Communication Error")
            return -1

    def get_photo(self, name="img.jpg"):
        serialcmd = "snap"
        sp = serial.Serial(self.port_name,
                           baudrate=115200,
                           bytesize=serial.EIGHTBITS,
                           parity=serial.PARITY_NONE,
                           xonxoff=False, rtscts=False,
                           stopbits=serial.STOPBITS_ONE,
                           timeout=None,
                           dsrdtr=True)

        sp.setDTR(True)  # dsrdtr is ignored on Windows.
        sp.write(serialcmd.encode())
        sp.flush()
        size = struct.unpack('<L', sp.read(4))[0]
        img = sp.read(size)
        sp.close()

        with open(name, "wb") as f:
            f.write(img)

    def update_test(self):
        self.test = self.cam_mand("test")

    def get_fps(self):
        return self.cam_mand("fpsr")


def main():
    print("FPS Test")
    #v = H7Camera(port_name="COM5")
    # x = v.get_test()
    # print(x)
    sp = serial.Serial("COM5",
                       baudrate=115200,
                       bytesize=serial.EIGHTBITS,
                       parity=serial.PARITY_NONE,
                       xonxoff=False, rtscts=False,
                       stopbits=serial.STOPBITS_ONE,
                       timeout=None,
                       dsrdtr=True)
    sp.setDTR(True)  # dsrdtr is ignored on Windows.

    for x in range(100):
        sp.write("fpsr".encode())
        sp.flush()
        result = struct.unpack('<L', sp.read(4))[0]
        print(result)

    sp.close()

    print("done")


if __name__ == '__main__':
    main()
