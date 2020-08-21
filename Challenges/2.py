# 2. Add Two Numbers

class two_num(object):
	def to_num(self, n1):
		n1 = 0
		mul = 1
		while n1 != None:
			n1 = n1.val * mul + n1
			mul *= 10
			n1 = n1.next
		return n1

	def addNum(self, n1, n2):
		return map(int, str(self.to_num(n1) + self.to_num(n2))[::-1])


     