"""Entidad base Vehiculo.

Define la interfaz comun para todos los tipos de vehiculos del estacionamiento.
"""

# Standard library
from __future__ import annotations
from abc import ABC
from datetime import datetime


class Vehiculo(ABC):
    """Entidad base abstracta para vehiculos.

    Esta clase define los atributos y metodos comunes a todos los vehiculos.
    Solo contiene datos (DTO), sin logica de negocio.
    """

    def __init__(
        self,
        patente: str,
        superficie: float,
        tarifa_base: float,
        tolerancia_minutos: int
    ):
        """Inicializa un vehiculo.

        Args:
            patente: Patente del vehiculo
            superficie: Superficie ocupada en metros cuadrados
            tarifa_base: Tarifa base por hora
            tolerancia_minutos: Minutos de tolerancia sin cargo
        """
        self._patente = patente
        self._superficie = superficie
        self._tarifa_base = tarifa_base
        self._tolerancia_minutos = tolerancia_minutos
        self._hora_ingreso: datetime | None = None
        self._hora_egreso: datetime | None = None

    # Getters y setters
    def get_patente(self) -> str:
        """Obtiene la patente del vehiculo."""
        return self._patente

    def set_patente(self, patente: str) -> None:
        """Establece la patente del vehiculo."""
        self._patente = patente

    def get_superficie(self) -> float:
        """Obtiene la superficie ocupada."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """Establece la superficie ocupada."""
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def get_tarifa_base(self) -> float:
        """Obtiene la tarifa base por hora."""
        return self._tarifa_base

    def set_tarifa_base(self, tarifa: float) -> None:
        """Establece la tarifa base por hora."""
        if tarifa < 0:
            raise ValueError("La tarifa no puede ser negativa")
        self._tarifa_base = tarifa

    def get_tolerancia_minutos(self) -> int:
        """Obtiene los minutos de tolerancia."""
        return self._tolerancia_minutos

    def set_tolerancia_minutos(self, minutos: int) -> None:
        """Establece los minutos de tolerancia."""
        if minutos < 0:
            raise ValueError("La tolerancia no puede ser negativa")
        self._tolerancia_minutos = minutos

    def get_hora_ingreso(self) -> datetime | None:
        """Obtiene la hora de ingreso."""
        return self._hora_ingreso

    def set_hora_ingreso(self, hora: datetime) -> None:
        """Establece la hora de ingreso."""
        self._hora_ingreso = hora

    def get_hora_egreso(self) -> datetime | None:
        """Obtiene la hora de egreso."""
        return self._hora_egreso

    def set_hora_egreso(self, hora: datetime) -> None:
        """Establece la hora de egreso."""
        self._hora_egreso = hora
