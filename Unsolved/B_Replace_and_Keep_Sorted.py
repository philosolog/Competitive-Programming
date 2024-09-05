#!/usr/bin/env python
from __future__ import division, print_function
import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
	from __builtin__ import xrange as range
	from future_builtins import ascii, filter, hex, map, oct, zip

def main():
	n, q, k = map(int, input().split())
	nl = list(map(int, input().split()))
	bl = []
	tl = []

	for i, v in enumerate(nl):
		b = None
		t = None

		if i == 0:
			b = 0
		else:
			b = nl[i-1]
		if i == n-1:
			t = k # !: Could be negative
		else:
			t = min(k, nl[i+1])
		
		bl.append(b)
		tl.append(t)
	for _ in range(q):
		l, r = map(int, input().split())
		a = 0

		for i in range(l-1, r):
			b = bl[i]
			t = tl[i]

			if i == l-1:
				b = 0
			if i == r-1:
				t = k

			a += max(0, t-b-(b<nl[i]<t))

		print(a)
		



		

# region fastio
BUFSIZE = 8192

class FastIO(IOBase):
	newlines = 0

	def __init__(self, file):
		self._file = file
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