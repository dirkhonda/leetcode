# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example:
#   Input: "babad"
#   Output: "bab"
#   Note: "aba" is also a valid answer.

def find_l_palidrome(s):
    max_len = 1
    start_index = 0
    current_length = 0

    if len(s) < 2:
        return s

    for index in range(len(s)):
        # even
        left = index
        right = index + 1

        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break

            current_length = right - left + 1
            if current_length > max_len:
                start_index = left
                max_len = current_length
            left -= 1
            right += 1

        # odd
        left = index - 1
        right = index + 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break

            current_length = right - left + 1
            if current_length > max_len:
                start_index = left
                max_len = current_length
            left -= 1
            right += 1

    return s[start_index:start_index+max_len]
if __name__ == "__main__":
    s = 'abcbb'
    print(find_l_palidrome(s))