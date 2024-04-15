import sys

input = sys.stdin.readline
sys.setrecursionlimit(30000)


def dfs(cnt, x):
    global flag
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, i)
    stack.append(x)
    if cnt == n:
        flag = True


def rev_dfs(x):
    elements.append(x)
    for i in rev_graph[x]:
        if not visited[i]:
            visited[i] = 1
            rev_dfs(i)


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    stack = []
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        rev_graph[b].append(a)
    ans = []
    for i in range(n):
        flag = False
        if not visited[i]:
            visited[i] = 1
            dfs(1, i)

    visited = [0 for _ in range(n)]
    while stack:
        s = stack.pop()
        if not visited[s]:
            elements = []
            visited[s] = 1
            rev_dfs(s)
            ans.append(elements)
    flag = False
    visited = [0 for _ in range(n)]
    dfs(1, ans[0][0])
    if flag == True:
        ans[0].sort()
        for l in ans[0]:
            print(l)
    print(ans)
    print(visited)
    if flag == False:
        print('Confused')
    print()
    if tc < t - 1:
        space = input()