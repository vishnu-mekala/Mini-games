s = {1,2,3,4,5,6}
ss = {3,4,5,6,7,8,0}
s - ss
{1, 2}
ss - s
{0, 8, 7}
s.difference(ss)
{1, 2}
ss.difference_update(s)
ss
{0, 7, 8}
s
{1, 2, 3, 4, 5, 6}
ss
{0, 7, 8}
s.difference_update(ss)
s
{1, 2, 3, 4, 5, 6}
ss
{0, 7, 8}
s.discard(2)
s
{1, 3, 4, 5, 6}
l.remove(3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.remove(3)
NameError: name 'l' is not defined
l.remove(l)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l.remove(l)
NameError: name 'l' is not defined
l = s.copy()
l
{1, 3, 4, 5, 6}
l.remove(1)
l
{3, 4, 5, 6}
l.remove(1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l.remove(1)
KeyError: 1
s.discard(1)
s.intersection(ss)
set()
ss
{0, 7, 8}
s
{3, 4, 5, 6}
s.update(ss)
s
{0, 3, 4, 5, 6, 7, 8}
ss.intersection_update(s)
ss
{0, 8, 7}
s
{0, 3, 4, 5, 6, 7, 8}
s.union(ss)
{0, 3, 4, 5, 6, 7, 8}

s.pop()
0
s
{3, 4, 5, 6, 7, 8}
ss
{0, 8, 7}
ss.pop()
0
ss
{8, 7}
s
{3, 4, 5, 6, 7, 8}
s = {1,2,3,4,5,6}
s.isdisjoint(ss)
True
s.isdisjoint(ss-s)
True
s.issubset(s.intersection(ss))
False
s.intersection(ss).issubset(s)
True
s.issuperset(s.intersection(ss))
True
