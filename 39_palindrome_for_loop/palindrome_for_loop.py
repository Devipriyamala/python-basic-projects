# Palindrome using for loop
reverse_word = ""
word = input("Enter a word: ")
for i in word:
  reverse_word = i + reverse_word
if word == reverse_word:
  print(word,"is a Palindrome.")
else:
  print(word,"is not a Palindrome.")
