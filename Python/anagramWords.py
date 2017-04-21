print ("Anagram finder")
print ("Enter two key words to check if they are anagram of each other")

word1 = raw_input("Word 1: ")
word2 = raw_input("Word 2: ")

count = 0
if (len(word1)>len(word2) or len(word1)==len(word2) ):
	word11 = word1
	while(count!=len(word2)):
		for w in range(len(word2)):
			if word2[w] in word11:
				word11 = list(word11)
				count +=1
				word11.remove(word2[w])
		break		
elif(len(word1)<len(word2)):
	word22 = word2
	while(count!=len(word1)):
		for w in range(len(word1)):
			if word1[w] in word22:
				word22 = list(word22)
				count +=1
				word22.remove(word1[w])
		break
		
if(count == len(word1)):
	print (word1)+" is an anagram of "+(word2)
elif(count == len(word2)):
	print (word2)+" is an anagram of "+(word1)
else:
	print (word1)+" and "+(word2)+" are NOT anagram of each other"