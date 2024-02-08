#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
	from __builtin__ import xrange as range
	from future_builtins import ascii, filter, hex, map, oct, zip


def main():
	sys.setrecursionlimit(10000)

	n, m = map(int, input().split())
	p = []

	for _ in range(n):
		p.append(list(map(int, input().split())))
	
	x, y, c, t = map(int, input().split())
	colored = []

	def check(i, j, ii, jj):
		tt = []
		o = p[i][j]

		if i > 0 and abs(o-p[i-1][j]) <= t and [i-1, j] != [ii, jj] and [i-1, j] not in colored:
			tt.append([i-1, j])
		if i < n-1 and abs(o-p[i+1][j]) <= t and [i+1, j] != [ii, jj] and [i+1, j] not in colored:
			tt.append([i+1, j])
		if j > 0 and abs(o-p[i][j-1]) <= t and [i, j-1] != [ii, jj] and [i, j-1] not in colored:
			tt.append([i, j-1])
		if j < m-1 and abs(o-p[i][j+1]) <= t and [i, j+1] != [ii, jj] and [i, j+1] not in colored:
			tt.append([i, j+1])

		p[i][j] = c
		colored.append([i, j])
		
		for v in tt:
			check(v[0], v[1], i, j)

	check(x-1, y-1, None, None)

	for l in p:
		print(*l)



# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
	newlines = 0

	def __init__(self, file):
		self._fd = file.fileno()
		self.buffer = BytesIO()
		self.writable = "x" in file.mode or "r" not in file.mode
		self.write = self.buffer.write if self.writable else None

	def read(self):
		while True:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			if not b:
				break
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines = 0
		return self.buffer.read()

	def readline(self):
		while self.newlines == 0:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			self.newlines = b.count(b"\n") + (not b)
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines -= 1
		return self.buffer.readline()

	def flush(self):
		if self.writable:
			os.write(self._fd, self.buffer.getvalue())
			self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
	def __init__(self, file):
		self.buffer = FastIO(file)
		self.flush = self.buffer.flush
		self.writable = self.buffer.writable
		self.write = lambda s: self.buffer.write(s.encode("ascii"))
		self.read = lambda: self.buffer.read().decode("ascii")
		self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
	"""Prints the values to a stream, or to sys.stdout by default."""
	sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
	at_start = True
	for x in args:
		if not at_start:
			file.write(sep)
		file.write(str(x))
		at_start = False
	file.write(kwargs.pop("end", "\n"))
	if kwargs.pop("flush", False):
		file.flush()


if sys.version_info[0] < 3:
	sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
	sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
	main()
