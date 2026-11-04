from hypothesis import given, settings
import hypothesis.strategies as st
from mss.models import Monitor

@settings(max_examples=300, deadline=None)
@given(left=st.integers(min_value=-10000, max_value=10000), top=st.integers(min_value=-10000, max_value=10000), width=st.integers(min_value=0, max_value=10000), height=st.integers(min_value=0, max_value=10000))
def test_as_region_never_crashes(left, top, width, height):
    mon = {'left': left, 'top': top, 'width': width, 'height': height}
    region = Monitor.as_region(mon)
    assert region is not None
