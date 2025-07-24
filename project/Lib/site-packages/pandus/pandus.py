import pandas as _pandas

__all__ = []
for name in dir(_pandas):
    if name.startswith('_'):
        continue
    obj = getattr(_pandas, name)
    globals()[name] = obj
    __all__.append(name)

del _pandas


