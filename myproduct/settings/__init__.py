from .local import *
try:
    from .base import *
except:
    pass

try:
    from .allauth import *
except:
    pass