"""Estrategia de precio para eventos especiales.

Aplica recargo significativo durante eventos.
"""

# Standard library
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Local application
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.constantes import RECARGO_EVENTO_ESPECIAL

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingEventoStrategy(PricingStandardStrategy):
    """Estrategia de precio para eventos especiales.

    Aplica recargo mayor durante eventos como recitales, partidos, etc.
    """

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio con recargo de evento.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio con recargo de evento aplicado
        """
        # Calcular precio estandar
        precio_base = super().calcular_precio(vehiculo, hora_ingreso, hora_egreso)

        # Aplicar recargo de evento
        recargo = precio_base * RECARGO_EVENTO_ESPECIAL
        precio_final = precio_base + recargo

        return round(precio_final, 2)
