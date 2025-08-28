#6.Write a program to swap the first n characters of two strings.

def swapStrings(string1,string2,n):
	if n <= len(string1) and n <= len(string2):
		prefixString1 = string1[:n]
		prefixString2 = string2[:n]
		suffixString1 = string1[n:]
		suffixString2 = string2[n:]
		string1 = prefixString2 + suffixString1
		string2 = prefixString1 + suffixString2
		return string1 , string2
	
	else:
		print("Please provide a valid n")
		print("n is greater than string1 and string2")
		return "",""

#7. Write a function that accepts two strings and returns the indices of all the occurrences of the second string in the first string as a list. If the second string is not present in the first string then it should return -1.

def indicesOfString(mainString,subString):
	listOfIndices = []
	start = 0
	for i in range(mainString.count(subString)):
		index = mainString.index(subString,start)
		start = index + 1
		listOfIndices.append(index)
	
	if listOfIndices:
		return listOfIndices
	else:
		return -1

"""8. Write a program to create a list of the cubes of only the even integers appearing in the input list (may have elements of other types also) using the following:
	a. 'for' loop
	b. list comprehension"""

def cubeEvenNumber(list):
	newList = []
	for x in list:
		if type(x) is int and x%2 == 0:
			newList.append(x**3)
	return newList
			
"""9.Write a program to read a file and
	a. Print the total number of characters, words and lines in the file.
	b. Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.
	c. Print the words in reverse order.
	d. Copy even lines of the file to a file named ‘File1’ and odd lines to another file named ‘File2’."""

def totalCharWordsLines(filepath):
	numChars = 0
	numWords = 0
	numLines = 0		
	
	fileObject = open(filepath,"r")
	text = fileObject.read()
	numChars = len(text)
	numWords = len(text.split())
	numLines = len(text.split("\n"))-1
	fileObject.close()
	return numChars,numWords,numLines

def countCharacter(filepath):
	file = open(filepath,"r")
	charDict = {}
	text = file.read()
	for i in text:
		if i not in charDict.keys():
			charDict[i] = text.count(i)
	file.close()
	return charDict

def reverseWords(filepath):
	file = open(filepath,"r")
	text = file.read()
	text = text.split("/n")
	words = []
	for i in text:
		words.extend(i.split())
	file.close()
	return words[::-1]

def seperateOddEvenLines(filepath):
	file = open(filepath,"r")
	file1 = open("/Users/veerjyotsingh/PycharmProjects/College/Practical/File1.txt","w")
	file2 = open("/Users/veerjyotsingh/PycharmProjects/College/Practical/File2.txt","w")
	lines = file.readlines()
	evenLines = []
	oddLines = []
	for i in range(len(lines)):
		if i%2 == 0:
			evenLines.append(lines[i])
		else:
			oddLines.append(lines[i])
	file1.writelines(evenLines)
	file2.writelines(oddLines)
	file1.close()
	file2.close()
	file.close()



	


if __name__ == "__main__":
	while True:
		print("","-"*30,"",sep="\n")
		print("Which question do you want:[6-10] ")
		x = int(input("Please enter your choice: "))
		
		if x == 6:
			string1 = input("Please Enter the First String: ")
			string2 = input("Please Enter the Second String: ")
			n = int(input("Please Enter a number: "))
			print(swapStrings(string1,string2,n))

		elif x == 7:
			mainString = input("Please enter the main string: ")
			subString = input("Please enter the sub string: ")
			print(indicesOfString(mainString,subString))
		
		elif x == 8:
			inputList = list(input("Please enter the list: "))
			print(cubeEvenNumber(inputList))
		
		elif x == 9:
			filepath = input("Please enter the filepath: ")
			characters, words, lines = totalCharWordsLines(filepath)
			print(f"Number of Characters are {characters}")
			print(f"Number of words are {words}")
			print(f"Number of lines are {lines}")
			
			print("Dictionary of Characters is: ",countCharacter(filepath)) 
			print("Words in reverse Order are as follow:- ", reverseWords(filepath))
			seperateOddEvenLines(filepath)
		else:
			print("bye bye..")
			break
