import string
newString = input("Enter input: ").lower() #newString takes the input and converts everything to lower
new = list(set(newString.split())) #Split the new strings into a collection of words to put in a set.
#This needs to be converted back into a list since sort() method is for lists only
new.sort()
print(" ".join(new)) #Prints the elements of list as a string joined by space ie. like  a regular sentence
