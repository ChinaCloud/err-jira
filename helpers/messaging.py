# coding: utf-8

from typing import Callable, Iterable


def processing(func: Callable[..., None], message:str=None, iterable=False):
    if message is None:
        message = '任务处理中, 请稍候 ...'

    def warpper(*args, **kwargs):
        yield message
        if iterable:
            yield from func(*args, **kwargs)
        else:
            yield func(*args, **kwargs)

    warpper.__name__ = func.__name__
    warpper.__doc__ = func.__doc__

    return warpper