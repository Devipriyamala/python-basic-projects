# Reverse a Word
word = input("Enter a word: ")
reverse_word = ""
for i in word:
  reverse_word = i + reverse_word
print("Reversed word: ",reverse_word)
