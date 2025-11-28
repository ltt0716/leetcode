class MinHeap:
    def __init__(self):
        self.heap=[]

    def __len__(self):
        return len(self.heap)
    def _parent(self,index):
        return (index-1)//2

    def _left_child(self,index):
        return 2*index+1

    def _right_child(self,index):
        return 2*index+2

    def _swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def _sift_up(self,index):
        # 只要当前节点不是根节点，并且比父节点小，就继续上浮
        parent_index=self._parent(index)
        while index>0 and self.heap[parent_index]>self.heap[index]:
            self._swap(index,parent_index)
            index=parent_index
            parent_index=self._parent(index)


    def _sift_down(self,index):

        max_index=len(self.heap)-1



        while self._left_child(index)<=max_index:
            left_child = self._left_child(index)
            right_child = self._right_child(index)

            minest=self.heap[left_child]
            min_index=left_child
            if right_child<=max_index and self.heap[right_child]<minest:
                minest,min_index=self.heap[right_child],right_child

            if minest<self.heap[index]:
                self._swap(index,min_index)
                index=min_index

            else:
                break

    def pop(self):
        if not self.heap:
            raise IndexError("pop from an empty heap")

        if len(self.heap)==1:
            return self.heap.pop()

        minval=self.heap[0]
        self.heap[0]=self.heap.pop()

        self._sift_down(0)

        return minval

    def push(self,num):
        self.heap.append(num)
        self._sift_up(len(self.heap)-1)
    def peek(self):
        if not self.heap:
            raise IndexError("empty heap!")
        return self.heap[0]



# --- 使用我们自己实现的 MinHeap 类 ---
print("\n--- 测试自定义的 MinHeap 类 ---")
my_heap = MinHeap()
my_heap.push(4)
my_heap.push(1)
my_heap.push(7)
my_heap.push(3)
my_heap.push(8)
my_heap.push(5)

print(f"自定义堆的内部列表: {my_heap.heap}")
print(f"堆的大小: {len(my_heap)}")
print(f"最小的元素是: {my_heap.peek()}")

print("\n开始从自定义堆中弹出元素:")
while len(my_heap) > 0:
    smallest = my_heap.pop()
    print(f"弹出的元素: {smallest}, 剩下的堆: {my_heap.heap}")


