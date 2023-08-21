#! /usr/bin/python3 

# Harbor Higginbotham
# Time Assesment: 3 Hours
# Difficulty: Easy
# Date Started: 07/26/2023 @ 6pm 

import sys 
import subprocess 
import pkg_resources 
from prettytable import PrettyTable 
from Objects import *

def File_IO():
	# Var Dec:
	FILE = "./players.txt"
	Obj = LineUp()

	# Open File and read lines into LineUp Object. 
	with open(FILE, "r") as Stream:
		for Line in Stream:
			Ray = Line.split(",")
			Obj.Add(Ray[0], Ray[1], Ray[2], int(Ray[3]), int(Ray[4]))

	return Obj


def Pretty(List):
	# Var Dec:
	Table = PrettyTable(["", "Player", "Pos", "AB", "H", "AVG"]) # Create Header

	# Add Rows:
	for x in List:
		Table.add_row(x)

	# Console Output:
	print(Table)

def main():
	# Var Dec:
	Loop = True
	PlayerList = File_IO()

	print("+"*64)
	print("\t    [&] Baseball Team Management Program [&] ")
	print("+"*64)
	
	while(Loop):
		# Menue: 
		print("""
MENU OPTIONS
[&] 1 – Display lineup
[&] 2 – Add player
[&] 3 – Remove player
[&] 4 – Move player
[&] 5 – Edit player position
[&] 6 – Edit player stats
[&] 7 - Exit program

POSITIONS
[&] C, 1B, 2B, 3B, SS, LF, CF, RF, P [&]""")

		# User Input:
		try:
			User_Input = int(input("\n[&] Menu Option: "))

		except ValueError as Err:
			print("+"*64)
			print(f"[&] Input Failed - Invalid Option: {User_Input} \n[&] Error: {Err}")

		else:
			# Menu Options Function Call:
			if User_Input == 1: # Display - Should be off with those tabs I counted them at 4 spaces but it was way more. 
				Pretty(PlayerList)

			elif User_Input == 2: # Add Player
				# Header
				print("Valid positions - [&] C, 1B, 2B, 3B, SS, LF, CF, RF, P [&]\n[!]No check so... Get it right...\n")

				# User Input:
				PlayerList.Add(str(input("[$] First Name: ")), str(input("[%] Last Name: ")), str(input("[#] Position: ")), int(input("[^] Bats: ")), int(input("[@] Hits: ")))
				print("[&] Player Successfully added!")

			elif User_Input == 3: # Remove Player 
				# Header
				print(f"Player Range 1 - {len(PlayerList._LineUp__Player_List)}\n[!]No check so... Get it right...\n")

				# User Input:
				PlayerList.Remove(int(input("[*] Enter A Player Number: ")))
				print("[&] Player Successfully removed!")


			elif User_Input == 4: # Move Player 
				# Header
				print(f"Player Range 1 - {len(PlayerList._LineUp__Player_List)}\n[!]No check so... Get it right...\n")

				# User Input:
				PlayerList.Move(int(str(input('[*] Enter A Player Number: '))), int(str(input("[#] Position To Move To:"))))
				print("[&] Player Successfully moved!")

			elif User_Input == 5:# Edit Position 
				# Header
				print(f"Player Range 1 - {len(PlayerList._LineUp__Player_List)}\n[!]No check so... Get it right...\n")
				print("Valid positions - [&] C, 1B, 2B, 3B, SS, LF, CF, RF, P [&]\n[!]No check so... Get it right...\n")

				# User Input:
				PlayerList.Edit_Pos(int(input("[*] Enter A Player Number: ")), str(input("[#] Position: ")))
				print("[&] Player Position Successfully Changed!")

			elif User_Input == 6: # Edit Stats 
				# Header
				print(f"Player Range 1 - {len(PlayerList._LineUp__Player_List)}\n[!]No check so... Get it right...\n")

				# User Input:
				PlayerList.Edit_Stats(int(str(input("[*] Enter A Player Number: "))), int(str(input("[^] Bats: "))), int(str(input("[@] Hits: "))))
				print("[&] Player Stats Successfully Changed!")

			elif User_Input == 7: # Exit
				print("[!] Bye")
				Loop = False

			else:
				print(f"User Input Invalid: {User_Input}")

if __name__ == '__main__':
	# Check for Required Modules and ask if user wants to install... 
	# Source - https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t
	# Man I miss bash.... 

	# Var Dec
	Reqs = {"prettytable"}
	Installed_Mods = {pkg.key for pkg in pkg_resources.working_set} 
	Missing = Reqs - Installed_Mods # ooooo Fuck a linear search!

	if Missing: # Whoa very pythonic 
		try:
			Uin = str(input(f"[&] Missing Packages {Missing}\n[&] Would you like to install? [y/n] "))
		except ValueError as Err:
			print(f"[&] Input Failed - Invalid Option: {User_Input} \n[&] Error: {Err}")
		else:
			if Uin == "y" or Uin == "Y":
				subprocess.check_call([python, '-m', 'pip', 'install', *Missing], stdout=subprocess.DEVNULL)
				print(f"[&] {Missing} Installed... Re-feed interpreter")
			else:
				print("Manualy run 'python3 -m pip install prettytable'")
				print("yOu CaNt DoC pOiNtS If I gAvE aN OpTiOn?\nidk man the project needed some spice sorry")

	else:
		main()