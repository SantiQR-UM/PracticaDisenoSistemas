"""Patron Observer - Clase Observable.

Define la clase base para objetos observables.
"""

# Standard library
from __future__ import annotations
from abc import ABC
from typing import List, TypeVar, Generic, TYPE_CHECKING

if TYPE_CHECKING:
    from python_estacionamiento.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """Clase base Observable generica.

    Los observables mantienen una lista de observadores y los notifican
    cuando su estado cambia.
    """

    def __init__(self):
        """Inicializa el observable con una lista vacia de observadores."""
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un observador a la lista.

        Args:
            observador: El observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista.

        Args:
            observador: El observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores de un cambio.

        Args:
            evento: El evento o dato a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)
