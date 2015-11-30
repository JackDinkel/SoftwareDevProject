import sys
import pydoc

'''
This is the main file for the python test script

This program is designed to take user input and
calculate how much their phone is worth. At the very
end, it spits out a price.

All testing is done on this file

All auto-documentation is done on this file using pydoc
'''

def findPhone(phoneList, i=0):
	'''
		Uses phones in phoneDic to ask the user which phone they have.
		Takes user input using the terminal and parses it.

		Takes the list of phones(phoneDic.keys()) as input.
		Returns the user's phone.
	'''

	x = 1
	for phone in phoneList:
		print "%d. %s" % (x, phone)
		x += 1
	if not i:
		i = int(input("Please enter the number corresponding to the phone you have. "))
	currentPhone = phoneList[i-1]
	print "You currently own the", currentPhone

	return currentPhone

def findCarrier(carrierList, i=0):
	'''
		Uses carriers in carrierDic to ask the user which carrier they have.
		Takes user input using the terminal and parses it.

		Takes the list of carriers(carrierDic.keys()) as input.
		Returns the user's carrier.
	'''

	#print carrierList
	x = 1
	for carrier in carrierList:
		print "%d. %s" % (x, carrier)
		x += 1
	if not i:
		i = int(input("Please enter the number corresponding to the carrier you have. "))
	currentCarrier = carrierList[i-1]
	print "Your carrier is ", currentCarrier

	return currentCarrier


def power(i=0):
	'''
	Asks the user whether their phone can power on.
	Takes user input using the terminal and parses it.

	Returns True if it can or False if it can't.
	'''
	if not i:
		i = raw_input("Does your phone turn on? (y)es or (n)o. ")
	if i == "y":
		print "Your phone turns on."
		return True
	else:
		print "Your phone does not turn on."
		return False


def screenDamage(i=0):
	'''
	Asks the user to rate the condition of their screen from 1-3
		3: flawless
		2: scratched
		1: cracked
	Takes user input using the terminal and parses it.

	Returns the number 1, 2, or 3.
	'''

	if not i:
		i = int(raw_input("From 1-3, please rate the condition of your screen, 3 being flawless, 2 being scratched, 1 being cracked: "))
	if i == 1:
		print "Your screen is cracked."
	elif i == 2:
		print "Your screen is scratched."
	elif i == 3:
		print "Your screen is flawless."
	return i

def waterDamage(i=0):
	'''
	Asks the user if their phone has water damage.
	Takes user input using the terminal and parses it.

	Returns True if it is damaged and False if it is not.
	'''

	if not i:
		i = raw_input("Does your phone have water damage? (y)es or (n)o. ")
	if i == "y":
		print "Your phone has water damage."
		return True
	else:
		print "Your phone has no water damage."
		return False

def buttons(i=0):
	'''
	Asks the user how many broken buttons their phone has.
	Takes user input using the terminal and parses it.

	Returns the number of broken buttons.
	'''

	if not i:
		i = int(raw_input("How many broken buttons does your phone have? "))
	print "You have %d broken buttons" % i
	return i

def birds(i=0):
	'''
	Asks the user if their phone has the Angry Birds app installed
	Takes user input using the terminal and parses it.

	Returns True if it is installed and False if it is not.
	'''

	if not i:
		i = raw_input("Does your phone have Angry Birds? (y)es or (n)o. ")
	if i == "y":
		print "Your phone has Angry Birds."
		return True
	else:
		print "Your phone does not have Angry Birds."
		return False

def contract(i=0):
	'''
	Asks the user if their phone is under contract.
	Takes user input using the terminal and parses it.

	Exits the program if the phone is under contract.
	Returns nothing.
	'''

	if not i:
		i = raw_input("Is this phone under contract? (y)es or (n)o. ")
	if i == "y":
		print "We cannot purchase your phone at this time."
		sys.exit()
	else:
		print "Your phone is not under contract."

def insurance(i=0):
	'''
	Asks the user if their phone is covered by insurance.
	Takes user input using the terminal and parses it.

	Returns True if it is, and False if it is not.
	'''

	if not i:
		i = raw_input("Is your phone covered by insurance? (y)es or (n)o. ")
	if i == "y":
		print "Your phone is covered."
		return True
	else:
		print "Your phone is not covered."
		return False

def frame(i=0):
	'''
	Asks the user to rate the condition of their frame
		4: flawless
		3: slightly damaged
		2: moderately damaged
		1: severely damaged
	Takes user input using the terminal and parses it.

	Returns the number 1, 2, 3, or 4.
	'''

	if not i:
		i = int(raw_input("From 1-4, please rate the condition of your frame, 4 being flawless, 3 being slightly damaged, 2 being moderately damaged, 1 being severely damaged: "))
	if i == 1:
		print "Your screen is severely damaged."
	elif i == 2:
		print "Your screen is moderately damaged."
	elif i == 3:
		print "Your screen is slightly damaged."
	elif i == 4:
		print "Your screen is flawless"
	return i

def box(i=0):
	'''
	Asks the user whether they have the original box for their phone.
	Takes user input using the terminal and parses it.

	Returns True if they have the box, False if they don't.
	'''

	if not i:
		i = raw_input("Do you have the original box for your phone? (y)es or (n)o. ")
	if i == "y":
		print "You have the original box."
		return True
	else:
		print "You do not have the original box."
		return False

