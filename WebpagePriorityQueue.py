import re


class WebpagePriorityQueue:
    def __init__(self, webpageidxs, query=''):
        self.webpageidxs = webpageidxs
        self.query = query
        self.size = 0
        self.queue = [self.getPriority(wp) for wp in self.webpageidxs]
        self.shiftDown(self.queue, 0)

    def getPriority(self, webpageindex):
        """
        Find the priority of a word based on the sum of the frequency of the words in the query
        :param webpageindex:
        :return:
        """
        words = re.sub("[^\w' ]", '', self.query).split()
        s = sum([webpageindex.getCount(word) for word in words])
        return [s, webpageindex]

    def peek(self):
        """
        return the top of the queue
        :return:
        """
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0][1]

    def poll(self):
        """
        Remove and return the top of the queue
        :return:
        """
        if len(self.queue) == 0:
            return None
        else:
            highest_pri = self.queue[0][1]

            # length of queue is 1. Delete node
            if len(self.queue) == 1:
                del self.queue[0]
                return highest_pri
            else:

                # Swap bottom left most node and reheap.
                self.queue[0] = self.queue[-1]
                del self.queue[-1]
                self.shiftDown(self.queue, 0)

        return highest_pri

    def shiftUp(self, q, idx):
        """
        Traverse up a queue and keep it in order.
        :param q:
        :param idx:
        :return:
        """
        parent_idx = (idx-1)//2

        # Reached the end of the heap
        if parent_idx < 0:
            return

        # Traverse up the tree and swap if child is bigger than parent.
        if q[idx][0] > q[parent_idx][0]:
            self.swap(q[parent_idx], q[idx])
            self.shiftDown(q, parent_idx)


    def reheap(self, newquery):
        """
        Find the new priorities of the queue and reorder.
        :param newquery:
        :return:
        """
        self.query = newquery
        if self.queue is not None:

            # Find new priorities
            self.queue = [self.getPriority(wp) for wp in self.webpageidxs]

            # Reheap the queue
            self.shiftUp(self.queue, len(self.queue) - 1)

    def shiftDown(self, q, idx):
        """
        Reheap the queue from top to bottom to keep it in order.
        :param q:
        :param idx:
        :return:
        """

        # Find current node and children
        current = q[idx]
        leftChild = self.getLeftChild(idx)
        rightChild = self.getRightChild(idx)

        # Reached the end of the queue
        if idx >= len(q):
            return

        else:
            # Left child has higher priority than right
            if q[leftChild][0] > q[rightChild][0]:
                self.swap(current, q[leftChild])

            # Right child has higher priority than left
            else:
                self.swap(current, q[rightChild])
            self.shiftDown(q, idx + 1)


    def getLeftChild(self, curr):
        """
        Find the left child of a node
        :param curr:
        :return:
        """
        return self.queue[2*curr + 1]

    def getRightChild(self, curr):
        """
        Find the right child of a node
        :param curr:
        :return:
        """
        return self.queue[2*curr + 2]

    def parent(self, curr):
        """
        Find the parent of a node
        :param curr:
        :return:
        """
        return self.queue[(curr-1)//2]

    def swap(self, k, l):
        """
        Swap two nodes.
        :param k:
        :param l:
        :return:
        """
        self.queue[k], self.queue[l] = self.queue[l], self.queue[k]


