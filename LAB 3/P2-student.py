"""
File: student.py
Resources to manage a student's name and test scores.
"""
import random
class Student(object):
    """Represents a student."""
 
    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
 
    def getName(self):
        """Returns the student's name."""
        return self.name
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score
 
    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    def __eq__(self, other):
        return self.name == other.name
 
    def __lt__(self, other):
        return self.name < other.name
 
    def __ge__(self, other):
        return self.name >= other.name
def main():
    s1 = Student("Marky", 1)
    s1.setScore(1, 95)
    s2 = Student("Xandre", 1)
    s2.setScore(1, 88)
    s3 = Student("Angel", 1)
    s3.setScore(1, 99)
    s4 = Student("SomeoneIDK", 1)
    s4.setScore(1, 89)
    s5 = Student("Crush", 1)
    s5.setScore(1, 98)
 
    students = [s1, s2, s3, s4, s5]
 
    random.shuffle(students)
 
    print("Shuffled Students' List:")
    for student in students:
        print(student)
 
    students.sort()
 
    print("\nSorted Students' List:")
    for student in students:
        print(student)
 
if __name__ == "__main__":
    main()
