# 트리 순회
import sys
input = sys.stdin.readline

N = int(input())
C1 = [0] * N    # 왼쪽자식
C2 = [0] * N    # 오른쪽자식
for _ in range(N):
    p, c1, c2 = input().split()
    idx = ord(p)-ord('A')
    C1[idx] = c1
    C2[idx] = c2

# 전위순회
def pre(node):
    idx = ord(node) - ord('A')
    print(node, end='')
    if C1[idx] != '.':
        pre(C1[idx])
    if C2[idx] != '.':
        pre(C2[idx])
pre('A')
print()

# 중위순회
def mid(node):
    idx = ord(node) - ord('A')
    if C1[idx] != '.':
        mid(C1[idx])
    print(node, end='')
    if C2[idx] != '.':
        mid(C2[idx])
mid('A')
print()

# 후위순회
def post(node):
    idx = ord(node) - ord('A')
    if C1[idx] != '.':
        post(C1[idx])
    if C2[idx] != '.':
        post(C2[idx])
    print(node, end='')
post('A')