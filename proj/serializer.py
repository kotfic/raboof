import functools
try:
    from . import  transform
except ImportError:
    import transform

from kombu.utils import json as _json

def object_hook(obj):
    try:
        cls  = getattr(transform, obj['_class'])
    except Exception:
        return obj

    return cls.__obj__(obj["__state__"])

def serialize(obj):
    return _json.dumps(obj, check_circular=False)

def deserialize(obj):
    return _json.loads(
        obj, _loads=functools.partial(
            _json.json.loads, object_hook=object_hook))
