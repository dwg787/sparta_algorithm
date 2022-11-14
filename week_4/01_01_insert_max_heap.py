class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_idx = len(self.items) - 1

        while cur_idx > 1:
            parent_idx = cur_idx //2
            if self.items[cur_idx] > self.items[parent_idx]:
                self.items[cur_idx], self.items[parent_idx]
                cur
        return