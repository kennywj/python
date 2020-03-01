# -*- coding: utf-8 -*-
import threading
import time
from threading import Timer

# be submodule of Timer class
class RepeatTimer(Timer):
	def run(self):
		while not self.finished.wait(self.interval):
			self.function(*self.args, **self.kwargs)
