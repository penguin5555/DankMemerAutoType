#Grind commands(beg, fish, hunt, dig, search, crime, trivia)

import pyautogui as gui
import time as t

def gotobox():
    if gui.size() == (2560, 1440):
        gui.moveTo(806, 1339, duration=0)
    else:
        gui.moveTo(1060, 1722, duration=0)
    gui.click()

def command(name):
    gotobox()
    gui.typewrite(f"/{name}")
    t.sleep(1)
    gui.typewrite(["enter"])
    gui.typewrite(["enter"])

def search_crime():
    t.sleep(1)
    command("search")
    t.sleep(2.75)
    if gui.size() == (2560, 1440):
        gui.moveRel(-140, -70)
    else:
        gui.moveRel(-100, -130)
    for i in range(2):
        gui.click()
        gui.moveRel(15,0)
        gui.click()
        gui.moveRel(-30,0)
        gui.click()
        gui.moveRel(15,0)
    t.sleep(0.2)
    command("crime")
    t.sleep(2.75)
    if gui.size() == (2560, 1440):
        gui.moveRel(-140, -70)
    else:
        gui.moveRel(-100, -130)
    t.sleep(1)
    for i in range(2):
        gui.click()
        gui.moveRel(15,0)
        gui.click()
        gui.moveRel(-30,0)
        gui.click()
        gui.moveRel(15,0)
    t.sleep(0.2)

def trivia():
    t.sleep(1)
    command("trivia")
    if gui.size() == (2560, 1440):
        gui.moveRel(-140, -70)
    else:
        gui.moveRel(-100, -130)
    t.sleep(1)
    for i in range(2):
        gui.click()
        gui.moveRel(15,0)
        gui.click()
        gui.moveRel(-30,0)
        gui.click()
        gui.moveRel(15,0)
    t.sleep(0.2)

t.sleep(0.5)
gotobox()
t.sleep(2)
while True:
    command("beg")
    t.sleep(0.2)
    command("fish")
    t.sleep(0.2)
    command("hunt")
    t.sleep(0.2)
    command("dig")
    t.sleep(0.2)
    search_crime()
    t.sleep(0.2)
    trivia()
    for i in range(45):
        t.sleep(1)
        print(i)

