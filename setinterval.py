import random
# card = {}.fromkeys(['spade','diamond','heart','club'],['2','3','4','5','6','7','8','9','10','J','Q','K','A'])
card = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_types = ['spade','diamond','heart','club']
random.shuffle(card)
random.shuffle(card_types)
print(card.pop())
print(card_types.pop())