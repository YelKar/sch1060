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

    def __call__(self, length):
        """Set value length"""
        assert isinstance(length, int), "length must be only integer"
        res = copy(self)
        res.length = length
        return res

    def __copy__(self):
        """return copy of self instance"""
        res = self.__class__(self.value)
        res.length = self.length
        res.empty = self.empty
        return res

    def __getattr__(self, item) -> Any:
        """Get value attributes"""
        return getattr(self.value, item)

    def __getitem__(self, item):
        if hasattr(self.value, "__getitem__"):
            return self.value[item]
        raise TypeError("'Variable' object is not subscriptable")

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
        return f"{str(self.value):^{self.length}}".replace(" ", self.empty)

    def __repr__(self):
        return repr(self.value)

    def __dir__(self) -> Iterable[str]:
        return list(super().__dir__()) + dir(self.value)


if __name__ == '__main__':
    v = Variable("Hello, world")
    print(v(40) <= "8")
    print(Variable("Hello, world!")(21) <= "_")
