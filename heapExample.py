"""http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html#the-structure-property"""

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
       while (i * 2) <= self.currentSize:
        mc = self.minChild(i)
        if self.heapList[i] > self.heapList[mc]:
            tmp = self.heapList[i]
            self.heapList[i] = self.heapList[mc]
            self.heapList[mc] = tmp
        i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        return self.currentSize == 1

    def findMin(self):
        result = None
        if not self.isEmpty:
            result = self.heapList[1]
        
        return result    

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        
        while (i > 0):
            self.percDown(i)
            i = i - 1


import random
if __name__ == '__main__':
    h = BinHeap()
    
    options = [0, 1, 2]
    p = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]
    np = [11, 12, 13, 14, 15, 16, 17, 18, 20]

    while len(p) > 0 or len(np) > 0 or h.currentSize > 0:
        random.shuffle(options)
        option = options[0]

        if option == 0:
            if len(p) > 0:
                i = p.pop(0)
                h.insert(i)
                print('Prioritário {0} entrou na fila'.format(i))
        elif option == 1:
            if len(np) > 0:
                i = np.pop(0)
                h.insert(i)
                print('Não prioritário {0} entrou na fila'.format(i))
        else:
            if h.currentSize > 0:
                i = h.delMin()
                print('Atendendo {0}'.format(i))

