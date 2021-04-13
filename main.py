class CustomList:
    """Класс, определяющий поэлементное сложение списков"""
    res = []
    min_len = 0

    def __init__(self, x):
        super().__init__()
        self.taking_list = list(x)

    def __add__(self, other):
        getting = CustomList.mid(self, other)
        min_len = getting[0]
        new_taking_list = getting[1]
        new_other = getting[2]
        i: int
        for i in range(min_len):
            CustomList.res.append(new_taking_list[i] + new_other[i])
        if len(new_taking_list) == min_len:
            for i in range(min_len, len(new_other)):
                CustomList.res.append(new_other[i])
        else:
            for i in range(min_len, len(new_taking_list)):
                CustomList.res.append(new_taking_list[i])
        return CustomList(CustomList.res)

    def __radd__(self, other):
        if len(CustomList.res) != 0:
            CustomList.res.clear()
        min_len = min(len(self.taking_list), len(other))
        i: int
        for i in range(min_len):
            CustomList.res.append(self.taking_list[i] + other[i])
        if len(self.taking_list) == min_len:
            for i in range(min_len, len(other)):
                CustomList.res.append(other[i])
        else:
            for i in range(min_len, len(self.taking_list)):
                CustomList.res.append(self.taking_list[i])
        return CustomList(CustomList.res)

    def __sub__(self, other):
        getting = CustomList.mid(self, other)
        min_len = getting[0]
        new_taking_list = getting[1]
        new_other = getting[2]
        i: int
        for i in range(min_len):
            CustomList.res.append(new_taking_list[i] - new_other[i])
        if len(new_taking_list) == min_len:
            for i in range(min_len, len(new_other)):
                CustomList.res.append(0 - new_other[i])
        else:
            for i in range(min_len, len(new_taking_list)):
                CustomList.res.append(new_taking_list[i])
        return CustomList(CustomList.res)

    def __rsub__(self, other):
        if len(CustomList.res) != 0:
            CustomList.res.clear()
        min_len = min(len(self.taking_list), len(other))
        i: int
        for i in range(min_len):
            CustomList.res.append(other[i] - self.taking_list[i])
        if len(self.taking_list) == min_len:
            for i in range(min_len, len(other)):
                CustomList.res.append(other[i])
        else:
            for i in range(min_len, len(self.taking_list)):
                CustomList.res.append(0 - self.taking_list[i])
        return CustomList(CustomList.res)

    def mid(self, other):
        """Функция, определяющая тип входных данных"""
        if len(CustomList.res) != 0:
            CustomList.res.clear()
        new_taking_list = self.taking_list
        if isinstance(other, list):
            new_other = other
        else:
            new_other = other.taking_list
        min_len = min(len(new_taking_list), len(new_other))
        return min_len, new_taking_list, new_other

    def __str__(self):
        return f'{CustomList.res}'


if __name__ == '__main__':
    s = CustomList([1, 3, 5]) - CustomList([2])
    m = CustomList([9]) - [3]
    print(s-m)
    print(s + m)
    print(CustomList([1]) + CustomList([2]) + CustomList([9]) + [3])
    print(CustomList([1, 2]) + CustomList([1, 2, 11]))
    print(CustomList([2, 9, 8, 10]) + [3, 1, 6])
    print([17, 1, 5] + CustomList([2, 9]))
    print(CustomList([3, 8]) - CustomList([1, 2, 11]))
    print(CustomList([3, 8, 20]) - CustomList([1, 2]))
    print(CustomList([2, 9, 8, 10]) - [3, 1, 6])
    print([17, 1, 5] - CustomList([2, 9]))

