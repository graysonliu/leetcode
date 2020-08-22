def make_title(s):
    i = s.index('.')
    s = '0' * (4 - i) + s
    s = s.lower()
    s = [c if c.isalnum() else ' ' for c in s]
    return '_'.join(''.join(s).split())


print(make_title("236. Lowest Common Ancestor of a Binary Tree"))

a = [1, 2, 3]
b = [3, 2, 1]
for i, j in a, b:
    print(i, j)
