class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.index = 0

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        res = []
        if self.lst[self.index] is not None:
            res.append(self.lst[self.index])
        if self.index + 1 < len(self.lst) and self.lst[self.index + 1] is not None:
            res.append(self.lst[self.index + 1])

        self.index += 2
        return res

    def __iter__(self):
        return self

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    if len(pair) == 1:
        print(pair[0], None)
    else:
        print(pair)

