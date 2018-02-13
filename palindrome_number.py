def check_if_palidrome(integer):
    int_list = list(str(integer))
    left = 0
    right = len(int_list) - 1

    while left < right:
        if int_list[left] is not int_list[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(check_if_palidrome(1100))