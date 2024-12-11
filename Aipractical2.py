def water_jug_problem(jug1, jug2, target):
    visited = set()
    queue = [(0, 0)]
    while queue:
        a, b = queue.pop(0)
        if (a, b) in visited:
            continue
        visited.add((a, b))
        if a == target or b == target:
            return True
        queue.extend([(jug1, b), (a, jug2), (0, b), (a, 0),
                      (min(a+b, jug1), max(0, a+b-jug1)),
                      (max(0, a+b-jug2), min(a+b, jug2))])
    return False
print(water_jug_problem(4, 3, 2))