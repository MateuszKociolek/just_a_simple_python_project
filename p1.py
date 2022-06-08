import pyautogui
import time
import math

def kwadrat(x, y):
    for _ in range(10):
        pyautogui.click(x, y)
        x += 10
        print(pyautogui.position())
    for _ in range(10):
        pyautogui.click(x, y)
        y += 10
    for _ in range(10):
        pyautogui.click(x, y)
        x -= 10
        print(pyautogui.position())
    for _ in range(10):
        pyautogui.click(x, y)
        y -= 10

def prostokat(x, y, w, h):
    for _ in range(w):
        pyautogui.click(x, y)
        x += 10
        print(pyautogui.position())
    for _ in range(h):
        pyautogui.click(x, y)
        y += 10
    for _ in range(w):
        pyautogui.click(x, y)
        x -= 10
        print(pyautogui.position())
    for _ in range(h):
        pyautogui.click(x, y)
        y -= 10


def kolo(R):
    (x,y) = pyautogui.size()
    (X,Y) = pyautogui.position(x/2,y/2)
    pyautogui.moveTo(X+R,Y)

    for i in range(360):
        if i%6==0:
            pyautogui.click(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))

time.sleep(5)


prostokat(600, 600, 13, 7)
kwadrat(300,300)
kolo(100)
