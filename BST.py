class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.val)

def preorder(root):
	if root:
		print(root.val)
		preorder(root.left)
		preorder(root.right)


# Tree traversal ROOT
# i.e {30, 43, 13, 8, 50, 40, 20, 19, 22}
x = Node(5) # Provide NODE - ROOT counts as #1
x = insert(x, 3) #2
x = insert(x, 1) #3
x = insert(x, 4) #4
x = insert(x, 7) #5
x = insert(x, 6) #6
x = insert(x, 9) #7
# x = insert(x, 19) #8
# x = insert(x, 22) #9
#			      #etc...

print('(a) Inorder (Left, Root, Right)')
inorder(x)
print('\n(c) Post-order (Left, Right, Root)')
postorder(x)
print('\n(b) Pre-order (Root, Left, Right)')
preorder(x)


# BOILERPLATE 
if __name__ == "__main__":
	BSTmain = Node(0)
	print(f'\nAUTHOR: Jan Kupczyk')
	print(f'https://github.com/jankupczyk\n')