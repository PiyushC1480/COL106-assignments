"""ASSIGNMENT 2"""
"""BELOW IS THE IMPLEMENTATION OF THE HEAP BASED ON ARRAL(LIST)."""
class Empty(Exception):# to print errors
    pass
class PriorityQueueBase:# As heaps are based on priority queue so this is the base class 
    class _Item:
        __slots__ = "_key","_value","_index" # the elements stored in heap will have key, value along with the index i.r. position in the array list
        def __init__(self,k,v,inx):
            self._key = k
            self._value = v
            self._index = inx
        
        def __lt__(self,other):# less that equls to operator
            if self._key != other._key:
                return self._key < other._key
            else:
                return self._value<other._value
    def is_empty(self): # check queu is empty
        return len(self) ==0

"""implementation of HEAPQ """
class HeapPriorityQueue(PriorityQueueBase):
    """private methos initialization"""
    def _parent(self,inx):# gives parent of a given index
        return (inx-1)//2
    #TIME COMPLEXXITY: O(1)

    def _left(self,inx): # gives left chile of a given index
        return (2*inx)+1
    ##TIME COMPLEXXITY: O(1)

    def _right(self,inx): # five right child of a given index
        return (2*inx) +2
    #TIME COMPLEXXITY: O(1)
    # below two methods given whether a given index has a left(or right) child or not
    def _has_left(self,inx): 
        return self._left(inx) <len(self._data)
    #TIME COMPLEXXITY: O(1)
    def _has_right(self,inx):
        return self._right(inx) < len(self._data)
    #TIME COMPLEXXITY: O(1)

    # to swap the two values in the heap (used in _upheap) and (_downheap)
    def _swap(self,i,inx):
        self._data[i], self._data[inx] = self._data[inx],self._data[i]# swap the values
        # swap the indices
        self._data[i]._index = i
        self._dict[self._data[i]._value] = self._data[i]._index
        self._data[inx]._index = inx
        self._dict[self._data[inx]._value] = self._data[inx]._index
    #TIME COMPLEXXITY: O(1)
        
    def _upheap(self,j):
        # upheap an element if its key is less that that of its parent
        parent = self._parent(j)
        if j>0  and self._data[j] <self._data[parent]:
            self._swap(j,parent)# swap the two valuies and their indices
            self._upheap(parent)# if still heap is not valid do upheap again
        
    #TIME COMPLEXXITY: O(LOGN)

    def _downheap(self,inx):
        # down heap a given key
        if self._has_left(inx):# check for left child
            left = self._left(inx) # take its value
            small_child = left #make small_chile ot left 
            if self._has_right(inx):
                right = self._right(inx)
                if self._data[right] < self._data[left]:# if right child exits and is smaller than left child then reassign small_chile
                    small_child = right
            if self._data[small_child]<self._data[inx]:# if small_child is bigger that the key at index then perform down heap
                self._swap(inx,small_child)
                self._downheap(small_child)
    #TIME COMPLEXXITY: O(LOGN)
    """publich method initializations"""

    def __init__(self): 
        self._data = []
        self._dict ={}# this dictionary will sore the relation between value and index of a key
    #TIME COMPLEXXITY: O(1) 

    def __len__(self):
        return len(self._data)
    #TIME COMPLEXXITY: O(1)

    def add(self,key,value):# add an element in the heap and assign its correct index 
        self._data.append(self._Item(key,value,len(self._data)))
        self._dict[value] = len(self._data)-1
        self._upheap(len(self._data)-1)
    #TIME COMPLEXXITY: O(LOGN)
    

    def get_dict(self):# to access the dictionar made 
        return self._dict
    #TIME COMPLEXXITY: O(1)

    def min(self):# to find the minimum of the heap i.e. return the very first index 
        if self.is_empty():# if heap is empty then raise the error
            raise Empty("priority queue is empty ")
        item = self._data[0]
        return (item._key,item._value)
    #TIME COMPLEXXITY: O(1)
    
    def remove_min(self):# removing the minimum element from the heap 
        if self.is_empty():
            raise Empty("priority queue is empty")
        self._swap(0,len(self._data)-1)# swap the first and last index 
        self._dict.pop(self._data[-1]._value)# removen the index value pair from dict
        item = self._data.pop()# remove the last emelent
        self._downheap(0)# perform downheap on the top element 
        return (item._key,item._value)# return the key value pair
    #TIME COMPLEXXITY: O(LOGN)
    
    def remove(self,inx): # removing any index from the heap 
        if not (0 <= inx < len(self) ):
            raise ValueError( "Invalid locator" )# key value does not exists
        if inx == len(self) - 1: # if last index is to be pop out then remove its index and value form the heap 
            self._dict.pop(self._data[-1]._value)
            self._data.pop( )
        else:
            self._swap(inx,len(self)-1) 
            self._dict.pop(self._data[-1]._value)
            self._data.pop()
            if inx > 0 and self._data[inx] < self._data[self._parent(inx)]:# perform heapdown / heapup depending on the situation 
                self._upheap(inx)
            else:
                self._downheap(inx)
    #TIME COMPLEXXITY: O(LOGN)
