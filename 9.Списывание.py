def DFS(start):
    global IsBipartite
    for u in V[start]:
        if Color[u] == 0:
            Color[u] = 3 - Color[start]
            DFS(u)
        elif Color[u] == Color[start]:
            IsBipartite = False

n, m = map(int, input().split())
Color = [0] * n
IsBipartite = True
V = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    V[x-1].append(y-1)
    V[y-1].append(x-1)

for i in range(n):
    if Color[i] == 0:
        Color[i] = 1
        DFS(i)
if IsBipartite:
    print('YES')
else:
    print('NO')
