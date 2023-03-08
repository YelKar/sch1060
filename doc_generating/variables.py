from copy import copy
from typing import Any, TypeVar, Iterable

_VAL = TypeVar("_VAL", bound=Any)


class Variable:
    """
    Object of this class extends all attributes from passed value

    __call__ sets value length
    "<instance> <= <some_item>" sets characters that fills all spaces

    >>> length, char = 16, "+"
    >>> Variable.__repr__ = lambda x: f'"{x}"'  # for demonstration, we overwrite repr method
    >>> var = Variable("variable")
    >>> var
    "variable"
    >>> var(length) <= char
    "++++variable++++"
    >>> var(4)
    "variable"
    >>> other_var = var(12)
    >>> other_var
    "  variable  "
    >>> Variable("Hello, world!")(21) <= "_"
    "____Hello,_world!____"
    >>> other_var("Hello")
    Traceback (most recent call last):
    ...
    AssertionError: length must be only integer
    """
    def __new__(cls, value: _VAL) -> _VAL:
        return super().__new__(cls)

    def __init__(self, value: _VAL):
        self.value = value
        self.length = 0
        self.empty = " "
        self.align = "^"

    def __call__(self, length=None, align=None, empty=None):
        """Set value length"""
        assert isinstance(length, int), "length must be only integer"
        assert isinstance(align, str) or align is None, "align must be only string"
        assert align is None or align in "<^>", 'arrow must be "<" (left), "^" (center) or ">" (right)'
        res = copy(self)
        res.length = length or self.length
        res.align = align or self.align
        res.empty = empty or self.empty
        return res

    def __copy__(self):
        """return copy of self instance"""
        res = self.__class__(self.value)
        res.length = self.length
        res.empty = self.empty
        res.align = self.align
        return res

    def __getattr__(self, item) -> Any:
        """Get value attributes"""
        return getattr(self.value, item)

    def __getitem__(self, item):
        if hasattr(self.value, "__getitem__"):
            return self.value[item]
        return self.__class__(None)

    def __setitem__(self, key, value):
        if hasattr(self.value, "__setitem__"):
            self.value[key] = value
        else:
            raise TypeError("'Variable' object is not subscriptable")

    def __le__(self, char: str):
        """Sets characters that fills all spaces"""
        res = copy(self)
        res.empty = char
        return res

    def __str__(self):
        string = '' if self.value is None else str(self.value)
        return f"{string:{self.align}{self.length}}".replace(" ", self.empty)

    def __repr__(self):
        return repr(self.value)

    def __dir__(self) -> Iterable[str]:
        return list(super().__dir__()) + dir(self.value)


if __name__ == '__main__':
    v = Variable(2005)
    print(v(9))
    print(Variable("Hello, world!")(21, ">") <= "_")
