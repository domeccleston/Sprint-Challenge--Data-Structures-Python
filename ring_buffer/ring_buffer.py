from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        else:
            if self.current is self.storage.head:
                self.storage.delete(self.storage.tail)
                self.storage.add_to_tail(item)
                self.current = self.storage.tail
            else:
                to_delete = self.current.prev
                self.storage.delete(to_delete)
                self.current.insert_before(item)
                if self.current == self.storage.head:
                    self.storage.head = self.storage.head.prev
                print(self.storage.head.value)
                self.current = self.current.prev
                self.storage.length += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        i = self.storage.tail
        while i is not None:
            list_buffer_contents.append(i.value)
            i = i.prev
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity

    def append(self, item):
        pass

    def get(self):
        pass
