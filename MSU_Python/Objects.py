#! /usr/bin/python3


class Player:
	def __init__(self, First, Last, Pos, AB, H): # Default Constructor
		self.__First = First
		self.__Last = Last
		self.__Position = Pos
		self.__At_Bats = AB
		self.__Hits = H

	# Return Full Name:	
	def Fullname(self):
		return f"{self.__First} {self.__Last}"

	# Returns Player Average:
	def Average(self):
		return round(float(self.__Hits/self.__At_Bats), 3)


class LineUp():
	def __init__(self): # Default Constructor
		self.__Player_List = []
		self.__Index = 0

	# Iterator Creation:
	def __iter__(self):
		return self

	def __next__(self): # Used as a general itterator for my print to table function. 
		if self.__Index < len(self.__Player_List):
			self.__Index += 1 # Add for next itteration, kinda fuckes me on the return but hey thats okay. 

			# Return all Varibales. 
			return [self.__Index, self.__Player_List[self.__Index-1].Fullname(), self.__Player_List[self.__Index-1]._Player__Position, self.__Player_List[self.__Index-1]._Player__At_Bats, self.__Player_List[self.__Index-1]._Player__Hits, self.__Player_List[self.__Index-1].Average()]
			# self.__Player_List[self.__Index-1].__Position, self.__Player_List[self.__Index-1].__At_Bats, self.__Player_List[self.__Index-1].__Hits, self.__Player_List[self.__Index-1].Average()

		else:
			self.__Index = 0
			raise StopIteration

	# Add a Player
	def Add(self, First, Last, Pos, AB, H):
		self.__Player_List.append(Player(First, Last, Pos, AB, H))

	# Remove A Player
	def Remove(self, LineUpNum):
		self.__Player_List.pop(LineUpNum-1)
	
	# Print a Single Player
	def Get(self, LineUpNum): # Lol I dont even use this... 
		return self.__Player_List[LineUpNum-1]

	# Move a Player: 
	def Move(self, Newindex, Oldindex):
		self.__Player_List.insert(Oldindex-1, self.__Player_List.pop(Newindex-1))

	# Edit Player Position
	def Edit_Pos(self, LineUpNum, Pos):
		self.__Player_List[LineUpNum-1]._Player__Position = Pos

	# Edit Player Stats 
	def Edit_Stats(self, LineUpNum, Bats, Hits):
		self.__Player_List[LineUpNum-1]._Player__At_Bats = Bats
		self.__Player_List[LineUpNum-1]._Player__Hits = Hits








