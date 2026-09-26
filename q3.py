from typing import Optional


class TreeNode:
    """Binary tree node for the org chart."""
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right
    


def count_fair_managers(root: Optional[TreeNode]) -> int:
    """
    Problem 3: Fair managers in an org chart.

    Given the root of a binary tree where each node has a `salary`,
    count the number of nodes whose salary equals the floor-division
    average salary of their entire subtree (including themselves).

    Args:
        root: root TreeNode of the org chart (or None for empty chart).

    Returns:
        Number of fair managers in the tree.
    """
    count=0
    div=0
    sum=0
    def subtreecheck(node1=root):
        if not node1:
            return 0,0
        nonlocal count
        lcount,lsum=subtreecheck(node1.left)
        rcount,rsum=subtreecheck(node1.right)

        totalsum=lsum+rsum+node1.salary
        totalcount=lcount+rcount+1
        if node1.salary==totalsum//totalcount:
             count+=1
        return totalcount,totalsum

    subtreecheck(root)
    return count



pass


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    # root = [1] -> a single employee is trivially a fair manager
    root = TreeNode(1)
    print(count_fair_managers(root))  # expected: 1
