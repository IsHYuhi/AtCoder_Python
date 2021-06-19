import math
from collections import Counter


class UnionFindTree:

    __all__ = ['find_root', 'merge', 'same', 'size']

    def __init__(self, maxsize=10**6):    
        assert (maxsize > 0)

        self._n = maxsize
        self._parent_or_size = [-1]*maxsize
    
    def find_root(self, a):
        '''Find the root of a'''
        assert (0 <= a < self._n)
        
        pos = a
        children = []
        # Follow the path to the root
        while self._parent_or_size[pos] >= 0:
            children.append(pos)
            pos = self._parent_or_size[pos]
        else:
            root_pos = pos
        # Set the parent of child_pos to root_pos
        for child_pos in children:
            self._parent_or_size[child_pos] = root_pos
        return root_pos



    def merge(self, a, b):
        '''Merge the group of a and the group of b'''
        assert (0 <= a < self._n)
        assert (0 <= b < self._n)

        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a == root_b:
            return True
        else:
            # The size of the group of b should be larger 
            if -self._parent_or_size[root_a] > -self._parent_or_size[root_b]:
                root_a, root_b = root_b, root_a
            # Merge the group of a with the group of b
            self._parent_or_size[root_b] += self._parent_or_size[root_a]
            self._parent_or_size[root_a] = root_b
            return False
    
    def same(self, a, b):
        '''See if the group of a and the group of b are the same'''
        assert (0 <= a < self._n)
        assert (0 <= b < self._n)

        root_a = self.find_root(a)
        root_b = self.find_root(b)
        return root_a == root_b
    
    def size(self, a):
        '''Return the size of the group of a'''
        assert (0 <= a < self._n)
        
        root_a = self.find_root(a)
        return -self._parent_or_size[root_a]


n = int(input())
a = list(map(int, input().split()))

N = len(Counter(a))
tree = UnionFindTree()
a_1 = a[:n//2]
a_2 = a[int(math.ceil(n/2)):][::-1]

tmp_a_1 = []
tmp_a_2 = []
S = set()
for i, j in zip(a_1, a_2):

    if i==j:
        continue
    else:
        tmp_a_1.append(i)
        tmp_a_2.append(j)
        S.add(i)
        S.add(j)
        tree.merge(i, j)

ans = 0

S = list(S)
dic = dict()
for s in S:
    r = tree.find_root(s)
    if dic.get(r):
        continue
    else:
        dic[r] = True
        ans += max(1, tree.size(r)-1)

print(ans)


