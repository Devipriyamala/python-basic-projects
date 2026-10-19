#Count the Frequency of the Character
count = 0
word = input("Enter a word: ")
character = input("Enter a single character: ")
word = word.lower()
character = character.lower()
for i in word:
  if i == character:
    count += 1
print("Character",character,"appears",count,"times.")
