
#  _|_|_|                            _|_|                        _|            _|_|    _|                  _|                    _|      
#  _|    _|    _|_|    _|  _|_|    _|        _|_|      _|_|_|  _|_|_|_|      _|    _|      _|_|_|  _|_|    _|_|_|      _|_|    _|_|_|_|  
#  _|_|_|    _|_|_|_|  _|_|      _|_|_|_|  _|_|_|_|  _|          _|          _|_|_|_|  _|  _|    _|    _|  _|    _|  _|    _|    _|      
#  _|        _|        _|          _|      _|        _|          _|          _|    _|  _|  _|    _|    _|  _|    _|  _|    _|    _|      
#  _|          _|_|_|  _|          _|        _|_|_|    _|_|_|      _|_|      _|    _|  _|  _|    _|    _|  _|_|_|      _|_|        _|_|                                                                                                                                                                                                                                                                        
# Wayne Kenney (Pythogen) - 4/27/2018 - [This Software is Private]

#                                 ,----.___________,-,
#         ,__                    (________________|__|
#      __/()(_________________________/o(____)o(__  ``            _
#     (__________________________(_(_(_(_(________Y_....-----====//
#                   ( , , , , , , (______________)--            ((
#                    \_____________|________|[ )) JW  ____   __  \\
#                                   |____|    "" \.__-'`". \(__) \\\
#                                   |____|        `""      ```"""=,))
#                                   |    |
#                                    ====

# Configured to GunZ 2

# This aimbot automatically locks onto enemies by detecting pixel color locations 
# and automatically positioning your mouse. This script will continuously capture 
# desktop screeshots and scan those screenshots immediately after. If the target's
# pixel color is found, then the aimbot will calculate the screen coordinates and
# finally position your mouse directly over the target.

# 1) Set enemy color(s) in variable(s)
# 2) Configure 'Screen Capture/Target Detection' Box Parameters
# 4) Configure Conditions in the Mouse Movement/Positioning Algorithm
# 3) Run Aimbot and be unstoppable

print """
  _____         ___         _      _____ _       _       _     
 |  _  |___ ___|  _|___ ___| |_   |  _  |_|_____| |_ ___| |_   
 |   __| -_|  _|  _| -_|  _|  _|  |     | |     | . | . |  _|  
 |__|  |___|_| |_| |___|___|_|    |__|__|_|_|_|_|___|___|_|                                                             
 Coded by Pythogen (Wayne Kenney) - 4/27/2018 - [Private Edition]
 		   -= GunZ 2 (Undetectable) =-
"""

from PIL import Image
import pyautogui
from time import sleep
import time
import sys
import win32gui, win32api, win32con, ctypes

# Enemy Color for Aimbot
#color = (255, 0, 0)
color = (218, 33, 40)

# (Mouse Position / Monitor Resolution) Calculation Variables
xCord = 0
yCord = 0

# Default Box Template 640x360
Box = 640, 360, 640, 360

# Primary Function / Command Console
def main():

	while(True):
		cmd = raw_input(" Command>")
		cmd = cmd.lower()
		if cmd == "help":
			# List of Commands
			print """\nList of commands:\n  
	help - Displays a List of Commands
	info - Displays Aimbot Information
	aimbot.on - Activate the Aimbot
	shotbot.on - Activate the Shotbot
	resolution.setup - Monitor Resolution Settings
	exit - Exit this Script\n"""
		elif cmd == "aimbot.on":
			# Execute Aimbot
			Aimbot_GO()
		elif cmd == "exit":
			# Exit
			sys.exit()
		elif cmd == "shotbot.on":
			#Shotbot_GO()
			print "\n To be finished later...\n"
		elif cmd == "debug":
			debug_mode()
		elif cmd == "info":
			print """
   /$$$$$$                      /$$$$$$$$        /$$$$$$ 
  /$$__  $$                    |_____ $$        /$$__  $$
 | $$  \__/ /$$   /$$ /$$$$$$$      /$$/       |__/  \ $$
 | $$ /$$$$| $$  | $$| $$__  $$    /$$/          /$$$$$$/
 | $$|_  $$| $$  | $$| $$  \ $$   /$$/          /$$____/ 
 | $$  \ $$| $$  | $$| $$  | $$  /$$/          | $$      
 |  $$$$$$/|  $$$$$$/| $$  | $$ /$$$$$$$$      | $$$$$$$$
  \______/  \______/ |__/  |__/|________/      |________/ 

  Perfect Aimbot for GunZ 2:
  	- Auto-Aim Tool Designed using in-game enemy pixel color detection
  	- Unique logic that enables amazing speed and accuracy
  	- Configured for Headshots (Headshot probability 98%)
  	- Dominate in Death Match and Conquer in Campaign mode

  Enjoy!
 """
		else:
			print "\n Invalid command. (Type 'help' for list of commands)\n"

# Aimbot Function (Auto-Aim)
def Aimbot_GO():

	print "\n Aimbot Activated!\n"
	# Loop for process...
	while(True):

		x, y = win32api.GetCursorPos()

		# Debugging (1)
		#print "current pos: %s : %s\n" % (x,y)

		# Take screenshots (Full Screen)
		#pic = pyautogui.screenshot()
		 
		# # Take screenshots (640px Box)
		pic = pyautogui.screenshot(region=(Box)) 

		# Set list with screenshot pixel colors
		pix_val = list(pic.getdata())

		# Scan array >> Find enemy color
		# [x][x][x][x][x][x][x][x][x][x]
		# [x][x][x][x][x][x][ ][ ][ ][ ]
		# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
		# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]

		# If Target's Pixel Color Found in Screenshot, then...
		if color in pix_val:

			# Variables for Storing Pixel Color Location
			xCord = pix_val.index(color) / 640
			yCord = pix_val.index(color) % 640

			# Debugging (3)
			#print "pixel color pos: %s, %s" % (yCord, xCord)

			# Algorithm for Automatic Aiming
			if(yCord>310):
				z = (yCord - 310) / 2
				win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,z,0,0,0)
				#pass
			elif(yCord<310):
				z = (310 - yCord) / 2
				win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,-(z),0,0,0)
				#pass
			if(xCord>100):
				x = (xCord - 100) / 2
				win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,x,0,0)
				#pass
			elif(xCord<100):
				x = (100 - xCord) / 2
				win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,-(x),0,0)
				#pass
		else:
			# If No Targets are Visible...
			pass

def Shotbot_GO():
	try:
	    while True:
	        pixelColor = pyautogui.screenshot().getpixel((1025, 561))
	        time.sleep(0)
	        print " Shotbot Listening..."
	        if (str(pixelColor[0]).rjust(3) == "220" and str(pixelColor[1]).rjust(3) == " 12" and str(pixelColor[2]).rjust(3) == " 14"):
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
				sleep(0.05)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
				print " Shotbot Fire!"
	except KeyboardInterrupt:
	    print("\nDone...")

def print_no_newline(string):
	import sys
	sys.stdout.write("\r")
	sys.stdout.write(string)
	sys.stdout.flush()

# Auto-Click Function for Shotbot
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

# Debug option for setting up bot
def debug_mode():

	print "\n Debug Activated!\n"

	while(True):

		pic = pyautogui.screenshot(region=(Box))

		pix_val = list(pic.getdata())

		if color in pix_val:

			xCord = pix_val.index(color) / 640
			yCord = pix_val.index(color) % 640

			# Debugging (3)
			print "pixel color pos: %s, %s" % (yCord, xCord)

main()