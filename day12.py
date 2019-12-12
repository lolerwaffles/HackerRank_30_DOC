class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores=[]):
        super().__init__(firstName,lastName,idNumber)
        self.scores = scores
    def meanScores(self):
        return sum(self.scores)/len(self.scores)
    def calculate(self):
        if self.meanScores() >= 90:
            return "O"
        elif self.meanScores() >= 80 and self.meanScores() < 90:
            return "E"
        elif self.meanScores() >= 70 and self.meanScores() < 80:
            return "A"
        elif self.meanScores() >= 55 and self.meanScores() < 70:
            return "P"
        elif self.meanScores() >= 40 and self.meanScores() < 55:
            return "D"
        else:
            return "T"                                    
    


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
