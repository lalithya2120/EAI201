# Data:
students = [
    {'hours': 2, 'pass': 0},
    {'hours': 4, 'pass': 0},
    {'hours': 6, 'pass': 1},
    {'hours': 8, 'pass': 1},
    {'hours': 10, 'pass': 1}
]

# Possible split points:
splits = [3, 5, 7, 9]

# Gini impurity:
def gini(groups):
    total = sum(len(g) for g in groups)
    score = 0.0
    for group in groups:
        size = len(group)
        if size == 0:
            continue
        passes = sum(row['pass'] for row in group)
        fails = size - passes
        p_pass = passes / size
        p_fail = fails / size
        gini_group = 1.0 - (p_pass**2 + p_fail**2)
        score += (size / total) * gini_group
    return score

best_split = None
best_gini = 1.0

for s in splits:
    left = [row for row in students if row['hours'] <= s]
    right = [row for row in students if row['hours'] > s]
    impurity = gini([left, right])
    print(f"Split at {s}: Gini = {impurity:.3f}")
    if impurity < best_gini:
        best_gini = impurity
        best_split = s

# Decision:
print("\nBest split point:", best_split)
print(f"If Study Hours <= {best_split}, → predict Fail (0)")
print(f"If Study Hours > {best_split}, → predict Pass (1)")
