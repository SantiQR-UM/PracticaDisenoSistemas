"""Patron Observer - Interfaz Observer.

Define la interfaz que deben implementar todos los observadores.
"""

# Standard library
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """Interfaz Observer generica.

    Los observadores implementan esta interfaz para recibir notificaciones
    cuando el estado del observable cambia.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Metodo llamado cuando el observable notifica un cambio.

        Args:
            evento: El evento o dato notificado por el observable
        """
        pass
