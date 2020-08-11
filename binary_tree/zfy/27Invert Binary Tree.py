class Solution:
    def reverse(self,treenew,treeold):
        if treeold is None:
            return
        if treeold.right is not None:
            treenew.left=TreeNode(treeold.right.val)
        if treeold.left is not None:
            treenew.right=TreeNode(treeold.left.val)
        self.reverse(treenew.left,treeold.right)
        self.reverse(treenew.right,treeold.left)
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        rootnew=TreeNode(root.val)
        self.reverse(rootnew,root)
        return rootnew