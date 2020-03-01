import collections
word = collections.Counter(input().upper())
word = sorted(word.items(), key=lambda x : x[1], reverse=True)
if len(word)>1 and word[0][1] == word[1][1] : print('?')
else: print(word[0][0])