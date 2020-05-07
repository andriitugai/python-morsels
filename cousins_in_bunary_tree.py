#
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values,
# and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
#
# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root.val == x or root.val == y:
            return False

        def search_treenode_for_val(tree, val, level):
            '''returns level and the value of the parent of the node'''
            if tree is None or tree.val is None:
                return None, None

            if (tree.left is not None and tree.left.val == val) or \
                (tree.right is not None and tree.right.val == val):
                return level, tree.val
            else:
                # search left
                lvl, pvl = search_treenode_for_val(tree.left, val, level + 1)
                if lvl is None and pvl is None:
                    lvl, pvl = search_treenode_for_val(tree.right, val, level + 1)
                return lvl, pvl

        xlvl, xpvl = search_treenode_for_val(root, x, 0)
        ylvl, ypvl = search_treenode_for_val(root, y, 0)

        if xlvl == ylvl and xpvl != ypvl:
            return True

        return False