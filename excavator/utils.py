import os


def env_string(name, default='', required=False):
    """
    Get a string from the environment, defaulting to `default` if it is not
    there and not required.
    """
    if required and default:
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


TRUE_VALUES = set((
    True,
    'True',
    'true',
))


def env_bool(name, truthy_values=TRUE_VALUES, required=False, default=None):
    """
    Return a boolean value derived from an environmental variable.  This is
    done via string comparison (Or if the value is `True`).
    """
    env_value = env_string(name, required=required, default=default)
    return env_value in TRUE_VALUES


def env_list(name, separator=',', required=False, default=''):
    """
    Return a list of items derived from an environmental variable.  This is
    done by splitting the string value from the environment on a given
    separator.
    """
    value = env_string(name, required=required, default=default)
    return [v.strip() for v in value.split(separator)]
