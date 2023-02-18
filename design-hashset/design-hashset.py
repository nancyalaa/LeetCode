class MyHashSet:

    def __init__(self):
        self.hash_set = set()

    def add(self, key: int) -> None:
        self.hash_set.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hash_set else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(5)
# obj.remove(5)
# param_3 = obj.contains(5)