"""all operations in the heap are either O(1) or O(logn)"""


"""below function detects whether given pair of [m,x,v] will collide or not."""
"""if collide then return the time in which they are colliding."""
def helper1(l1,l2): #l1=[m,x,v] l2=[m',x',v'] #(O(1))
    if l1[2]>0 and l2[2]>0 and l1[2] > l2[2]:
        coll_time = abs(l2[1] - l1[1])/ abs(l2[2] - l1[2])
        return (True,coll_time)
    elif l1[2]>0 and l2[2]<0:
        coll_time = abs(l2[1] - l1[1])/ (abs(l2[2]) + l1[2])
        return (True,coll_time)
    elif l1[2] == 0  and l2[2] <0:
        coll_time = abs(l2[1] - l1[1]) / abs(l2[2])
        return (True,coll_time)
    elif l2[2] ==0 and l1[2] >0:
        coll_time = abs(l2[1] - l1[1]) / abs(l1[2])
        return (True,coll_time)
    elif l1[2]<0 and l2[2]<0 and l1[2]>l2[2]:
        coll_time = abs(l2[1] - l1[1])/ (abs(l2[2])-abs(l1[2]))
        return (True,coll_time)
    return (False,None)
    #TIME OMPLEXITY : O(1)


"""defining the main function """
def listCollisions(M,x,v,m,T):
    coll_heap = HeapPriorityQueue()# initialise heap prioirty queue
    i=0
    last_time_when_collide =[0]*(len(M))#stores what was the last time a given index collided
    while i < len(M)-1:# iterate on the given values and from a Heap O(n)
        (a,b) = helper1([M[i],x[i],v[i]],[M[i+1],x[i+1],v[i+1]]) #O(1)check whether they are colliding 
        if a:
            coll_heap.add(b,i) # if yes then add in the heap
        i+=1
    # variables initialisation
    collisions =0
    final_list = []# stores the answer 
    while len(coll_heap) !=0:# iterate ovet the heap
        (t,p) = coll_heap.remove_min()# remove the minimum element
        collisions+=1# increase collision by1  
        if collisions <= m and t<=T:# if collisions are <m and time <t
            # perform the usual colllison calculatoins 
            mass1 = M[p]
            vel1 = v[p]
            mass2 = M[p+1]
            vel2 = v[p+1]
            final_vel1 = (((mass1-mass2)/(mass1+mass2))*vel1) +(((2*mass2)/(mass1+mass2))*vel2)
            final_vel2 = (((mass2-mass1)/(mass1+mass2))*vel2) + (((2*mass1)/(mass1+mass2))*vel1)
            # update the distances
            x[p] +=(vel1 * (t - last_time_when_collide[p]))
            x[p+1] +=(vel2 * (t - last_time_when_collide[p+1]))
            # update the last time when p,p+1 collide
            last_time_when_collide[p] = t
            last_time_when_collide[p+1] = t
            final_list.append((t,p,x[p]))
            # update the final velocities
            v[p] = final_vel1
            v[p+1] = final_vel2
            # since collision at i,i+1 will affect i-1 and i+2 this below blocks solves that issue 
            if p != 0:# ti check for i-1
                temp_1 = x[p-1] + (v[p-1] * (t - last_time_when_collide[p-1]))#temporaily increase the disatnce of i-1
                (is_coll,time_ofcoll) = helper1([M[p-1],temp_1,v[p-1]],[M[p],x[p],v[p]])# check whether they collide
                if is_coll:# if collide then look in heap whether they were earlier colliding or not
                    try:
                        token_dict = coll_heap.get_dict()
                        m1= token_dict[p-1]
                    except KeyError:# if not then simly add
                        coll_heap.add(time_ofcoll+t,p-1)
                    else:# if yes then remove that and add the new time
                        coll_heap.remove(m1)
                        coll_heap.add(time_ofcoll+t,p-1)
            if p < len(M)-2:# siminalr case is done for i+2
                temp_2 = x[p+2] + (v[p+2] * (t-last_time_when_collide[p+2]))#temporaily increase the disatnce of i+2
                (is_coll2,time_ofcoll2) = helper1([M[p+1],x[p+1],v[p+1]],[M[p+2],temp_2,v[p+2]])#check whether they collide
                if is_coll2:#if colliding 
                    try:
                        token_dict = coll_heap.get_dict()
                        m2= token_dict[p+1]
                    except KeyError:# if not then simly add
                        coll_heap.add(time_ofcoll2+t,p+1)
                    else:# if yes then remove that and add the new time
                        coll_heap.remove(m2)
                        coll_heap.add(time_ofcoll2+t,p+1)      
        else:# collisions or time exceed then return final list
            return final_list
    return final_list# if no collision is occuring 
"""time complexity since all operation take O(logn) and max element in the heap can be m so total time complexity is O(n+mlogn)"""