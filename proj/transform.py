from kombu.exceptions import DecodeError

class BaseTransform(object):
    __state__ = {}

    @classmethod
    def __obj__(cls, state):
        return cls(*state.get("args", []),
                   **state.get("kwargs", {}))

    def __json__(self):
        return {"_class": self.__class__.__name__,
                "__state__": self.__state__}

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__state__['args'] = args
        obj.__state__['kwargs'] = kwargs
        return obj



class Reverse(BaseTransform):
    def __init__(self, value):
        self.value = value

    def transform(self):
        return self.value[::-1]

class Capitalize(BaseTransform):
    def __init__(self, value):
        self.value = value

    def transform(self):
        return self.value.upper()


class RaiseException(BaseTransform):

    def transform(self):
        raise DecodeError("Some kind of Error")
