"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a
node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def getTargetCopy(original, cloned, target):
    def gen(node):
        if node:
            yield node
            yield from gen(node.left)
            yield from gen(node.right)

    for n1, n2 in zip(gen(original), gen(cloned)):
        if n1 == target:
            return n2
