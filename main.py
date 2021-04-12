class CustomList():
    res = []
    min_len = 0
    def __init__(self, x):
        super().__init__()
        self.taking_list = list(x)

    def __add__(self, other):
        if len(CustomList.res) != 0:
            CustomList.res.clear()
        if isinstance(other, list):
            print("aaaaa")
            a = len(self.taking_list)
            b = len(other)
            min_len = min(a, b)
            i: int
            for i in range(min_len):
                CustomList.res.append(self.taking_list[i] + other[i])
            if len(self.taking_list) == min_len:
                for i in range(min_len, len(other)):
                    CustomList.res.append(other[i])
            else:
                for i in range(min_len, len(self.taking_list)):
                    CustomList.res.append(self.taking_list[i])
        else:
            print("bbbb")
            a = len(self.taking_list)
            b = len(other.taking_list)
            min_len = min(a, b)
            for i in range(min_len):
                CustomList.res.append(self.taking_list[i] + other.taking_list[i])
            if len(self.taking_list) == min_len:
                for i in range(min_len, len(other.taking_list)):
                    CustomList.res.append(other.taking_list[i])
            else:
                print("bbbb")
                for i in range(min_len, len(self.taking_list)):
                    CustomList.res.append(self.taking_list[i])

        return CustomList(self.taking_list)

    def __radd__(self, other):
        print("cccccc")
        if len(CustomList.res) != 0:
            CustomList.res.clear()
        a = len(self.taking_list)
        b = len(other)
        min_len = min(a, b)
        i: int
        for i in range(min_len):
            CustomList.res.append(self.taking_list[i] + other[i])
        if len(self.taking_list) == min_len:
            for i in range(min_len, len(other)):
                CustomList.res.append(other[i])
        else:
            for i in range(min_len, len(self.taking_list)):
                CustomList.res.append(self.taking_list[i])
        return CustomList(self.taking_list)


    def __sub__(self, other):
        # return CustomList(self.taking_list - list(other.taking_list))
        pass
    def __rsub__(self, other):
        # return CustomList(self.taking_list - list(other.taking_list))
        pass

    def __str__(self):
        return f'{CustomList.res}'


if __name__ == '__main__':
    s = CustomList([3, 8, 11]) + CustomList([1, 2])
    print(s)
    m = CustomList([2, 9, 8, 10]) + [3, 1, 6]
    print(m)
    n = [17, 1, 5] + CustomList([2, 9])
    print(n)

