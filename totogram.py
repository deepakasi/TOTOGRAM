######################Assignment 2###################
#######Implementation of totogram.py#################
####Step1:Find the total number of nodes for the given height,function num_nodes() is implemented to compute this#######
####step2:call on function medians() to compute median and it creates a list which as all the medians#########
####step3:function leveltree() is called to build a balanced binary tree with an exception at level two which has three nodes####
####step4:diff() is called to find the maximum difference in built tree########
####step5:loop is constructed which call the function optimize() to reorders the tree to reduce the maximum difference found so far####
####step6:loop terminates if no more optimization could be made with the tree constructed#######
####Result Analysis######
####k=3 solution obtained 3####
####k=4 solution obtained 5####
####k=5 solution obtained 11####
####k=6 solution obtained 23####
####k=7 solution obtained 47####
###################End################################# 
import statistics
import sys
h=int(sys.argv[1])
maximum=0
class Tree(object): ######tree nodes are of class type TREE######
	def __init__(self,data):
		self.left = None
		self.right = None
		self.middle=None
		self.data = data
def num_nodes(h): ####### Function to return number of nodes for given height######
	sum=0
	pnode=0
	for i in range(1,h+1):
		if i ==1:
			sum=1
		elif i==2:
			sum+=3
			pnode=3
		else:
			sum=sum+(pnode*2)
			pnode=pnode*2
	return sum
temp={}
queue=[]
tnode=Tree(0)
def chunks(l, n):#######find the element for each level of tree######
	n = max(1, n)
	return [l[i:i + n] for i in range(0, len(l), n)]
def medians(mylist,num):
	temp=chunks(mylist,int(len(mylist)/num))
	for i in range(0,num):
		median=int(statistics.median(temp[i]))
		queue.append(median)
		mylist.remove(median)
node=Tree(0)
def leveltree(node):
	for i in range (1,h+1):
		if i==1:
			temp=queue[0:1]
			node=maketree(node,temp,i,0)
			n=1
		elif i==2:
			temp=queue[n:n+3]
			maketree(node,temp,i,0)
			n=n+3
			p=3
		else:
			temp=queue[n:n+p*2]
			maketree(node,temp,i,0)
			n=n+p*2
			p=p*2
	return node
def maketree(self,temp,i,bool):######builds a level balanced binary tree with 3 nodes in second level and two nodes each###### 
	bool=bool+1
	if i==1:
		self=Tree(0)
		self.data=temp.pop(0)
		return self
	else :
		self.left=maketree(self.left,temp,i-1,bool)
		if(bool==1):
			self.middle=maketree(self.middle,temp,i-1,bool)
		self.right=maketree(self.right,temp,i-1,bool)
		return self

a=[]		
def lprintTree(tree,bool):######prints the tree in level based order on finding the result######
		if tree==None:
			return
		if bool==1:
			a.append(tree.data)
		if tree != None:
			lprintTree(tree.left,bool-1)
			if tree.middle != None:
				lprintTree(tree.middle,bool-1)
			lprintTree(tree.right,bool-1)
def diff(self,i,bool):######Function find the difference#######
	global maximum
	global tnode
	bool=bool+1
	if self.left == None and self.right ==None:
		return self
	else :
		l=self.left.data
		self.left=diff(self.left,i-1,bool)
		if(bool==1):
			self.middle=diff(self.middle,i-1,bool)
		r=self.right.data
		self.right=diff(self.right,i-1,bool)
		difference=max(abs(self.data-l),abs(self.data-r))
		if maximum < difference:
			if( self != None):
				tnode=self
				maximum=difference
	return self	
mini=999	
mp=Tree(0)
def min(tnode,parent):######Helper function to reorder the tree,returns the address of parent node having child with minimum value#######
	global mini
	global mp
	if(tnode==None):
		return
	if(mini>tnode.data):
		mini=tnode.data
		mp=parent
	min(tnode.left,tnode)
	min(tnode.right,tnode)
	return mp
mx=-999	
def maxi(tnode,parent):######Helper function to reorder the tree, returns the address of parent node having child with maximum value######
	global mx
	global mp
	if(tnode==None):
		return
	if(mx<tnode.data):
		mx=tnode.data
		mp=parent
	maxi(tnode.left,tnode)
	maxi(tnode.right,tnode)
	return mp		
def optimize(tnode):#######function to optimize the tree returning minimum difference#######
	if(tnode.data+maximum==tnode.right.data):
		temp=min(tnode.right,tnode)
		if(temp.left.data<temp.data):
			t=tnode.right.data
			tnode.right.data=temp.left.data
			temp.left.data=t
		if(temp.right.data<temp.data):
			t=tnode.right.data
			tnode.right.data=temp.right.data
			temp.right.data=t
	if(tnode.data-maximum==tnode.left.data):
		temp=maxi(tnode.left,tnode)
		if(temp.left.data>temp.data):
			t=tnode.left.data
			tnode.left.data=temp.left.data
			temp.left.data=t
		if(temp.right.data>temp.data):
			t=tnode.left.data
			tnode.left.data=temp.right.data
			temp.right.data=t	
mylist=[i for i in range(1,num_nodes(h)+1)]
for height in range(0,h):########call to build the initial tree######
	if height==0:
		medians(mylist,1)
	elif height==1:
		medians(mylist,3)
		parent=3
	elif height >1:
		medians(mylist,parent*2)
		parent=parent*2
node=leveltree(node)
s=diff(node,h,0)
maximum1=999
while(maximum<maximum1):###### optimize tree until minimum difference could be made######
	optimize(tnode)
	if(maximum1>maximum):
		maximum1=maximum
		a=list()
		for i in range(1,h+1):
			lprintTree(node,i)
	maximum=0	
	diff(node,h,0)	
print(maximum)#######returns our result i.e maximum of all the differences in the tree#######
print(a)######3retiurns the level based order of the tree#######

 













