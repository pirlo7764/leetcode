class Solution:
    def reverse(self,treenew,treeold):
        if treeold is None:
            return
        treenew.left=TreeNode(treeold.right.val)
        treenew.right=TreeNode(treeold.left.val)
        reverse(treenew.left,treeold.right)
        reverse(treenew.right,treeold.left)
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        rootnew=TreeNode(root.val)
        self.reverse(rootnew,root)
        return rootnew
        