# Lab 5
# Daim Bin Khalid
# 251686775

class Classroom:

	totalstudents = 0

	def __init__(self, classID, studnum, namelist):
		self.classID = classID
		self.studnum = studnum
		self.namelist = namelist
		Classroom.totalstudents += studnum

	def StudentAdded(self, name):
		Classroom.totalstudents += 1
		self.studnum += 1
		self.namelist.append(name)

	def getStudentCount(self):
		return self.studnum

	def DisplayClassroom(self):
		print(*self.namelist, sep = ', ')

	def getTotalStudentCount(self):
		return Classroom.totalstudents

def main():
	Physics = Classroom(101, 3, ['Daim', 'Maulana Hafash Jalaludeen', 'Manal'])
	Physics.StudentAdded('Momi')
	Physics.DisplayClassroom()
	print(Physics.getStudentCount())
	print(Physics.getTotalStudentCount())

	print()

	Maths = Classroom(111, 3, ['Arbab', 'Maulana Hafash Jalaludeen', 'Badshah Kiran'])
	Maths.StudentAdded('Julia')
	Maths.DisplayClassroom()
	print(Maths.getStudentCount())
	print(Maths.getTotalStudentCount())

	print()

	Computer = Classroom(102, 3, ['Hitler', 'Maulana Hafash Jalaludeen', 'Stalin'])
	Computer.StudentAdded('Genghis Khan')
	Computer.DisplayClassroom()
	print(Computer.getStudentCount())
	print(Computer.getTotalStudentCount())

main()