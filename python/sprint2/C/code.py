# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(head, index):
    if index == 0:
        return get_node_by_index(head, 1)
    deleted_node = get_node_by_index(head, index)
    previous_node = get_node_by_index(head, index-1)
    if deleted_node.next_item == None:
        previous_node.next_item = None
    previous_node.next_item = deleted_node.next_item
    return head



def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    # assert new_head is node0
    # assert new_head.next_item is node2
    # assert new_head.next_item.next_item is node3
    # assert new_head.next_item.next_item.next_item is None
    node = new_head
    while node:
        print(node.value)
        node = node.next_item
    # result is node0 -> node2 -> node3

if __name__ == '__main__':
    test()