# fedml
A Federated Learning Repository


## What is FedML?
FedML, or Federated Learning, is a machine learning method that trains an algorithm in a decentralized manner across many "edge devices," without the need to exchange the actual data samples. 

Visit the [fedml Wiki Page](https://github.com/lucastliu/fedml/wiki) to learn more about FedML, Tensorflow, the H7 Camera, and more!


## OpenMV

![cam](https://github.com/lucastliu/fedml/blob/main/media/cam.png)

"The OpenMV project is about creating low-cost, extensible, Python powered, machine vision modules and aims at becoming the "Arduino of Machine Vision" " - [OpenMV Homepage](https://openmv.io/)



### Devices

The following instructions have been tested using the `Cam H7` and the `Cam H7 Plus`

Host devices the workflow has been tested on include:

* Windows PC
* Windows PC running WSL2
* Raspberry Pi 3B+

### OpenMV IDE

The OpenMV IDE is perhaps the easiest way to get started. It comes with a lot of support and information for starting with their products, including example scripts, a serial monitor, and an integrated camera preview.

![openmvide](https://cdn.shopify.com/s/files/1/0803/9211/files/openmv-ide.gif?v=1480470511)

First, [Download the IDE](https://openmv.io/pages/download) onto your host device.

Second, simply connect your Cam H7 via USB to your host device, launch the IDE, and get started!

### Pure Data Communication

During production, you do not want to operate through an IDE. This repository includes example Python code for what to put on the H7 Camera, as well as what code to run on your host device in order to communicate via USB.

First, connect your `Cam H7` to your host device (such as a PC)

#### Client

Save your desired script as `main.py` on your `Cam H7` under the root directory. This can be achieved through the IDE, or through traditional methods of adding files to an external device connected to your computer.

This special file will be set to automatically run everytime the `Cam H7` is powered on.

Here is an [example file](https://github.com/lucastliu/fedml/blob/main/mnist_client.py). Remember to rename the file!


If you are running a prediction model, also make sure to save the model to the camera device as well. Our example file happens to use this [tflite model](https://github.com/lucastliu/fedml/blob/main/models/mnist_A.tflite)

More tflite mnist models are available in the `models` folder of this repository.

This example setup will run MNIST classification using the specified model, and is capable of reporting the FPS during this process.

Safely disconnect the camera device.

#### Host

Reconnect the camera to the host device.

After identifying the COM port that your camera is connected to, modify your host script [such as this example](https://github.com/lucastliu/fedml/blob/main/cam_host.py) to use the correct port.

Then simply run the python script.


### Troubleshooting

Some tips for troubleshooting:

* The IDE is a great way to debug and understand what is happening on the camera
* Ensure you have the right kind of port specified on the host device (this port may not be the same each time!)
* You may need to disconnect and re-connect the devices if you get into a bad state
* Make use of the color LED on the camera to help signal what state the camera is in - this is a great visual debugging tool!
* The [OpenMV Forums](https://github.com/lucastliu/fedml/blob/main/cam_host.py) can also be a useful resource






