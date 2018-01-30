# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def add_two_numbers(a, b):
    head = None
    rem = 0

    while a or b or rem:
        sum = 0
        if a:
            sum += a.value
            a = a.next
        if b:
            sum += b.value
            b = b.next
        node = Node((sum + rem) % 10)
        rem = (sum + rem) // 10
        if head:
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            head = node
    return head


if __name__ == "__main__":
    a = Node(2)
    a.next = Node(4)
    a.next.next = Node(3)
    b = Node(5)
    b.next = Node(6)
    b.next.next = Node(4)
    new_number = add_two_numbers(a, b)
    nums = []
    while new_number:
        nums.append(str(new_number.value))
        new_number = new_number.next
    print("".join(nums))