from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.sorted_map = {}  # Maps number -> SortedSet of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.sorted_map:
                self.sorted_map[old_number].discard(index)  # Remove old index
        
        self.index_to_number[index] = number
        
        if number not in self.sorted_map:
            self.sorted_map[number] = SortedSet()
        self.sorted_map[number].add(index)

    def find(self, number: int) -> int:
        if number in self.sorted_map and self.sorted_map[number]:
            return self.sorted_map[number][0]  # Get smallest index
        return -1
