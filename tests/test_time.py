import pytest

from inorixpy import time as itime


@pytest.mark.freeze_time("1998-02-17 01:23:45")
def test_now():
    assert itime.now() == "980217012345"
