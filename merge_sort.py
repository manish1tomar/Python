class merge_sort():
    def __init__(self, data):
        self.data = data

    def merge(self, data_arr1, data_arr2):
        data_res = []
        i = 0
        j = 0
        k = 0
        total_len = len(data_arr1) + len(data_arr2)

        while k < total_len:
            if i >= len(data_arr1):
                data_res.extend(data_arr2[j:])
                break
            elif j >= len(data_arr2):
                data_res.extend(data_arr1[i:])
                break
            elif data_arr1[i] > data_arr2[j] and j < len(data_arr2):
                data_res.append(data_arr2[j])
                j += 1
                k += 1
            elif i < len(data_arr1):
                data_res.append(data_arr1[i])
                i += 1
                k += 1

        return data_res

    def split_arr(self, data_arr):
        if len(data_arr) > 1:
            return self.merge(self.split_arr(data_arr[:int(len(data_arr) / 2)]),
                              self.split_arr(data_arr[int((len(data_arr) / 2)):]))
        else:
            return data_arr


a = merge_sort([5, 2, 4, 6, 1, 3, 7])
print(a.split_arr(a.data))