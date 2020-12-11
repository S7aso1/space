words = input("Give me words and separate them with whitespace: ")
wordsArray = words.split(' ')
wordsArray = list(set(wordsArray))
wordsArray.sort()
sentance = ' '.join(wordsArray)
print(sentance)

