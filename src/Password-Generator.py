import mechanicalsoup
import json
from random import randrange
from random import randint

API_URL = 'https://api.datamuse.com/words?rel_trg='

def random_case(string):
	password = ''
	for char in string:
		case = randint(0, 1)
		if case == 0:
			password += char.upper()
		elif case == 1:
			password += char.lower()	
	return password

def password_generator():
	password_lst = []

	print("Exit and generate password by typing '/'.") 
	i=0
	while (True):
		try:
			userinput = input(f"Enter keyword {i+1}: ").rstrip()
			if userinput == '/' and i != 0:
				break

			url = API_URL+f'{userinput}'

			browser = mechanicalsoup.Browser()
			response = browser.get(url)
			data = json.loads(response.text)
			random_num = randrange(len(data)) # randrange throws ValueError is data = 0
			password_lst.append(data[random_num]['word'])
			i += 1
		except ValueError:
			if userinput == '/' and i == 0:
				print("Minimum 1 keyword required.")
			else:	
				print("Got nothing for that, try again.")

	print(f"Your {i} randomly generated words were {'/'.join(password_lst)}.")
	password = random_case(''.join(password_lst))
	print(f"Generated password: {password}\n")

def main():
	print("### Password-Generator ###")
	while True:
		password_generator()

if __name__ == '__main__':
	main()