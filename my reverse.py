while True:
    word = (input("Enter Here : "))
    newword=''
    print('The length of this word was', len(word),'characters')
    letters = len(word)
    for x in range(letters):
       newword += word[letters-x-1]
    print(newword.title().strip())
