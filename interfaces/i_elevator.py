from abc import ABC, abstractmethod


class IElevator(ABC):
    @abstractmethod
    def _current_floor(self, current_floor): ...

    @abstractmethod
    def _call_elevator(self): ...

    @abstractmethod
    def _open_doors(self): ...

    @abstractmethod
    def _close_doors(self): ...

    @abstractmethod
    def _select_floor(self): ...

    @abstractmethod
    def _move_to_floor(self, current_floor): ...
