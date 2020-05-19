import contextlib
import os


def print_separate():
    width = int(os.popen("stty size", "r").read().split()[1])
    print("-" * width)


@contextlib.contextmanager
def print_separates():
    print_separate()
    yield
    print_separate()
