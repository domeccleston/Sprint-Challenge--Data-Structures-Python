from doubly_linked_list import DoublyLinkedList


# ugly implementation but passes tests, array buffer is properly implemented
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
                self.storage.insert_before(self.current, item)
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
        self.current = None
        self.storage = []
        self.count = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.count += 1
        else:
            self.count += 1
            self.storage[(self.count % self.capacity) - 1] = item

    def get(self):
        return self.storage


arb = ArrayRingBuffer(3)