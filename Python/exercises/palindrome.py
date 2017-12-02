def reverse(word):
    aux = ''
    for i in range(len(word)):
       aux += word[len(word) - 1 - i] 
    return aux

word = input("Enter a word: ")
rvs = reverse(word)

if word == rvs:
    print("The word entered is a palindrome")
else:
    print("The word entered isn't a palindrome")
