from typing import *

class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		check = True
		str = list(s)
		for c in str:
			if c == "[" or c == "{" or c == "(":
				stack.append(c)
			elif c == "]" or c == "}" or c == ")":
				if stack:
					tmp = stack.pop()
				else:
					check = False
					break
				if c == "]" and tmp != "[":
					check = False
					break
				if c == "}" and tmp != "{":
					check = False
					break
				if c == ")" and tmp != "(":
					check = False
					break
		if stack:
			check = False
		return check