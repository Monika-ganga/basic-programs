class queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,items):
        self.items.append(items)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            print("queue is empty")
    def size(self):
        return len(self.items)
object=queue()
object.enqueue(1)
object.enqueue(2)
object.enqueue(3)
object.enqueue(4)
print(object.size())
object.dequeue()
print(object.size())


