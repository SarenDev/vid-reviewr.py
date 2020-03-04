#!/bin/bash
clear
printf "Testing for VLC, Python, Pip and its imports"
sleep 1
clear
printf "? VLC\n"
printf "? Python\n"
printf "* ? Pip\n"
printf "** ? 'send2trash' Module\n"
if hash vlc 2>/dev/null; then
	clear
	printf "✓ VLC\n"
	printf "? Python\n"
	printf "* ? Pip\n"
	printf "** ? 'send2trash' Module\n"
	if hash python3 2>/dev/null; then
		clear
		printf "✓ VLC\n"
		printf "✓ Python\n"
		printf "* ? Pip\n"
		printf "** ? 'send2trash' Module\n"
		if hash pip3 2>/dev/null; then
			clear
			printf "✓ VLC\n"
			printf "✓ Python\n"
			printf "* ✓ Pip\n"
			printf "** ? 'send2trash' Module\n"
			if pip3 search send2trash | grep -q 'INSTALLED'; then
				clear
				printf "✓ VLC\n"
				printf "✓ Python\n"
				printf "* ✓ Pip\n"
				printf "** ✓ 'send2trash' Module\n"
				printf "Everything seems to be working, running script and closing this window in a bit"
				python3 vid-reviewr.py
				sleep 3
				exit
			else
				clear 
				printf "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
				printf "✓ VLC\n"
				printf "✓ Python\n"
				printf "* ✓ Pip\n"
				printf "** X 'send2trash' Module\n"
				printf "Something went wrong when testing for the 'Send2Trash' module. It's possible you're missing it\n"
				printf "Please install it using 'pip install send2trash' and run the script again\n"
				printf "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
				read -n 1 -r -s -p "Press any key to continue..."
				printf "\n"
				exit
			fi
		else
			clear 
			printf "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
			printf "✓ VLC\n"
			printf "✓ Python\n"
			printf "* X Pip\n"
			printf "** ? 'send2trash' Module\n"
			printf "Something went wrong when testing for Pip, please check your Python 3 installation\n"
			printf "If you don't have it installed try using 'sudo apt install python3-pip\n"
			printf "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
			read -n 1 -r -s -p "Press any key to continue..."
			printf "\n"
			exit
			fi
	else
		clear 
		printf "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
		printf "✓ VLC\n"
		printf "X Python\n"
		printf "* ? Pip\n"
		printf "** ? 'send2trash' Module\n"
		printf "Something went wrong when testing for Python 3, please make sure it's installed and works from terminal\n"
		printf "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
		read -n 1 -r -s -p "Press any key to continue..."
		printf "\n"
		exit
	fi
else
	clear 
	printf "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
	printf "X VLC\n"
	printf "? Python\n"
	printf "* ? Pip\n"
	printf "** ? 'send2trash' Module\n"
	printf "Something went wrong when testing for VLC, please make sure it's installed and works from terminal\n"
	printf "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
	read -n 1 -r -s -p "Press any key to continue..."
	printf "\n"
	exit
fi
