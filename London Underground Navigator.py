#Jake Eaton

import time
import typing
import sys

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
time.sleep(1)

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
print("Downloading Required Files...")
print("")
for i in range(101):
    time.sleep(0.0005)
    update_progress(i/100)

print ("")
print ("Files Downloaded")

print ("")
print("Installing Libraries, Files and Software Environments...")
print("")
for i in range(101):
    time.sleep(0.001)
    update_progress(i/100)

print ("")
print ("Install Complete")

print ("")
print("Cleaning all Junk Files")
print("")
for i in range(101):
    time.sleep(0.003)
    update_progress(i/100)

print("")
print("Clean Up Complete")

print("")
print("Finalising Installation")
print("")
for i in range(101):
    time.sleep(0.001)
    update_progress(i/100)

print ("")
print ("Activating Holo Version 4.7")
print("")
for i in range(101):
    time.sleep(0.01)
    update_progress(i/100)

print ("")
print("Artificial Intelligence activated...\n")

print("Preparing to engage Holo...\n")

print ("")
print("Engaging Neural Link... ")
print("")
for i in range(101):
    time.sleep(0.05)
    update_progress(i/100)

print ("")
print ("AI Successfully Activated")

print("Forming sOS...\n")

print ("")
print("Collecting Files... ")
print("")
for i in range(101):
    time.sleep(0.01)
    update_progress(i/100)

print ("")
print ("Files Collected")

print("Organising sOS...\n")

print ("")
print("Organising Files, Libraries and Software Environments... ")
print("")
for i in range(101):
    time.sleep(0.0005)
    update_progress(i/100)

print ("")
print ("Complete\n")

print("Starting Firmware, Utility and Application Software...\n")

print ("")
print("Firmware... ")
print("")
for i in range(101):
    time.sleep(0.0005)
    update_progress(i/100)

print ("")
print("Utility Software... ")
print("")
for i in range(101):
    time.sleep(0.0005)
    update_progress(i/100)

print ("")
print("Application Software... ")
print("")
for i in range(101):
    time.sleep(0.0005)
    update_progress(i/100)

print ("Loaded\n")
time.sleep(2)
type("Connecting AI via Neural Link...\n")
time.sleep(1)
type("Connection Successful...\n")
time.sleep(1)
type("Data transfer at maximum bandwidth...\n")
time.sleep(1)
type("Maximum speeds achieved...\n")
time.sleep(1)

print ("")
type("Loading AI...\n")
print("")
for i in range(101):
    time.sleep(0.01)
    update_progress(i/100)

print ("")
print("Launching Holo\n")
time.sleep(1)
type("Finding and opening London Underground Navigation System\n")
time.sleep(1)

def Main():

    stations = [["Edgware Road"], ["Marylebone"], ["Baker Street"], ["Euston"], ["Old Street"], ["Warren Street"], ["Farringdon"], ["Moorgate"], ["Liverpool Street"], ["Bond Street"], ["Oxford Street"], ["Tottenham Court Road"], ["Holborn"], ["Piccadilly Circus"], ["Leicester Square"], ["Bank"], ["Monument"], ["South Kensington"], ["Victoria"], ["Westminster"], ["Embankment"], ["Cannon Street"], ["London Bridge"]]
    brown_stations = [["Marylebone"],]



Main()
