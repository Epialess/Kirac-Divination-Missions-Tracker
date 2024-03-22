from collections import Counter
import os

# Data taken from https://www.poewiki.net/wiki/Crimson_Temple_Map
ITEM_CARD = ["Her Mask", "Hope", "Lingering Remnants", "Lucky Deck", 
"Seven Years Bad Luck", "The Blazing Fire", "The Dragon's Heart", "The Encroaching Darkness",
"The Enlightened", "The Gambler", "The Journalist", "The Life Thief", "The Lord of Celebration",
"The Opulent", "The Tinkerer's Table", "The Trial", "The Apothecary" ]

ITEM_LEVEL = [23,68,78,74,35,47,78,73,60,68,68,68,80,23,33,73,75]

def showList(lines):

	print("************************")
	print("Current list:")
	# print(lines)
	print("\n".join(lines))
	print("************************")


def addEntry(fname,lines):
	showList(lines)
	print("---------------------------------")
	for number, card in enumerate(ITEM_CARD):
		print(number, card)
	print("---------------------------------")
	print("Add multiple cards by entering card number seperated by a space")
	cardNumbers = input("Enter card number(s) to list: ")
	f = open(fname, "a")
	index = len(lines)
	cardsArray = [x.strip() for x in cardNumbers.split(' ') if x != '']
	# print(cardsArray)
	cardsTotalToAdd = len(cardsArray)
	# print(cardsTotalToAdd)
	flag = False
	count = 0
	for idx, cardNum in enumerate(cardsArray, start=index):
		if cardNum.isdigit() and 0 <= int(cardNum) <= (len(ITEM_CARD) - 1):
			if flag == True:
				idx -= count
			else:
				flag = False

			# print(idx, cardNum)
			entry = str(idx) + " " + ITEM_CARD[int(cardNum)]
			print("Added: " + entry)
			f.write(entry + "\n")
			lines.append(entry)
		else:
			flag = True
			count += 1
			print("Unable to add invalid card number: {}".format(cardNum))

	# showList(lines)
	f.close()

def deleteLatestEntry(fname, lines):
	# https://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python
	with open(fname, "r+", encoding = "utf-8") as file:

		file.seek(0, os.SEEK_END)
		pos = file.tell() - 1

		while pos > 0 and file.read(1) != "\n":
			pos -= 1
			file.seek(pos, os.SEEK_SET)

		if pos > 0:
			file.seek(pos, os.SEEK_SET)
			file.truncate()
			file.write("\n")
	
	del lines[len(lines)-1]
	showList(lines)

def countSetOfCards(lines):
	fname = "kiracStats.txt"
	try:
		print("Creating kiracStats.txt...")
		f = open(fname, "w")
	except OSError:
		print("Could not write to file:", fname)
		sys.exit()

	tmp = lines
	# strip number from card count
	tmp = [lines.lstrip('0123456789.- ') for lines in tmp]

	# print(tmp)
	# print(Counter(tmp))
	cardInList = Counter(tmp)
	# print("\n")
	print(f"\n{'Card' : <25}{'# of Sets' : ^20}{'Percentage' : >10}")
	f.write(f"{'Card' : <25}{'# of Sets' : ^20}{'Percentage' : >10}")

	for i in cardInList.keys():
		percent = cardInList[i]/(len(tmp))*100
		# print(percent)
		print(f"{i : <25}{cardInList[i] : ^20}{format(percent, '0.2f') : >10}")
		f.write(f"\n{i : <25}{cardInList[i] : ^20}{format(percent, '0.2f') : >10}")

	for j in range(17):
		if ITEM_CARD[j] not in cardInList.keys():
			# print("Is not in list",ITEM_CARD[j])
			print(f"{ITEM_CARD[j] : <25}{0 : ^20}{format(0, '0.2f') : >10}")
			f.write(f"\n{ITEM_CARD[j] : <25}{0 : ^20}{format(0, '0.2f') : >10}")

	print(f"\n{'Total' : <25}{len(tmp) : ^20}{'100' : >10}")
	f.write(f"\n\n{'Total' : <25}{len(tmp) : ^20}{'100' : >10}")
	f.close()

def main():
	fname = "kiracList.txt"
	try:
		print("Opening file...")
		f = open(fname, "r")
	except OSError:
		print("Could not open/read file:", fname)
		sys.exit()

	with f:
		print("Reading file...")
		with open(fname) as f:
			lines = [line.rstrip() for line in f]
			# print(lines)
		# index = len(lines)
		# print("index: " + str(index))
		# print(f.read())
	f.close()

	while True:
		print("\n1.Show list")
		print("2.Add entry")
		print("3.Delete latest entry")
		print("4.Count total")
		print("5.Exit\n")
		x = input("Choose option: ")
		print("\n")
		match x:
			case '1':
				showList(lines)
			case '2':
				addEntry(fname,lines)
			case '3':
				deleteLatestEntry(fname, lines)
			case '4':
				countSetOfCards(lines)
			case _:
				break
	return 0
	
if __name__ == '__main__':
	main()