"""
definitely enjoyed this one more than others, second part was not too hard,
I just extracted the card number and appended the relevant additional cards
depending on the amount of winning numbers
"""
cards = []
with open("input4", 'r') as source:
    cards = source.readlines()

winning_values = []
for card in cards:
    temp_card_num = card.split("|")
    card_num = temp_card_num[0][5:8]
    win_nums = temp_card_num[0][10:].split(' ')
    my_nums = temp_card_num[1][1:75].split(' ')
    while '' in win_nums:
        win_nums.remove('')
    while '' in my_nums:
        my_nums.remove('')
    in_winning = []
    for num in my_nums:
        if num in win_nums:
            in_winning.append(num)
    if len(in_winning) > 0:
        score = 0.5
        for i in range(len(in_winning)):
            score *= 2
        winning_values.append(score)
    temp_card_num = ''
    for each in card_num:
        if each.isdigit():
            temp_card_num += each
    card_num = temp_card_num
    for x in range(0, len(in_winning)):
        cards.append(cards[int(card_num)+x])

print(sum(winning_values))
print(len(cards))