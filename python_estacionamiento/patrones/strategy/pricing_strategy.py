"""Patron Strategy - Interfaz PricingStrategy.

Define la interfaz para estrategias de calculo de precios.
"""

# Standard library
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingStrategy(ABC):
    """Interfaz Strategy para calcular precios.

    Define el contrato que deben cumplir todas las estrategias de precios.
    """

    @abstractmethod
    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio a cobrar por el estacionamiento.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso al estacionamiento
            hora_egreso: Hora de egreso del estacionamiento

        Returns:
            El precio total a cobrar
        """
        pass
