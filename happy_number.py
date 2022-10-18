class Solution:
    def isHappy(self, num: int) -> bool:
        if sum_num(num) == 1:
            return True
        flags = {}
        count = 0
        table_truth = create_num_table()
        next_num = sum_num(num)
        while next_num != num and count <= 810:
            flags[next_num] = 1
            count += 1
            if table_truth[next_num] == 1:
                return True
            next_num = sum_num(next_num)
            print(next_num, table_truth[next_num], count)

        return False


def create_num_table():
    max_sum = 810
    table = [0]*max_sum
    for i in range(max_sum):
        if check_happy(i):
            table[i] = 1
    return table


def sum_num(num: int):
    num_str = str(num)
    return sum(int(i)**2 for i in num_str)


def check_happy(num: int):
    if sum_num(num) == 1:
        return 1
    return 0


def loop_checking(num):
    flags = {}
    count = 0
    table_truth = create_num_table()
    next_num = sum_num(num)
    while next_num != num and count != len(table_truth):
        flags[next_num] = 1
        count += 1
        if table_truth[next_num] == 1:
            return True
        next_num = sum_num(next_num)

    return False


if __name__ == "__main__":
    num = 2
    print(Solution().isHappy(num))
