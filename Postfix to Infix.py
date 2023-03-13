# -------------------------------------
# Author : Phoomtep Pitakamnuay
# ID : 1-63-07-0489-6
# SECTION : 227E
# DATE : 11/2/2021
# LAB NUMBER : 4
# -------------------------------------
class Node:
    def __init__(self, ch=None) :
        self.ch = ch
        self.left = None
        self.right = None

def createTree(data, pointer):
    if len(data) > 1:
        if not data[pointer].ch.isdigit():
            data[pointer].left = data[pointer-2]
            data[pointer].right = data[pointer-1]
            data[pointer-2] = data[pointer]
            print('(',data[pointer-2].left.ch,data[pointer-2].ch,data[pointer-2].right.ch,')')
            pointer = pointer-1
            data.pop(pointer)
            data.pop(pointer)
            return createTree(data, pointer)
        else:
            return createTree(data, pointer+1)

    return data

def printTreeInOrder(cur):
    if cur is None:
        return

    if not cur.ch.isdigit():
        print('(', end=' ')
 
    printTreeInOrder(cur.left)
    print(cur.ch, end=' ')
    printTreeInOrder(cur.right)
 
    if not cur.ch.isdigit():
        print(')', end=' ')

postFix = ['2','3','5','+','*','9','2','/','-','8','4','%','^']

arrayOfPointer = []
for item in postFix:
    arrayOfPointer.append(Node(item))

print(" Create tree log ".center(60,"-"))
tree = createTree(arrayOfPointer, 0)
print("-"*60)
print("InOrder:", end=' ')
cur = tree[0]
printTreeInOrder(cur)