def old(i=0):
	'''
	Asks the user how many months they have had their phone.
	Takes user input using the terminal and parses it.

	Returns the number of years as an integer
	'''

	if not i:
		i = int(raw_input("How many months have you had your phone? "))
	print "You have had your phone for %d months" % i
	return i

def condition(i=0):
	'''
	Asks the user whether their phone is used.
	Takes user input using the terminal and parses it.

	Returns True if the phone is used, False if it is not.
	'''

	if not i:
		i = raw_input("Is your phone used? (y)es or (n)o. ")
	if i == "y":
		print "Your phone is used."
		return True
	else:
		print "Your phone is new."
		return False

def build_phoneDic():
	'''
	Builds the phone dictionary, stored in the variable phoneDic.
	This function reads in the file "phone_dictionary" and parses
	it. It then stores the data in the file into the dictionary.

	THIS FUNCTION IS DEPRECATED AND SHOULD BE HANDLED BY A DATABASE
	'''

	phoneDic = {}
	f = open("phone_dictionary")
	for line in f.readlines():
		if line[0] != '#' and line.isspace() != True:
			line = line.split('$')
			phone = line[0]
			phone = phone.strip()
			price = line[1]
			price = price.strip()
			phoneDic[phone] = float(price)
	return phoneDic

def build_carrierDic():
	'''
	Builds the carrier dictionary, stored in the variable carrierDic.
	This function reads in the file "carrier" and parses
	it. It then stores the data in the file into the dictionary.

	THIS FUNCTION IS DEPRECATED AND SHOULD BE HANDLED BY A DATABASE
	'''

	carrierDic = {}
	c = open("carrier")
	for line in c.readlines():
		if line[0] != '#' and line.isspace() != True:
			line = line.split('=')
			carrier = line[0]
			carrier = carrier.strip()
			constant = line[1]
			constant = constant.strip()
			carrierDic[carrier] = float(constant)
	return carrierDic

def main():
	'''
	This is the main function for the python test script

	This program is designed to take user input and
	calculate how much their phone is worth. At the very
	end, it spits out a price.

	It works by calling several different functions which
	all ask different questions.
	It then calculates the final price.
	'''

	#build phone dictionary using file "phone_dictionary"
	phoneDic = build_phoneDic()

	#build carrier dictionary using file "carrier"
	carrierDic = build_carrierDic()
	
	#ask the user their phone and carrier
	currentPhone = findPhone(phoneDic.keys())
	currentCarrier = findCarrier(carrierDic.keys())

	#calculate the coefficient based off the carrier
	carrierCoefficient = carrierDic[currentCarrier]

	#set to initial value
	phoneWorth = phoneDic[currentPhone]

	#decrement phoneworth based on the carrier coefficient
	phoneWorth = phoneWorth * carrierCoefficient

	#contract() #ensure phone is not under contract
	#c = condition()
	#if c == False:
	#	print "Your phone is worth $%s" % phoneWorth
	#	sys.exit()
	#i = insurance()

	print "What condition is your phone in?"
	print "(E)xcellent"
	print "(G)ood"
	print "(P)oor"
	conditionChecker = raw_input();

	if conditionChecker == 'E':
		phoneWorth = .8 * ((.88 * phoneWorth) - 5)

	elif conditionChecker == 'G':
		phoneWorth = .8 * (((.88 * phoneWorth) - 5) * .8)

	else:
		#ask about damages
		p = power()
		wd = waterDamage()
		sd = screenDamage()
		butt = buttons()
		f = frame()
		b = box()
		o = old()
	#angry birds
		bird = birds()

	#account for insurance
		if i:
			phoneWorth += phoneWorth * .05
	#account for how old the phone is
		if o > 24:
			phoneWorth -= phoneWorth * .4
		elif o > 12:
			phoneWorth -= phoneWorth * .1
	#account for whether phone powers on
		if p == False:
			phoneWorth -= phoneWorth * .75
	#account for water damage
		if wd:
			phoneWorth -= phoneWorth * .3
	#account for screen damage
		if currentPhone == "Galaxy S5" or currentPhone == "Galaxy S4" or currentPhone == "Galaxy S3" or currentPhone == "Note 3" or currentPhone == "Note 2" or currentPhone == "LG G2" or currentPhone == "HTC One M7" or currentPhone == "HTC One M8":
			if sd == 1:
				phoneWorth -= phoneWorth * .6
			elif sd == 2:
				phoneWorth -= phoneWorth * .15
		else:
			if sd == 1:
				phoneWorth -= phoneWorth * .4
			elif sd == 2:
				phoneWorth -= phoneWorth * .15
	#account for frame damage
		if f == 1:
			phoneWorth -= phoneWorth * .15
		elif f == 2:
			phoneWorth -= phoneWorth * .1
		elif f == 3:
			phoneWorth -= phoneWorth * .05
	#account for whether owner has box
		if b:
			phoneWorth += 5
	#account for broken buttons
		phoneWorth -= 5 * butt
	#account for whether phone has angry birds
		if bird:
			phoneWorth += 10


		if phoneWorth <= 10:
			print "Sorry, we cannot purchase your phone at this time."
			sys.exit()



	print "Your phone is worth $%s" % round(phoneWorth, 2)

if __name__ == '__main__':
	main()
