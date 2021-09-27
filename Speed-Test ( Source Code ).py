#!/usr/bin/python3
# coding: utf-8

try:
	import signal
	from contextlib import contextmanager
except:
	print('Some Deepends not installed!')
else:
	""" Timeout Function """
	@contextmanager
	def timeout(time):
		signal.signal(signal.SIGALRM, raise_timeout)
		signal.alarm(time)
		try:
			yield
		except TimeoutError:
			pass
		finally:
			signal.signal(signal.SIGALRM, signal.SIG_IGN)

	def raise_timeout(signum, frame):
		raise TimeoutError

	""" Check Speed """
	with timeout(1):
		try:
			i = 0
			while True:
				i+=1
		except TimeoutError:
			print('Your computer CPU speed is ' + str(i) + ' i++ per a second.')
			print('Upper number is faster.')
