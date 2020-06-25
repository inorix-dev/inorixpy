import contextlib
import os

from tqdm import tqdm


def print_separate():
    width = int(os.popen("stty size", "r").read().split()[1])
    print("-" * width)


@contextlib.contextmanager
def print_separates():
    print_separate()
    yield
    print_separate()


def tqdm_print(*values, sep=" ", end="\n", file=None, nolock=False):
    s = sep.join([str(v) for v in values])
    tqdm.write(s, end=end, file=file, nolock=nolock)
