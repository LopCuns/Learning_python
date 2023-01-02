hash = {}

hash['k1'] = 1
hash['h2'] = "2"
print(hash['k1'],hash['h2'])
hash.pop('k1')
print(len(hash))
hash.clear()