import multiprocessing
import ctypes


class AtomicCounter:
    """An atomic, thread-safe incrementing counter.
    >>> ctx = multiprocessing.get_context()
    >>> counter = AtomicCounter()
    >>> counter.increment()
    1
    >>> counter.increment(4)
    5
    >>> counter = AtomicCounter(initial=42)
    >>> counter.value
    42
    >>> counter.increment(1)
    43
    >>> counter = AtomicCounter()
    >>> def incrementor():
    ...     for i in range(100000):
    ...         counter.increment()
    >>> p_arr = []
    >>> for i in range(4):
    ...     p = ctx.Process(target=incrementor)
    ...     p.start()
    ...     p_arr.append(p)
    >>> for p in p_arr:
    ...     p.join()
    >>> counter.value
    400000
    """

    def __init__(self, ctx=multiprocessing, initial=0):
        """Initialize a new atomic counter to given initial value (default 0)."""
        self._counter = ctx.Value(ctypes.c_int)
        self.value = initial

    @property
    def value(self):
        return self._counter.value

    @value.setter
    def value(self, val):
        with self._counter.get_lock():
            self._counter.value = val

    def increment(self, num=1):
        """Atomically increment the counter by num (default 1) and return the
        new value.
        """
        with self._counter.get_lock():
            self._counter.value += num
            return self._counter.value

    def reset(self):
        self.value = 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
