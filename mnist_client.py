import pyb, time
import sensor, image, time, math, ustruct
import os, tf


# Startup sequence


#net = tf.load('/mnist_A.tflite')
labels = ["zero","one","two","three","four","five","six","seven","eight","nine"]
#print("start")
led = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
led4 = pyb.LED(4)

led.off()
led2.off()
led3.off()
led4.off()
usb = pyb.USB_VCP()
#print("start2")
while (usb.isconnected()==False):
   #print("not connected")
   led.on()
   time.sleep_ms(150)
   led.off()
   time.sleep_ms(100)
   led.on()
   time.sleep_ms(150)
   led.off()
   time.sleep_ms(600)

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QQVGA for april tags
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
# AprilTags Test Measurements
#print("connected")
led.off()
led2.off()
led3.off()
led4.off()

sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
clock = time.clock()

while(True):
    clock.tick()
    cmd = usb.recv(4, timeout=500)
    img = sensor.snapshot()
    #out = net.classify(img.copy().binary([(0, 1)], invert=True))
    out = tf.classify('/mnist_E.tflite', img.copy().binary([(0, 1)], invert=True))
    for obj in out:
        # This combines the labels and confidence values into a list of tuples
        # and then sorts that list by the confidence values.
        sorted_list = sorted(zip(labels, obj.output()), key = lambda x: x[1], reverse = True)
        #print("%s = %f" % (sorted_list[0][0], sorted_list[0][1]))

    #print(clock.fps(), "fps")
    #print(int(clock.fps()))

    if (cmd == b'snap'):
        #print("snap")
        img = sensor.snapshot().compress()
        usb.send(ustruct.pack("<L", img.size()))
        usb.send(img)

    if (cmd == b'test'):
        #print("test")
        led2.on()
        time.sleep_ms(150)
        led2.off()
        ans = 7932
        usb.send(ustruct.pack("<L", ans))

    if (cmd == b'fpsr'):
        ans = int(clock.fps())
        usb.send(ustruct.pack("<L", ans))
