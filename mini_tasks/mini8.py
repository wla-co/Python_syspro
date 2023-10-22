import functools


def deprecated(fun=None, *, since=None, removed_in=None):
    if fun is None:
        return functools.partial(deprecated, since=since, removed_in=removed_in)

    @functools.wraps(fun)
    def inner(*args, **kwargs):
        print(f'Warning: function {fun.__name__} is deprecated{"" if since is None else f" since version {since}"}. '
              f'It will be removed in {"future versions" if removed_in is None else f"version {removed_in}"}.')
        return fun(*args, **kwargs)

    return inner


@deprecated
def foo():
    print("Hello from foo")


@deprecated(since='1.0.2')
def bar():
    print("Hello from bar")


@deprecated(since='10.2.33', removed_in='10.3.0')
def buzz():
    print("Hello from buzz")


foo()
bar()
buzz()
