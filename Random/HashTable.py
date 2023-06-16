class Hastable:

    def __init__(self):
        self.max = 100
        self.array = [None for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash = + ord(char)

        return hash % self.max


# def __setitem__ -- while callling ht['march 18']  =199


    def add(self, index, val):
        hash = self.get_hash(index)
        self.array[hash] = val


# def __getitem__ while calling ht[' march 18']

    def get(self, index):
        hash = self.get_hash(index)
        return self.array[hash]

    def __delitem__(self, index):
        hash = self.get_hash(index)
        self.array[hash] = None


ht = Hastable()


ht.add('march 6', 300)

print(ht.array)


# Linear probing and Collision


print(ht.get("march 6"))


del ht['march 6']

print(ht.array)
