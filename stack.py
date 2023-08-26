class stack:
    def __init__(self):
        self.items=[]
    def empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.empty():
            self.items.pop()
        else:
            print("stack is empty")
    def peak(self):
        if not self.empty():
            return self.items[-1]
        else:
            print("stack is empty")
    def length(self):
        return len(self.items)
object=stack()
object.push(1)
object.push(2)
object.push(3)
object.push(5)
print(object.length())
print(object.peak())
object.pop()
object.pop()
object.pop()
print(object.length())



