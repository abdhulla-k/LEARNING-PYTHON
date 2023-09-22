import math

# 1. get an input and show it to user
inputNumber = input('Please enter an number: ')
print(inputNumber)


# Accept two inputs from the user and output its sum.
def findSum():
  num1 = int(input('enter two numbers to find the sum: '))
  num2 = int(input())
  
  print(num1 + num2)

# findSum()


# 2. Write a program to find the simple interest.
def findSimpleInterest():
  capital = int(input('enter the capital amount: '))
  interestRate = float(input('interest rate: '))
  years = int(input('enter number or years: '))


  print('simple interest is: {}'.format((capital * interestRate * years) / 100))

# findSimpleInterest()


# 3. Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
def findGrade(userMark):
  # userMark = float(input('enter the mark: '))

  if(userMark >= 90):
    return 'A'
  elif(userMark >= 80):
    return 'B'
  elif(userMark >= 70):
    return 'C'
  elif(userMark >= 60):
    return 'D'
  elif(userMark >= 50):
    return 'E'
  else:
    return 'Failed'

# print(f"your grade is: { findGrade(int(input('enter your mark: '))) }")



# 4. Using the ‘switch case’ write a program to accept an input number from the
# user and output the day according to the number. 
def useSwitch():
  userSelectedNumber = int(input('enter a number between 1 - 7: '))

  match userSelectedNumber:
    case 1:
      print('Sunday')
    case 2:
      print('Monday')
    case 3:
      print('Tuesday')
    case 4:
      print('Wednesday')
    case 5: 
      print('Thursday')
    case 6:
      print('Friday')
    case 7:
      print('Saturday')
    case _:
      print('Invalid Entry')

# useSwitch()  



# 5. Write a program to print the multiplication table of given numbers. Using for and while
    # a. Accept an input from the user and display its multiplication table

def multiplicationTable():
  userProvidedNumber = int(input('enter a number: '))

  for i in range(1, 11):
    multiplication = userProvidedNumber * i
    print(f"{i} x {userProvidedNumber} = {multiplication}")

# multiplicationTable()



# 6. Write a program to print the following pattern (hint: use nested loop)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def printPatter(n):
  for i in range(n + 1):
    line = ''
    for j in range(i + 1):
      line += str(j+1)
    
    print(line)

# printPatter(5)

def checkPalindrome():
  enterdWord = input('enter a word to check is it palindrome: ')
  for i in range(math.floor(len(enterdWord) / 2)):
    if(enterdWord[i] != enterdWord[len(enterdWord) - (i + 1)]):
      print('word is not a palindrom')
      break
    
  print(f"the word {enterdWord} is a palindrome")

# checkPalindrome()


