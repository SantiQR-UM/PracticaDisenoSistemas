"""
Archivo integrador generado automaticamente
Directorio: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\observer
Fecha: 2025-11-04 15:58:22
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\observer\__init__.py
# ================================================================================

# Standard library

# Local application


# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\observer\observable.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\observer\observer.py
# ================================================================================

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


