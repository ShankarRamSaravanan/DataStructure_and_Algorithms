class graph:

    def __init__(self, edges):

        self.edges = edges

        self.dict = {}

        for i, j in self.edges:
            if i in self.dict:
                self.dict[i].append(j)
            else:
                self.dict[i] = [j]

        print(self.dict)


routes = [("mumbai", "paris"),
          ("mumbai", "kolkatta"),
          ("kolkatta", "tamilnadu"),
          ("tamilnadu", "kerala"),
          ("kolkatta", "kerala"),
          ("kerala", "Aandra"),
          ("tamilnadu", "Aandra")]


g = graph(routes)
