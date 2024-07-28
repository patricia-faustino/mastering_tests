import time
from src.performance_function.long_running import long_running

def test_long_running():
    start = time.time()
    long_running()
    end = time.time()
    duration = int(end - start)
    assert duration == 2, f"Expected 2, but got {duration}"