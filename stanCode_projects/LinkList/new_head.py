"""
File: new_head.py
Name: Michelle
------------------------
Keep putting the ListNode's value which is less than x ahead of
the ListNode's value which is greater than or equal to the x.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def new_head(head: ListNode, x: int) -> ListNode:
    """
    :param head: ListNode
    :param x: int, the number which the user gives
    :return: ListNode, the ListNode is the head of the new LinkList which is reorganized.
    --------------------------------------------------------------------------------------
    Thinking:
        Keep putting the ListNode's value which is less than x ahead of the ListNode's value
        which is greater than or equal to the x.
    """
    ans_lst = []
    bigger_than_x = []
    cur = head
    while cur:
        if cur.val < x:
            ans_lst.append(cur.val)         # 先用來存小於x的數
        else:
            bigger_than_x.append(cur.val)   # 用來存大於等於x的數
        cur = cur.next                      # 記得往前走!
    for num in bigger_than_x:
        ans_lst.append(num)                 # 2個list裡的element合併在1個list
    cur = None
    for num in ans_lst:
        if not cur:  # first data
            ans = ListNode(num, None)
            cur = ans
        else:
            cur.next = ListNode(num, None)
            cur = cur.next
    return ans


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
        print('Error: Please type"python3 new_head.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(9, None)
            l1.next = ListNode(6, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(8, None)
            ans = new_head(l1, 8)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(1, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(2, None)
            l1.next.next.next.next = ListNode(5, None)
            l1.next.next.next.next.next = ListNode(1, None)
            ans = new_head(l1, 3)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 new_head.py test1"')


if __name__ == '__main__':
    main()
