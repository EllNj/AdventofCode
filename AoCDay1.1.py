with open("AoCday1Data", 'r') as source:
    strings = source.readlines()
    numbers = []
    wordDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numberVersion = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for each in strings:
        tempnum = ''
        for y in range(1, 4):
            for word in wordDigits:
                listword = list(each)
                if word in each:
                    index = each.index(word) + 1
                    listword[index] = numberVersion[word]
                each = ''.join(listword)
        for i in each:
            if i.isdigit():
                tempnum += i
        numbers.append(int(tempnum[0]+tempnum[-1]))
    print(sum(numbers))
# this resulted in the correct answer correct
"""
part 2 was much harder, had to iterate through and change each word version so that it now had the 
digit i did this by replacing the second digit of the word version with the number it spelt so then
the part of the code that takes the first and last digit still worked, had an issue where there were 
multiple of the same word digit in a string so had to increase how many times i check the word for the 
digit to 4 times so that all word versions were correctly changed
"""
