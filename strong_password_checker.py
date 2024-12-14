from curses.ascii import isdigit, islower, isupper


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        return solve(password)


def check_valid_len(password: str):
    n = len(password)
    if n < 6 or n > 20:
        return False
    return True


def check_valid_lowercase_condition(password: str):
    for c in password:
        if c.islower():
            return True
    return False


def check_valid_uppercase_condition(password: str):
    for c in password:
        if c.isupper():
            return True
    return False


def check_valid_digit_condition(password: str):
    for c in password:
        if c.isdigit():
            return True
    return False


def check_valid_consequence_char(password: str):
    count = 0
    s = ""
    for c in password:
        if not s or c != s[-1]:
            s = c
            count = 1
        else:
            s += c
            count += 1
        if count >= 3:
            return False
    return True


def solve(password: str):
    res = 0
    k = 0
    n = len(password)
    if not check_valid_len(password):
        if n < 6:
            return 6 - n
        elif n > 20:
            k = n - 20
    if check_valid_consequence_char(password):
        if not check_valid_lowercase_condition(password):
            res += 1
        if not check_valid_uppercase_condition(password):
            res += 1
        if not check_valid_digit_condition(password):
            res += 1
        res += k
    else:
        s = ""
        fix_step = 0
        count = 0
        for c in password:
            if not s or c != s[-1]:
                if s and c != s[-1] and count >= 3:
                    fix_step += calculate_fix(count)
                s = c
                count = 1
            else:
                s += c
                count += 1
        if count >= 3:
            fix_step += calculate_fix(count)
        print("Fix step: {}".format(fix_step))
        if not check_valid_lowercase_condition(password):
            fix_step -= 1
        if not check_valid_uppercase_condition(password):
            fix_step -= 1
        if not check_valid_digit_condition(password):
            fix_step -= 1
        fix_step = fix_step + 1
        if fix_step > k:
            res += fix_step
        elif fix_step < k:
            res == k - fix_step
    return res


def calculate_fix(count: int):
    fix_step = 0
    if count % 2 == 0:
        fix_step = count // 2 - 1
    else:
        fix_step = count // 2
    return fix_step


if __name__ == "__main__":
    pw = "aaaaAAAAAA000000123456"
    print("String length: {}".format(len(pw)))
    print("Check valid consequence chars: ", check_valid_consequence_char(pw))
    print("Check valid digit: ", check_valid_digit_condition(pw))
    print("Check valid lowercase: ", check_valid_lowercase_condition(pw))
    print("Check valid uppercase: ", check_valid_uppercase_condition(pw))
    print(solve(pw))
