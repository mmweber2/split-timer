import time
from timer import Run
from nose.tools import assert_equals
from nose.tools import assert_almost_equal
from nose.tools import assert_less
from nose.tools import assert_less_equal

def test_create_run():
    t = Run()
    assert_equals(t.overall_time, 0)
    assert_equals(t.event_times, [])
    assert_equals(t.current_event_id, 0)
    assert_less_equal(t.run_start_time, time.time())
    assert_equals(t.event_start_time, t.run_start_time)

def test_single_event_run():
    t = Run()
    time.sleep(1)
    run_time = t.stop()
    assert_almost_equal(run_time, 1.0, places=2)
    assert_equals(len(t.event_times), 1)
    assert_almost_equal(t.event_times[0], 1.0, places=2)
    assert_less(t.run_start_time, time.time())