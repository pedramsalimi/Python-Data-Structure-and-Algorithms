import ctype
class DynamicArray(object):

    def __init__(self):

        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):

        return self._n

    def __getitem__(self,k):

        if not 0 <= k < self._n:
            raise IndexError(" K is out of bound! ")
        return self._A[k]

    def append(self,ele):

        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = ele
        self._n += 1

    def _resize(self, c):

        B = self._make_array(c)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c

    def _make_array(self, c):

        return (c * ctype.py_object)()

new_array = DynamicArray()
new_array.__len__()
new_array.append(1)
new_array.__len__()
new_array.append(2)
new_array.__len__()
new_array.append(3)
