from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
# graph[álice] = ['peggy']
search_queue = deque()
search_queue += graph['you']


# while search_queue:
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print(person + " is a mango seller")
#         return True
#     else:
#         search_queue += graph[person]


class LinkList:
    next = None
    data = None

    def __init__(self, next, data):
        self.next = next
        self.data = data


def reverselist(head):
    if head == None or head.next == None:
        return head
    p = reverselist(head.next)
    head.next.next = head
    head.next = None
    return p


def print_list(p):
    while p:
        print(p, "data: ", p.data)
        p = p.next


if __name__ == '__main__':
    p = LinkList(None, 4)
    p2 = LinkList(p, 3)
    p3 = LinkList(p2, 2)
    p4 = LinkList(p3, 1)
    print_list(p4)
    head = reverselist(p4)
    print_list(head)
