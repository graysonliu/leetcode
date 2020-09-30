def make_title(s):
    i = s.index('.')
    s = '0' * (4 - i) + s
    s = s.lower()
    s = [c if c.isalnum() else ' ' for c in s]
    return '_'.join(''.join(s).split())


print(make_title("11. Container With Most Water"))


def make_title_for_blog(s):
    s = [c if c.isalnum() else ' ' for c in s.lower()]
    from datetime import date
    return str(date.today()) + '-' + '-'.join(''.join(s).split())


print(make_title_for_blog('Lazy Evaluation & Late Binding: Unexpected Behavior of Iterables in Python'))
