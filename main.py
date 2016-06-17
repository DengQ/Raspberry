# !/usr/bin/env python
import os
import sys
import threading
from PyQt4.QtGui import *
import io
import socket
import struct
from PIL import Image

from RaspInterface.CameraInterface.CameraInterface import CameraInterface
#from igtCommunicationStack.igtCommunicationStack import CommunicationStack
from igtDataware.igtDataware import DataWare

if __name__ == "__main__":
    #comStack = CommunicationStack()

    data_ware = DataWare()

    cameraInterface = CameraInterface(data_ware)
    cameraInterface.launch()

    #data_ware.display()
    #data_ware.save()
