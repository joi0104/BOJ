import collections
import sys
card = collections.deque([i+1 for i in range(int(sys.stdin.readline()))])
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
print(card[0])