import sys
from typing import Hashable

data = [1, 2.0, '3', [4], (5,)]

for n, obj in enumerate(data, 1):
    print(f"{n} {obj} {id(obj)} {sys.getsizeof(obj)}" # sys.getsizeof(obj) - размер объекта
          f"{hash(obj) if isinstance(obj, Hashable) else " Not Hashable"}"
          f"{" Integer" if isinstance(obj, int) else " "}"
          f"{" String" if isinstance(obj, str) else " "}")
