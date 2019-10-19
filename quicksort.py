class quicksort:
    def __init__(self, data):
        self.data = data

    def partition(self, left, right):
        pivot = right
        j = right -1
        i = left
        while i in range(left, right) and i < j:
            if self.data[i] > self.data[pivot]:
                if self.data[j] < self.data[pivot]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
                else:
                    if(j >= 1):
                        j -= 1
            else:
                i += 1

        self.data[pivot], self.data[j] = self.data[j], self.data[pivot]

        return j


    def quicksort(self, left, right):
        pivot = self.partition(left, right)

        if (pivot -1 -left) > 1:
            self.quicksort(left, int(pivot-1))
        if (right -pivot -1) > 1:
            self.quicksort(int(pivot+1), right)

        return self.data

a = quicksort([5,2,4,3,6,1])
a.quicksort(0,5)
print("After Sorting ====> ", a.data)

