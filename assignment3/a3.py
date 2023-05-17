"""ASSIGNMENT 3
BASED ON BALANCED BINARY SEARCH TREE"""
class Node:
    """A node in a Range Tree."""
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.assoc = None# associated tree root 
"""BELOW IS THE FUNCTION TO CONSTRUCT THE TREE"""
def tree_construct(data, enable= True):
    # input: data: list of all points
    #        enable : to store w.r.t x or y, (by default by x, hence true)
    if len(data)==0:
        return
    elif len(data)==1:
        node= Node(data[0])
    elif len(data)==2:
        node= Node(data[0])
        node.right = Node(data[1])
        node.right.assoc = node.right
    else:
        mid = (len(data)//2)-1
        node= Node(data[mid])
        node.left= tree_construct(data[0:mid],enable)
        node.right = tree_construct(data[mid +1:],enable)
    if enable:# to make an associated y tree wihe every point in x 
        node.assoc= tree_construct(sorted(data, key=lambda x: x[1]), enable=False)# first sort w.r.t to y and then construct the associaed tree
    return node# return the roor node
    #O(nlogn) cause total element is n and for each element it takes logn time to construct the associated tree.

class PointDatabase:
    def __init__(self,datalist):
        datalist.sort()# O(nlogn)
        root = tree_construct(datalist)#recursively construct the balanced binary tree frim the given point table O(nlogn)
        self.root = root# reference to root 

    def splitnode(self,root,low_cor,high_cor,x_tree):# to find where the split occurs
        # input ,: root-> reference to root
        #        low_cor: minimum possible value of x(or y) in the region
        #        high_cor: maximum possible value of x(or y) in the region 
        #        x_tree: whether to find in x_tree or the y_tree
        split= root# initialize split point to the root 
        # if x_tree then compare node takes x coordinate of the points else: tak y coordinates of the point
        if x_tree:
            while split!=None:
                compare_node = split.value
                if high_cor< compare_node[0]:
                    split= split.left
                elif low_cor>compare_node[0]:
                    split = split.right
                elif low_cor<=compare_node[0]<=high_cor:
                    break
            return split
        else:
            while split!=None:
                compare_node = split.value
                if high_cor< compare_node[1]:
                    split= split.left
                elif low_cor>compare_node[1]:
                    split = split.right
                elif low_cor<=compare_node[1]<=high_cor:
                    break
            return split


    def Searchin1d(self,root, low, high,x_tree):# to search for points either in x_tree or the associated y_tree
        nodes = []
        sn =self.splitnode(root,low,high,x_tree)# find splitnode
        if sn==None:# if none r=then there are no points 
            return nodes
        if x_tree:# either to search in x_tree
            val= sn.value
            if low<=val[0]<=high:# if pount  lies in the range then append it into the node list
                nodes.append(sn.value)
            nodes+= self.Searchin1d(sn.left,low,high,x_tree) # check the lefr and right child and add it into the nodes list
            nodes += self.Searchin1d(sn.right,low,high,x_tree)
        else:# or in associated y_tree
            val= sn.value
            if low<=val[1]<=high:
                nodes.append(sn.value)
            nodes+= self.Searchin1d(sn.left,low,high,x_tree)
            nodes += self.Searchin1d(sn.right,low,high,x_tree)
        return nodes


    def searchNearby(self,q,d):
        low_x= q[0]-d# minimum value of x coordinate
        low_y = q[1]-d # minimum value of y coordinate
        high_x = q[0]+d # maximum value of x coordinate
        high_y = q[1]+d # maximum value of high coordinate
        nodes = []# final list 
        splt = self.splitnode(self.root,low_x,high_x,True)# finf the split node in the x_tree
        if splt == None:# if no splitnode then ther eis no point hence retunr the empty list 
            return nodes
        h = splt.value
        if low_x<=h[0]<=high_x and low_y<=h[1]<=high_y:
            nodes.append(h) # if the node split point lies in the region then append it 
        lc = splt.left # take the left child 
        while lc!=None:
                h2 = lc.value
                if low_x<=h2[0]<=high_x and low_y<=h2[1]<=high_y:# f=if left child lies in the region 
                    nodes.append(h2)
                if low_x <= h2[0]:# if in x_tree the left chold has bigger x-coordinate then the minimum x
                    if lc.right !=None:# then in y_tree associated wiht the right child of lc search for the possible points 
                        nodes+= self.Searchin1d(lc.right.assoc,low_y,high_y,False)
                    lc= lc.left# move to left child of the lc
                else:# if in x_tree the left chold has smaller x-coordinate then the minimum x them move to the right child of lc
                    lc = lc.right
        rc = splt.right # repeat the same procedure on rc of splitnode
        while rc!=None :
                h3 = rc.value
                if low_x<=h3[0]<=high_x and low_y<=h3[1]<=high_y:
                    nodes.append(h3)
                if h3[0]<= high_x:
                    if rc.left !=None:
                        nodes+= self.Searchin1d(rc.left.assoc,low_y,high_y,False)
                    rc= rc.right
                else:
                    rc = rc.left
        return sorted(nodes)
"""TIME COMPLEXITY:
__init__: takes O(nlogn) time.
searchnearby take O(m+(logn)**2) as we are moving down from the splitnode from eithrt side of subtree rooted at splitnode and searchin1d takes O(n+logn)time
total time complexity is O(m+h+logn+log**2(n))==> O(m+log**2(n)) """