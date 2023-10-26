class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None
        else:
            val= self.start.data
            if self.start.nref is None:
                self.end=None
            else:
                self.start.nref.pref=None
            self.start=self.start.nref
            return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node=Node(val)
        if self.end is None:
            self.end=new_node
            self.start=new_node
        else:
            new_node.pref=self.end
            self.end.nref=new_node
            self.end=new_node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        new_node=Node(val)
        node=self.start
        count=0
        while node is not None:
            if count==n:
                new_node.pref=node.pref
                new_node.nref=node
                if node.pref is None:
                    self.start=new_node
                else:
                    node.pref.nref=new_node
                node.pref.nref=new_node
                break
            count+=1
            node=node.nref

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        node=self.start
        while node is not None:
            print(node.data, end=' ')
            node=node.nref
        print()

queue=Queue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)
queue.push(50)
queue.print()

queue.pop()
queue.print()

queue.insert(2, 100)
queue.print()

