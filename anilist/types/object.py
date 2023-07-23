from typing import Dict


class Object:
    __slots__ = ()

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())


class Hashable(Object):
    __slots__ = ()

    id: int

    def __hash__(self) -> int:
        return hash((type(self), self.id))

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return other.id == self.id
        return NotImplemented
