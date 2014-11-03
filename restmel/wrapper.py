from maya import cmds
from maya import utils


class Wrapper(object):
    """Make thread-safe calls to maya.cmds

    Description
        Maya can't deal with commands coming in from threads other
        than main. This wrapper takes whatever we call and wrap it up
        using maya.utils.executeInMainThreadWithResult()

    How
        maya.utils.execu... has an argument signature that
        looks like this: (command, *args, **kwargs)

        Wrapper then intercepts any attribute-queries and wraps
        them up in a lambda that forwards the call to this method.

    """

    def __init__(self, module):
        self._module = module

    def __getattr__(self, attr):
        wrapper = utils.executeInMainThreadWithResult
        command = getattr(self._module, attr)

        return lambda *args, **kwargs: wrapper(
            command, *args, **kwargs)

cmds = Wrapper(cmds)
