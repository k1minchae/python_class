N = int(input())
import sys
score = list(map(int, sys.stdin.readline().split()))
M = max(score)
new_score = []

for i in score:
    new_score.append(i / M * 100)
print((sum(new_score))/N)    
