import sys
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1
        y -= 1
        g[x].append(y)
        g[y].append(x)
    
    component = [0] * n
    components = defaultdict(list)  
    num = 0
    
    for v in range(n):
        if component[v] == 0:
            num += 1
            stack = [v]
            component[v] = num
            components[num].append(v + 1) 
            
            while stack:
                u = stack.pop()
                for neighbor in g[u]:
                    if component[neighbor] == 0:
                        component[neighbor] = num
                        stack.append(neighbor)
                        components[num].append(neighbor + 1)  
    
    for key in components:
        print(len(components[key]))
        print(' '.join(map(str, components[key])))

if __name__ == "__main__":
    main()
