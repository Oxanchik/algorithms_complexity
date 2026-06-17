class Stack:
    def __init__(self):
        """Инициализирует стек пустым списком"""
        self.items = []

    def is_empty(self):
        """Проверяет стек на пустоту. Возвращает True, если стек пуст, иначе False."""
        return len(self.items) == 0

    def push(self, item):
        """Добавляет новый элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """
        Удаляет верхний элемент стека и возвращает его.
        Если стек пуст, выбрасывает исключение IndexError.

        """
        if self.is_empty():
            raise IndexError("Попытка удаления из пустого стека")
        return self.items.pop()

    def peek(self):
        """
        Возвращает верхний элемент стека без удаления.
        Если стек пуст, выбрасывает исключение IndexError.

        """
        if self.is_empty():
            raise IndexError("Попытка просмотра из пустого стека")
        return self.items[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)
