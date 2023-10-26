class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end.data is None:
            return None
        else:
            val=self.end.data
            self.end=self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_Node=Node(val)
        if self.end is None:
            self.end=new_Node
        else:
            new_Node.pref=self.end
            self.end=new_Node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        temp=self.end
        while temp is not None:
            print(temp.data, end=' ')
            temp=temp.pref
        print()

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print()

stack.pop()
stack.print()