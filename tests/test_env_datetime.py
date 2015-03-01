import os
import pytest
import time
import datetime


from excavator import env_datetime

try:
    import iso8601  # NOQA
    iso8601_available = True
except ImportError:
    iso8601_available = False


def to_timestamp(when):
    return time.mktime(when.utctimetuple()) + when.microsecond / 1e6


def assert_datetimes_almost_equal(w1, w2, delta=datetime.timedelta(microseconds=1)):
    assert abs(w1.replace(tzinfo=None) - w2.replace(tzinfo=None)) <= delta


def test_sanity_check_to_timestamp():
    """
    Sanity check that the from_timestamp helper works as expected
    """
    when_in = datetime.datetime.now()
    timestamp = to_timestamp(when_in)
    when_out = datetime.datetime.fromtimestamp(timestamp)

    assert_datetimes_almost_equal(when_in, when_out)


def test_sanity_check_to_utc_timestamp():
    """
    Sanity check that the from_timestamp helper works as expected
    """
    when_in = datetime.datetime.utcnow()
    timestamp = to_timestamp(when_in)
    when_out = datetime.datetime.fromtimestamp(timestamp)

    assert_datetimes_almost_equal(when_in, when_out)


def test_env_datetime_required_and_default_are_mutually_exclusive():
    """
    test the mutual exclusivity of the `required` and `default` keywords
    """
    assert 'TEST_DATETIME_ENV_VARIABLE' not in os.environ

    with pytest.raises(ValueError):
        env_datetime('TEST_DATETIME_ENV_VARIABLE', required=True, default='some-default')


def test_with_no_default():
    assert 'TEST_DATETIME_ENV_VARIABLE' not in os.environ

    with pytest.raises(ValueError):
        env_datetime('TEST_DATETIME_ENV_VARIABLE')


def test_with_unknown_format(monkeypatch):
    monkeypatch.setenv(
        'TEST_DATETIME_ENV_VARIABLE', str(to_timestamp(datetime.datetime.now())),
    )

    with pytest.raises(KeyError):
        env_datetime('TEST_DATETIME_ENV_VARIABLE', fmt='unknown-format')


#
# timestamp tests
#
def test_with_plain_timestamp(monkeypatch):
    when_in = datetime.datetime.now()
    timestamp = to_timestamp(when_in)

    monkeypatch.setenv(
        'TEST_DATETIME_ENV_VARIABLE', repr(timestamp),
    )

    when_out = env_datetime('TEST_DATETIME_ENV_VARIABLE', fmt='timestamp')

    assert_datetimes_almost_equal(when_in, when_out)


def test_with_utc_timestamp(monkeypatch):
    when_in = datetime.datetime.utcnow()
    timestamp = to_timestamp(when_in)

    monkeypatch.setenv(
        'TEST_DATETIME_ENV_VARIABLE', repr(timestamp),
    )

    when_out = env_datetime('TEST_DATETIME_ENV_VARIABLE', fmt='timestamp')

    assert_datetimes_almost_equal(when_in, when_out)


#
# iso8601 tests
#
@pytest.mark.skipif(iso8601_available, reason="iso8601 available")
def test_iso8601_with_library_not_installed(monkeypatch):
    when_in = datetime.datetime.utcnow()

    monkeypatch.setenv(
        'TEST_DATETIME_ENV_VARIABLE', when_in.isoformat(),
    )

    with pytest.raises(ImportError):
        env_datetime('TEST_DATETIME_ENV_VARIABLE', fmt='iso8601')


@pytest.mark.skipif(not iso8601_available, reason="iso8601 not available")
def test_iso8601_parsing(monkeypatch):
    when_in = datetime.datetime.utcnow()

    monkeypatch.setenv(
        'TEST_DATETIME_ENV_VARIABLE', when_in.isoformat(),
    )

    when_out = env_datetime('TEST_DATETIME_ENV_VARIABLE', fmt='iso8601')

    assert_datetimes_almost_equal(when_in, when_out)
