# timing.py
import time
from typing import Any

class ExecutionTime:
  def __init__(self, func):
    self.func = func
  def __call__(self, *args, **kwds):
    start = time.perf_counter()
    result = self.func(*args, **kwds)
    end = time.perf_counter()
    print(f"{self.func.__name__}() took{end - start * 1000:.4f} ms")
    return result
  