s1=input("enter first string:")
s2=input("enter second string:")
if(sorted(s1) == sorted(s2)):
	print("two strings are anagrams of each other")
else:
	print("two strings aren't anagrams of each other")
