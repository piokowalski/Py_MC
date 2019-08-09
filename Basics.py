m = 1
n = 2

sum1 = m+n
print(sum1)

## lists

student_grades = [2.2, 4.0, 3.8, 5.0]

mySum = sum(student_grades)
myLength = len(student_grades)

myMean = mySum / myLength
print(myMean)

##dictionary

students_grades = {"John": 4.0, "Zdzisia": 4.6, "Karen": 3.5, "Jack": 2.6}

myDictionarySum = sum(students_grades.values())
myDictionaryLen = len(students_grades)
myDictionaryMean = myDictionarySum / myDictionaryLen
print(myDictionaryMean)