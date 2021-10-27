words = {'a': '11010','b': '10111','c':'00111','d':'11100','e':'00100'}
arr = []
inp = input(': ')
for i in inp:
    arr.append(words[str(i)])
print(arr)