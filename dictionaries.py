dictionaries = {'a': 1, 'b': 2, 'c': 3}
print(len(dictionaries)) # 3
#print(dictionaries.clear()) # empty dict
print(dictionaries.copy) # <built-in method copy of dict object at 0x7fe08e147c40>
print(sorted(list(dictionaries))) # ['a', 'b', 'c']
print(sorted(list(dictionaries.values()))) # [1, 2, 3]
print(sorted(list(dictionaries), key=dictionaries.__getitem__)) # ['a', 'b', 'c']
print(sorted(list(dictionaries),reverse=True))
print([value for (key, value) in sorted(dictionaries.items())]) # [1, 2, 3]

def wordcount(filename):
    try:
        data = open(filename)
    except:
        print("Can't reach the file")
        exit()
    count = dict()
    for line in data:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1   
            else:
                count[word] += 1
    return count   
wordcount()