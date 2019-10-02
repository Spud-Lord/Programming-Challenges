#Jake Eaton
#Logic Gate Calculator

import time
import sys
import typing

def type(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.08)

print("Copyright Spud-Lord Technologies 2016-2020 ©\n")
time.sleep(0.5)
type("Welcome Agent Starch\n")
time.sleep(2)
type("Boot-up Sequence Initiated...\n")
time.sleep(2)

def update_progress(progress):
    barLength = 25
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

print ("")
type("Downloading Required Files...")
print("")
for i in range(101):
    time.sleep(0.075)
    update_progress(i/100)

print ("")
print ("Files Downloaded")
time.sleep(2)
print ("")
type("Installing Libraries, Files and Software Environments...")
print("")
for i in range(101):
    time.sleep(0.01)
    update_progress(i/100)
print ("")
print ("Install Complete")
time.sleep(2)
print ("")
type("Cleaning all Junk Files")
print("")
for i in range(101):
    time.sleep(0.03)
    update_progress(i/100)
print ("")
print ("Clean Up Complete")
time.sleep(2)
print ("")
type("Finalising Installation")
print("")
for i in range(101):
    time.sleep(0.0001)
    update_progress(i/100)
print ("")
print ("Final Checks Complete")
time.sleep(2)
print ("")
type ("Activating Holo Version 4.5")
print("")
for i in range(101):
    time.sleep(0.1)
    update_progress(i/100)
print ("")
type("Artificial Intelligence activated...\n")
type("Preparing to engage Holo...\n")
time.sleep(2)
print ("")
type("Engaging Neural Link... ")
print("")
for i in range(101):
    time.sleep(0.175)
    update_progress(i/100)
print ("")
print ("AI Successfully Connected via Neural Link")
time.sleep(2)
print ("")
type("Loading AI")
print("")
for i in range(101):
    time.sleep(0.075)
    update_progress(i/100)
print ("")
type("Launching Holo\n")
time.sleep(2)
type("Finding and opening Logic Gate Calculator\n")
print("")

choice = input("What Logic Gate would you like to use? AND, OR or XOR? ")

if choice == ("AND"):
    ins = int(input("How many inputs are there? "))
    for i in range (0, ins):
        enter = int(input("Please enter your input "))
        if enter == ("1"):
            print("Your output is 1")
            time.sleep(2)

        if enter == ("0"):
            print("Your output is 0")
            time.sleep(2)

if choice == ("OR"):
    ins = int(input("How many inputs are there? "))

if choice == ("XOR"):
    ins = int(input("How many inputs are there? "))
