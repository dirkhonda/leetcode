def lengthOfLastWord(s):
    words = s.split(' ')
    length = 0
    for word in words:
        if not word:
            continue
        else:
            length = len(word)
    return length

if __name__ == "__main__":
    s = "Green eggs and ham"
    print(lengthOfLastWord(s))