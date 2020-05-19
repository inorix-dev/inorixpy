import contextlib
import time


@contextlib.contextmanager
def timer(job_name: str = None):
    start = time.time()
    yield
    if job_name is not None:
        print(f"[{job_name}]", end=" ")
    print(f"{time.time() - start} sec")
