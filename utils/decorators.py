# -*- coding: utf-8 -*-


def get_original_docstring(func):
    def wrapper(target):
        target.__doc__ = func.__doc__
        return target
    return wrapper
