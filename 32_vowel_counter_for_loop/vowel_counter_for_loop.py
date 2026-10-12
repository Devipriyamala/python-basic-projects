# Vowel Counter using for loop
count = 0
word = input("Enter a word: ")
for ch in word:
  if ch in "aeiouAEIOU":
    count+=1
print("Number of vowels:",count)
