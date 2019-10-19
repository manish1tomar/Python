class insertion_sort:
    def __init__(self, data):
        self.data = data

    def ins_sort(self):
        for i in range(len(self.data)):
            #        pdb.set_trace()
            if i > 0:
                key = self.data[i]
                for j in reversed(range(i)):
                    if self.data[j] > key:
                        self.data[j + 1] = self.data[j]
                        self.data[j] = key
        return self.data


a = insertion_sort([5, 2, 4, 6, 1, 3])
print(a.ins_sort())