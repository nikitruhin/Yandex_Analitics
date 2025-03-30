def can_weigh_all(n, weights):
    possible_weights = set()
    possible_weights.add(0)
    for weight in weights:
        new_weights = set()
        for existing_weight in possible_weights:
            new_weights.add(existing_weight + weight)
            new_weights.add(abs(existing_weight - weight))
        possible_weights.update(new_weights)
    for i in range(1, n + 1):
        if i not in possible_weights:
            return False
    return True


n = int(input())
weights = list(map(int, input().split()))
if can_weigh_all(n, weights):
    print('Yes')
else:
    print('No')
