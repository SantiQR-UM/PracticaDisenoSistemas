"""Estrategia de precio con recargo de valet.

Aplica recargo por servicio de valet parking.
"""

# Standard library
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Local application
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.constantes import RECARGO_VALET

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingValetStrategy(PricingStandardStrategy):
    """Estrategia de precio con recargo de valet.

    Aplica recargo sobre el precio estandar por servicio premium.
    """

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio con recargo de valet.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio con recargo aplicado
        """
        # Calcular precio estandar
        precio_base = super().calcular_precio(vehiculo, hora_ingreso, hora_egreso)

        # Aplicar recargo
        recargo = precio_base * RECARGO_VALET
        precio_final = precio_base + recargo

        return round(precio_final, 2)
