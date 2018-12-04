from pkgutil import iter_modules
from importlib import import_module

_cpu_modules = [
    name for _, name, ispkg in iter_modules(__path__) if not ispkg
]

for c in _cpu_modules:
    try:
        import_module("." + c, package=__package__)
    except Exception as e:
        # Failed to import a CPU model due to a missing
        # dependency. This typically happens if gem5 has been compiled
        # without a CPU model needed by the timing model.
        #print("name error on import")
        #print(e)
        pass
#print(_cpu_modules)
__all__ = _cpu_modules
