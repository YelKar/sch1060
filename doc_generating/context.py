from typing import Iterable

from doc_generating.variables import Variable


class Context(dict):
    def __new__(cls, _context: dict = None, **context):
        if _context:
            context.update(_context)

        _obj = super().__new__(cls)

        for k, v in context.items():
            if isinstance(v, dict):
                _obj[k] = cls(v)
            elif isinstance(v, Iterable) and not isinstance(v, str):
                _obj[k] = Variable(list(cls._from_list(v)))
            else:
                _obj[k] = Variable(v)
        return _obj

    def __init__(self, _context: dict = None, **context):
        super().__init__()

    def __getattr__(self, item):
        return self.get(item)

    @classmethod
    def _from_list(cls, arr: Iterable):
        for item in arr:
            if isinstance(item, dict):
                yield cls(item)
            elif isinstance(item, Iterable) and not isinstance(item, str):
                yield Variable(list(cls._from_list(item)))
            else:
                yield Variable(item)


if __name__ == '__main__':
    ctx = Context({
        "name": "Елисей",
        "lastname": "Карамышев"
    })

    print(ctx)
