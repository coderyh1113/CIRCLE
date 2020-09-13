import time
import os

def area(a):
    b = a * a
    c = "π"
    time.sleep(0.11111)
    print("")
    print("\033[31m" + str(b) + c)
    print("\033[37m" + "")
    input("press enter to continue...")
def circumference(a):
    b = 2 * a
    time.sleep(0.11111)
    print("")
    print("\033[31m" + str(b) + "π")
    print("\033[37m" + "")
    input("press enter to continue...")
def sarea(a, b):
    c = a * a
    d = b / 360
    e = c * d
    time.sleep(0.11111)
    print("")
    print("\033[31m" + str(e) + "π")
    print("\033[37m" + "")
    input("press enter to continue...")
def fcircumference(a, b):
    c = 2 * a
    d = b / 360
    e = c * d
    time.sleep(0.11111)
    print("")
    print("\033[31m" + str(e) + "π")
    print("\033[37m" + "")
    input("press enter to continue...")
def notany():
    time.sleep(0.11111)
    print("")
    print("\033[31m" + "choose again!")
    print("\033[37m" + "")
    input("press enter to continue...")

    
while True:
    os.system('cls')
    time.sleep(0.5)
    print("\033[31m" + "              ---------------------------------------")
    print("\033[31m" + "        ----                   C                      -----")
    print("\033[31m" + "    ----                       I                          ----")
    print("\033[31m" + "----                           R                             ----")
    print("\033[31m" + "----                           C                             ----")
    print("\033[31m" + "    ----                       L                           ----")
    print("\033[31m" + "       ----                    E                        ----")
    print("\033[31m" + "             -----------------------------------------")
    print("")
    print("\033[37m" + "[1] Circle area")
    print("[2] Circumference of a circle")
    print("[3] Sector form area")
    print("[4] Fan-shape circumference")
    ch = input("choose: ")
    if ch == "1":
        ban = float(input("Radius length: "))
        area(ban)
    elif ch == "2":
        ban = float(input("Radius length: "))
        circumference(ban)
    elif ch == "3":
        ban = float(input("Radius length: "))
        angle = float(input("Central angle: "))
        sarea(ban, angle)
    elif ch == "4":
        ban = float(input("Radius length: "))
        angle = float(input("Central angle: "))
        fcircumference(ban, angle)
    else:
        notany()
