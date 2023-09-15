"""
File: add2.py
Name: Michelle
------------------------
There are two LinkLists and each of them represents a number.
The first Node represents Least Significant Bit and the last
Node represents Most Significant Bit. After the program adds
this two numbers, it will create a new LinkList and put the
result into the new LinkList.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        """
        Create a new LinkNode.
        """
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    :param l1: ListNode, the first LinkList
    :param l2: ListNode, the second LinkList
    :return: ListNode, the ListNode is the head of the new LinkList with the numbers added.
    """
    cur1 = l1
    cur2 = l2
    dummy = ListNode()
    cur = dummy
    carry_a_decimal = 0  # 進位值
    while cur1 and cur2:
        cur.next = ListNode((cur1.val + cur2.val + carry_a_decimal) % 10, None)  # 取餘數而得到每一位數的值
        carry_a_decimal = (cur1.val + cur2.val + carry_a_decimal) // 10  # 可得進位值
        cur = cur.next  # 往前走
        cur1 = cur1.next
        cur2 = cur2.next
    while not cur2 and cur1:  # 當l2長度小於l1
        cur.next = ListNode((cur1.val + carry_a_decimal) % 10, None)
        carry_a_decimal = (cur1.val + carry_a_decimal) // 10
        cur = cur.next
        cur1 = cur1.next
    while not cur1 and cur2:  # 當l1長度小於l2
        cur.next = ListNode((cur2.val + carry_a_decimal) % 10, None)
        carry_a_decimal = (cur2.val + carry_a_decimal) // 10
        cur = cur.next
        cur2 = cur2.next
    # 若最高位數須進位，例如99的長度為2，9的長度為1，兩者相加後位數會增加到3位，為108
    # 需為新增的最高位數創造一個node
    if not cur1 and carry_a_decimal:
        cur.next = ListNode(carry_a_decimal, None)
    elif not cur2 and carry_a_decimal:
        cur.next = ListNode(carry_a_decimal, None)
    return dummy.next


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
