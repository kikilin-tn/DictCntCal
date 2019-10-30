"""
可計算出字串中，每個字出現的次數
"""

message = 'It was a good day, and the company tourney will be held in weekend.'
count = {}

for character in message:
  count.setdefault(character,0)
  count[character] = count[character]+1

print(count)
