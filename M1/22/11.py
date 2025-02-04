class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def simple_hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        hash = self.simple_hash(key)
        # Линейное пробирование: ищем следующий свободный слот
        while self.table[hash] is not None:
            hash = (hash + 1) % self.size
        self.table[hash] = (key, value)

    def get(self, key):
        hash = self.simple_hash(key)
        start_index = hash  # Чтобы избежать бесконечного цикла
        # Линейное пробирование для поиска элемента
        while self.table[hash] is not None:
            if self.table[hash][0] == key:
                return self.table[hash][1]
            hash = (hash + 1) % self.size
            if hash == start_index:
                return None  # Пройден весь массив
        return None
