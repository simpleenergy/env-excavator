import os
import datetime


class empty(object):
    pass


def get_env_value(name, default=empty, required=False):
    """
    Core function for extracting the environment variable.

    Enforces mutual exclusivity between `required` and `default` keywords.

    The `empty` sentinal value is used as the default `default` value to allow
    other function to handle default/empty logic in the appropriate way.
    """
    if required and default is not empty:
        raise ValueError("Using `default` with `required=True` is invalid")
    elif required:
        try:
            value = os.environ[name]
        except KeyError:
            raise KeyError(
                "Must set environment variable {0}".format(name)
            )
    else:
        value = os.environ.get(name, default)
    return value


def env_string(name, default=empty, required=False):
    """
    Get a string from the environment, defaulting to `default` if it is not
    there and not required.
    """
    value = get_env_value(name, default=default, required=required)
    if value is empty:
        value = ''
    return value


TRUE_VALUES = set((
    True,
    'True',
    'true',
))


def env_bool(name, truthy_values=TRUE_VALUES, required=False, default=empty):
    """
    Return a boolean value derived from an environmental variable.  This is
    done via string comparison (Or if the value is `True`).
    """
    value = get_env_value(name, required=required, default=default)
    if value is empty:
        return None
    return value in TRUE_VALUES


def env_list(name, separator=',', required=False, default=empty):
    """
    Return a list of items derived from an environmental variable.  This is
    done by splitting the string value from the environment on a given
    separator.
    """
    value = get_env_value(name, required=required, default=default)
    if value is empty:
        return []
    # wrapped in list to force evaluation in python 3
    return list(filter(bool, [v.strip() for v in value.split(separator)]))


def env_int(name, required=False, default=empty):
    """
    Return an integer derived from an environmental variable.  In the case
    where no default is specified and the variable is not present in the
    environment, a `TypeError` will be raised since we don't want to guess
    about a sensible default.
    """
    value = get_env_value(name, required=required, default=default)
    if value is empty:
        raise ValueError(
            "`env_int` requires either a default value to be specified, or for "
            "the variable to be present in the environment"
        )
    return int(value)


def env_timestamp(name, default=empty, required=False):
    if required and default is not empty:
        raise ValueError("Using `default` with `required=True` is invalid")

    value = get_env_value(name, required=required, default=empty)
    # change datetime.datetime to time, return time.struct_time type
    if default is not empty and value is empty:
        return default
    if value is empty:
        raise ValueError(
            "`env_timestamp` requires either a default value to be specified, or "
            "for the variable to be present in the environment"
        )

    timestamp = float(value)
    return datetime.datetime.fromtimestamp(timestamp)


def env_iso8601(name, default=empty, required=False):
    try:
        import iso8601
    except ImportError:
        raise ImportError(
            'Parsing iso8601 datetime strings requires the iso8601 library'
        )

    if required and default is not empty:
        raise ValueError("Using `default` with `required=True` is invalid")

    value = get_env_value(name, required=required, default=empty)
    # change datetime.datetime to time, return time.struct_time type
    if default is not empty and value is empty:
        return default
    if value is empty:
        raise ValueError(
            "`env_iso8601` requires either a default value to be specified, or "
            "for the variable to be present in the environment"
        )
    return iso8601.parse_date(value)
