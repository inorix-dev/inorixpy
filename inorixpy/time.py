import contextlib
import datetime as dt
import time


def now(fmt: str = r"%y%m%d%H%M%S") -> str:
    now = dt.datetime.now()
    return now.strftime(fmt)


@contextlib.contextmanager
def timer(job_name: str = None):
    start = time.time()
    yield
    if job_name is not None:
        print(f"[{job_name}]", end=" ")
    print(f"{time.time() - start} sec")
