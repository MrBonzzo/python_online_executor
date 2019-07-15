import sys


class Checker():
    def __init__(self):
        self.next_checker = None

    def set_next(self, next_checker):
        self.next_checker = next_checker
        return self.next_checker

    def check(self):
        if self.next_checker:
            self.next_checker.check()


class ModuleChecker(Checker):
    def __init__(self, module_name):
        super().__init__()
        self.module_name = module_name

    def check(self):
        if self.module_name in sys.modules:
            del sys.modules[self.module_name]
        super().check()


class FunctionChecker(Checker):
    def __init__(self, builtin_name):
        super().__init__()
        self.builtin_name = builtin_name

    def check(self):
        if self.builtin_name in __builtins__:
            del __builtins__[self.builtin_name]
        super().check()


def preparing_statements():
    modules = ['os']
    builtins = ['open', 'exec', 'eval']

    checkers = [ModuleChecker(m) for m in modules]
    checkers.extend([FunctionChecker(b) for b in builtins])

    for i, c in enumerate(checkers[1:]):
        checkers[i].set_next(c)

    checkers[0].check()
