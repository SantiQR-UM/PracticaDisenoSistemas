"""Estrategia de precio con descuento Happy Hour.

Aplica descuento en horario especifico.
"""

# Standard library
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Local application
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.constantes import DESCUENTO_HAPPY_HOUR

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingHappyHourStrategy(PricingStandardStrategy):
    """Estrategia de precio con descuento Happy Hour.

    Aplica descuento sobre el precio estandar.
    """

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio con descuento Happy Hour.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio con descuento aplicado
        """
        # Calcular precio estandar
        precio_base = super().calcular_precio(vehiculo, hora_ingreso, hora_egreso)

        # Aplicar descuento
        descuento = precio_base * DESCUENTO_HAPPY_HOUR
        precio_final = precio_base - descuento

        return round(precio_final, 2)
