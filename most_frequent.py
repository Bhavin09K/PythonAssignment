from calendar import month_abbr
import collections


x = input('Please enter a string : ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

y_dict = most_frequent(x)

A = sorted(y_dict.items(), key=lambda a :a[1])
print(A)