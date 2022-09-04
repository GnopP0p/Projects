import pyautogui
from PIL import ImageGrab, ImageOps
import time
from numpy import *

class cord():
    repBtn = (340,420)
    trex = (171,420)

def restartG():
    pyautogui.click(cord.repBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.03)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (cord.trex[0]+60,cord.trex[1],
           cord.trex[0]+100,cord.trex[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return(a.sum())

def main():
    restartG()
    while True:
        if(imageGrab()!=1447):
            pressSpace()
            time.sleep(0.1)
main()
    
