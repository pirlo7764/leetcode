class Solution:
    def check(self,a,b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val!=b.val:
            return False
        if a.val==b.val:
            return self.check(a.left,b.right) and self.check(a.right,b.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.check(root.left,root.right)