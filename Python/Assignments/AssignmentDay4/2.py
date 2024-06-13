Original_dictionary =  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

ascending = dict(sorted(Original_dictionary.items(), key= lambda item: item[1], reverse=False))
decending = dict(sorted(Original_dictionary.items(), key= lambda item: item[1], reverse=True))

print("Dictionary in ascending order by value :",ascending)
print("Dictionary in descending order by value :",decending)
