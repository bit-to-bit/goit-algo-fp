"""Task 1 - Linked List"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        cur = self.head
        i = 0
        while cur:
            i += 1
            cur = cur.next
        return i

        return self.number

    def get_last_node(self):
        res = self.head
        while res.next:
            res = res.next
        return res

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" >> ")
            current = current.next
        print("\n")

    def reverse(self):
        if self.head:
            cur = self.head
            next = cur.next
            previous = None
            while next:
                cur.next = previous
                previous = cur
                cur = next
                next = cur.next
            cur.next = previous
            self.head = cur

    def insertion_sort(self):
        end_node = self.head
        cur = self.head
        while cur.next:
            cur = cur.next
            check_node = self.head
            do_next_check = True
            if cur.data <= self.head.data:
                self.delete_node(cur.data)
                self.insert_at_beginning(cur.data)
                do_next_check = False
            while do_next_check:
                if check_node.next:
                    if cur.data <= check_node.next.data:
                        self.delete_node(cur.data)
                        self.insert_after(check_node, cur.data)
                        do_next_check = False
                if check_node == end_node:
                    self.delete_node(cur.data)
                    self.insert_after(check_node, cur.data)
                    end_node = cur
                    do_next_check = False
                check_node = check_node.next

    def join_sorted_linked_list(self, adding_linked_list):
        # Відсортуємо вихідний список на випадок, якщо не відсортований
        self.insertion_sort()

        while adding_linked_list.head:
            processed = adding_linked_list.head
            current = self.head
            do_next_check = True
            if processed.data <= current.data:
                adding_linked_list.delete_node(processed.data)
                self.insert_at_beginning(processed.data)
            else:
                while do_next_check:
                    if current.next:
                        if processed.data <= current.next.data:
                            adding_linked_list.delete_node(processed.data)
                            self.insert_after(current, processed.data)
                            do_next_check = False
                    else:
                        adding_linked_list.delete_node(processed.data)
                        self.insert_after(current, processed.data)
                        do_next_check = False
                    current = current.next


llist = LinkedList()
second_llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Вставляємо вузли у second_llist
second_llist.insert_at_beginning(1)
second_llist.insert_at_beginning(2)
second_llist.insert_at_beginning(17)
second_llist.insert_at_beginning(100)
second_llist.insertion_sort()

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Друк зв'язного списку після операції реверсування
llist.reverse()
print("Зв'язний список після реверсування:")
llist.print_list()

# Друк зв'язного списку після операції сортування
llist.insertion_sort()
print("Зв'язний список після сортування:")
llist.print_list()


# Тест функції обєднання двох відсортованих списків в один
print("Другий звязний список для додавання:")
second_llist.print_list()

llist.join_sorted_linked_list(second_llist)
print("Зв'язний список після додавання другого відсортованого списку:")
llist.print_list()
