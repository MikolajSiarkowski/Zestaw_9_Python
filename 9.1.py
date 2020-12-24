class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(n)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("Lista jest pusta")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            while node.next != self.tail:
                node = node.next
            self.tail = node
            node.next = None
            self.length -= 1
            return self.tail

    def merge(self,other):
        while other.is_empty() == False:
           self.insert_tail(other.head)
           other.remove_head()

    def clear(self):
        while self.is_empty() == False:
            self.remove_head()

alist = SingleList()
blist = SingleList()
blist.insert_head(Node(34))         # blist [34]
blist.insert_head(Node(44))         # blist [44, 34]
print ( "blist length {}".format(blist.length) ) # odczyt atrybutu
alist.insert_head(Node(11))         # alist [11]
alist.insert_head(Node(22))         # alist [22, 11]
alist.insert_tail(Node(33))         # alist [22, 11, 33]
print ( "\n") 
print ( "alist length {}".format(alist.count()) ) # wykorzystujemy interfejs
alist.merge(blist)                  # alist [22,11,33,44,34]
print ( "\n")  
print ( "alist merge with blist\nalist length {}".format(alist.length) ) # odczyt atrybutu
print ( "blist length {}".format(blist.length) ) # odczyt atrybutu
alist.clear()                       # alist []
print ( "\n") 
print ( "alist clear\nalist length {}".format(alist.count()) ) # wykorzystujemy interfejs

