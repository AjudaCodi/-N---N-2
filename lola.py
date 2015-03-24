import math
def equation (n, k):
	return ((k +1) - (n%(k +1)), 1 + (n%(k +1)))

"""
|N => |N^2
Idea, n \in [ \frac {k(k+1)}{2}, \frac {(k+1)(k+2)}{2} )

d'aqui treiem la k
"""

def searchK (n):
	return -1 + math.sqrt (1 + 8*n)

def brutusSearchK (n):
	pass


def eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeequation (n, k):
	return (k - n%k, 1 + n%k)


def testing (e = 10):
	d = {}
	k = 1
	for n in xrange (1, e +1):
		t = eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeequation (n, k)
		q = str(t[0]) + ',' + str (t[1])
		if d.has_key (q):
			k += 1
			t = eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeequation (n, k)
			q = str(t[0]) + ',' + str (t[1])
			d[q] = 1
		else:
			t = eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeequation (n, k)
			q = str(t[0]) + ',' + str (t[1])
			d[q] = 1
	return d


def show (e = 10):
	d = testing	(e)
	q = d.keys	()
	q.sort		()
	for i in q:
		print i


class numerable:
	def __init__ (self, a, b):
		self.a = int(a)
		self.b = int(b)

	def inter (self):
		return self.a + self.b

	def __cmp__ (self, e):
		if self.inter ().__cmp__ (e.inter ()):
			return self.inter ().__cmp__ (e.inter ())
		return self.a.__cmp__ (e.a)
	def __str__ (self):
		return str (self.a) + ", " + str(self.b)


def sssssssssssssssssssssssssssssshow (e = 10):
	d = testing		(e)
	q = d.keys		()
	o =			[]
	for r in q:
		a, b = r.split (',')
		o += [numerable	(a, b)]
	o.sort			()
	for i in o:
		print i
