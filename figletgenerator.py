#!/bin/pyhton3

from os import system
from datetime import datetime as dt
import time


def sistema():

	white = '\033[1;37;40'
	magenta = '\033[1;35;40'
	
	
	def banner():
		print("*"*80)
		print('''		
	
 _____ _       _      _      ____                           _             
|  ___(_) __ _| | ___| |_   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |_  | |/ _` | |/ _ \ __| | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  _| | | (_| | |  __/ |_  | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
|_|   |_|\__, |_|\___|\__|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
         |___/                       
                                           
''')
		print("*"*80)
		print('\n','\n')
		
		
	def clear():
		_ = system('clear')

	def figlet(text):
		_ = system('figlet '+text)
	
	def cont():
		conti=input('''Do you want to create another figlet?
> ''')
		if conti == 'YES':
			print('\n')
			print('Restarting...')
			time.sleep(1.5)
			sistema()		
		elif conti == 'NO':
			clear()
			print('Turning off the system')
			time.sleep(2)		
			clear()
		else:
			print('Please chose a valid option!')
			print('YES  |   NO')
			cont()
	clear()
	banner()
	text = input('''Write your text here:
> ''')
	figlet(text)
	cont()


sistema()
