#! /usr/bin/python3 

import sqlite3 
from contextlib import closing

class DB_Player:

	# Default Constructor:
	def __init__(self):
		self.__Conn = sqlite3.connect("./player_db.sqlite") # Connect to database
		self.__Index = 0

	# Iterator Creation:
	def __iter__(self):
		return self

	def __next__(self): # Used as a general itterator for my print to table function. 

		if self.__Index < self.Size():
			Output = self.View()

			Temp = [Output[self.__Index][1], Output[self.__Index][2] + " " + Output[self.__Index][3], Output[self.__Index][4], Output[self.__Index][5], Output[self.__Index][6], round(int(Output[self.__Index][6])/int(Output[self.__Index][5]), 3)]

			self.__Index += 1 

			# Return all Varibales. 
			return Temp
		else:
			self.__Index = 0
			raise StopIteration
	
	# Used to Sanitize Input of DB Entries just for kicks! Gonna throw sqlmap at it some time soon!  
	def Sanitize(self, Input): 
		return Input.replace("'", "''").replace("#", "").replace("-", "")
	

	# Used to execute db queries that have user input and them commit to DB if exec is successful!
	def Exec_Check(self, Obj, Query):
		# try: # Execute query
		Obj.execute(Query)

		# except sqlite3.Error: # Query Failed
		#	print("[!] ERROR, Input Not Found in DB")

		# else: # Commit if successful. 
		#	self.__Conn.commit()


	# Query DB to get full list size to maintain entry order. 
	def Size(self):
		with closing(self.__Conn.cursor()) as ection:
			# Query:
			ection.execute("SELECT * FROM Player")

			# Return List:
			return len(ection.fetchall())

	# View All Players:
	def View(self):
		with closing(self.__Conn.cursor()) as ection:
			# Query:
			ection.execute("SELECT * FROM Player")

			# Return List to Pretty Table! 
			return ection.fetchall()

	# Adds Players to DB:
	def Add(self, First, Last, Pos, Bats, Hits):
		
		with closing(self.__Conn.cursor()) as ection:
			# Query:
			self.Exec_Check(ection ,f'''INSERT INTO Player (playerID, batOrder, firstName, lastName, position, atBats, hits) VALUES ({self.Size()+1}, {self.Size()+1}, {self.Sanitize(First)}, {self.Sanitize(Last)}, "{self.Sanitize(Pos)}", {self.Sanitize(Bats)}, {self.Sanitize(Hits)})''')

				
		
	# Edit Player Bats and Hits: 
	def Edit_Stats(self, Order, Bats, Hits):
		with closing(self.__Conn.cursor()) as ection:
			# Query:
			self.Exec_Check(ection ,f'''UPDATE Player 
				SET (atBats = {self.Sanitize(Bats)}, hits = {self.Sanitize(Hits)})
				WHERE batOrder = {self.Sanitize(Order)}''')


	# Edit Player Bats and Hits: 
	def Edit_Pos(self, Order, Pos):
		# Variable Dec:
		Valid = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
		Check = False
		Exec_Check = True

		# Input Sanitize:
		for Position in Valid:
			if Position == Pos:
				Check = True
				break

		if Check:
			with closing(self.__Conn.cursor()) as ection:
				# Query:
				self.Exec_Check(ection ,f'''UPDATE Player 
					SET position = {self.Sanitize(Pos)}
					WHERE batOrder = {self.Sanitize(Order)}''')
		else:
			print(f"[!] Position Input Invalid - {Pos}")
	
	# Move Player Position In DB Aboud. 
	def Move(self, Current_Order, New_Order):
		with closing(self.__Conn.cursor()) as ection:
			# Current Row:
			self.Exec_Check(ection ,f'''SELECT * FROM Player WHERE batOrder = {self.Sanitize(Current_Order)}''')
			Row_Current = ection.fetchone()

			# New Row:
			self.Exec_Check(ection ,f'''SELECT * FROM Player WHERE batOrder = {self.Sanitize(New_Order)}''')
			Row_New = ection.fetchone() 

			# Swap:
			Row_Current_Upate = (Row_New[0], Row_New[1], Row_New[2], Row_New[3], Row_New[4], Row_New[5], Row_New[6])
			Row_New_Update = (Row_Current[0], Row_Current[1], Row_Current[2], Row_Current[3], Row_Current[4], Row_Current[5], Row_Current[6])

			# Execute Swap:
			ection.execute(f'''UPDATE Player SET playerID = ?, batOrder = ?, firstName = ?, lastName = ?, position = ?, atBats = ?, hits = ? WHERE batOrder = {self.Sanitize(Current_Order)}''', Row_Current_Upate)
			ection.execute(f'''UPDATE Player SET playerID = ?, batOrder = ?, firstName = ?, lastName = ?, position = ?, atBats = ?, hits = ? WHERE batOrder = {self.Sanitize(New_Order)}''', Row_New_Update)
			
		
	# Deletes Player based on order number: 
	def Remove(self, Order):
		with closing(self.__Conn.cursor()) as ection:
			# Query:
			self.Exec_Check(ection ,f'''DELETE FROM Player WHERE batOrder = {self.Sanitize(Order)}''')


