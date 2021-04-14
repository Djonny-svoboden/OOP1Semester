import pickle
from collections import deque
import os
from abc import abstractmethod
from typing import Protocol, runtime_checkable, Iterable


######################################################
@runtime_checkable
class Printable(Protocol):
    @abstractmethod
    def printQueue(self):
        pass


class Queue:  # superclass
    def __init__(self, filename):
        # self.name=name
        self.items = deque()
        self.filename = filename
        print(self.items)
        if not os.path.isfile(self.filename):
            with open(self.filename, 'wb') as file:
                pickle.dump(self.items, file)
        else:
            try:
                with open(self.filename, 'rb') as f:
                    self.items = pickle.load(f)
            except EOFError:
                self.items = deque()

    def isEmpty(self):
        if len(self.items) == 0:
            print("pusto")
        else:
            print("Ne pusto")

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def printQueue(self):
        for i in range(len(self.items)):
            print(self.items[i])

    def saveWork(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.items, f)

    def __del__(self):
        print("Queue deleted ")


#####################################################
class PriorQueue(Queue):  # subclass
    def __init__(self, filename):
        Queue.__init__(self, filename)
        # self.name=name

    def enqueue(self, item):
        if item > 100:
            self.items.append(item)
        else:
            print('no')


#####################################################
class ReverseQueue(Queue):  # subclass
    def __init__(self, filename):
        Queue.__init__(self, filename)
        # self.name=name

    def endDequeue(self):
        return self.items.pop()


#####################################################
q1 = Queue('data.pickle')
q2 = PriorQueue('newFile2')
q3 = ReverseQueue('newFile')


def interface_run(moves: Iterable[Printable]) -> None:
    for move in moves:
        move.printQueue()


interface_run([q1, q2, q3])

######################################################
while True:
    i = int(input())
    if i == 2:
        q1.enqueue(123)
        q1.enqueue(98)
        q1.enqueue(111)
        q2.enqueue(123)
        q2.enqueue(13)
        q2.enqueue(999)
        q3.enqueue(123)
        q3.enqueue(123)
        q3.enqueue(123)

    elif i == 3:
        print("####que1####")
        q1.printQueue()
        print("####que1####")
        print("####que2####")
        q2.printQueue()
        print("####que1####")
        print("####que1####")
        q3.printQueue()
        print("####que1####")
        print("end")
    elif i == 4:
        print(q1.isEmpty())
        print(q2.isEmpty())
        print(q3.isEmpty())
    elif i == 5:
        q1.saveWork()
        q2.saveWork()
        q3.saveWork()
    elif i == 6:
        q1.dequeue()
        q2.dequeue()
        q3.dequeue()
    elif i == 7:
        q3.endDequeue()


    else:
        q1.__del__()
        q2.__del__()
        q3.__del__()
        break
