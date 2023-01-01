# This program will prompt the user to enter a password and determine if the entered value is a strong password or not
# このプログラムは、ユーザーをパスワードの入力を聞いて、パスワードの強さは十分かどうかを判定します。
# Conditions for the password(パスワードの条件):
# 	At least 12 characters long (MAX: 20)
#	Contains at least one of each of the following:
# 		Uppercase, lowerchase character, symbol, and a number 
import re


# Variable definitions; 変数定義
properties = []
strong = True
length_check = False
upper_check = False
lower_check = False


# Propmt user
print("PASSWORD CHECK PROGRAM: /n")
password = input("Enter your password: ")


# Check if length is valid 
if len(password) >= 12:
	if len(password) <= 20:
		length_check = True
else:
	length_check = False

if (length_check == True):
	properties.append("Length is at least 12 characters, but does not exceed 20: PASS")
else:
	properties.append("Length is at least 12 characters, but does not exceed 20: FAIL")


# Check if uppercase letter is present
for char in password:
	if (char.isupper()):
		upper_check = True
if (upper_check == True):
	properties.append("Contains at least one uppercase character: PASS")
else:
	properties.append("Contains at least one uppercase character: FAIL")
	strong = False

#Check if lowercase letter is present
for char in password:
	if (char.islower()):
		lower_check = True
if (lower_check == True):
	properties.append("Contains at least one lowercase character: PASS")
else:
	properties.append("Contains at least one lowercase character: FAIL")
	strong = False

#Check if number is present 
regex= re.compile('[0123456789]')
if regex.search(password) != None:
	properties.append("Contains at least one number: PASS")
else:
	properties.append("Contains at least one number: FAIL")
	strong = False

#Check if special character is present
regex= re.compile('[@_!#$%^&*()<>?/\\|}{~:\[\]]')
if regex.search(password) != None:
	properties.append("Contains at least one special character: PASS")
else:
	properties.append("Contains at least one special character: FAIL")
	strong = False

#Print result
for item in properties:
	print(item)
if (strong == True):
	print("Password check passed")
else:
	print("Password check failed")