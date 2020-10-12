class Linked_list():
    def __init__(self, collection=None):
        self.head = None    
        if collection:
            for item in reversed(collection):   
                self.insert(item)
    
    def insert(self, value):
        self.head = Node(value, self.head)
    
    def append(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def __iter__(self):
        def value_generator():
            current = self.head

            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __len__(self):
        return len(list(iter(self)))

    def __str__(self):
        output = ''
        for value in self:
            output += f"[ {value} ] -> "
        output += "None"
        return output

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):

        if index < 0:
            raise IndexError
        for i, item in enumerate(self):  
            if i == index:
                return item 
        raise IndexError

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_ 


if __name__ == "__main__":

    foods = Linked_list(['apple', 'banana', 'carrot'])
    first_food = foods[0]
    
    for food in foods:
        print(food)

    def gen():
        

        i = 0
        while True:
            yield i 
            i += 1

        for i in range(100):
            print(next(num_gtr))

    num_gtr = gen()
    print(num_gtr)
