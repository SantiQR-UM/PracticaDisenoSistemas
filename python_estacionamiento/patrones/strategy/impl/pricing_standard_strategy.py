"""Estrategia de precio estandar.

Calcula el precio basado en la tarifa base del vehiculo y el tiempo de estadia.
"""

# Standard library
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Local application
from python_estacionamiento.patrones.strategy.pricing_strategy import PricingStrategy

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingStandardStrategy(PricingStrategy):
    """Estrategia de precio estandar.

    Calcula: tarifa_base_por_hora * horas_de_estadia
    Considera tolerancia en minutos sin cargo.
    """

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio estandar.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio calculado considerando tolerancia
        """
        # Calcular tiempo de estadia en minutos
        delta = hora_egreso - hora_ingreso
        minutos_totales = delta.total_seconds() / 60.0

        # Restar tolerancia
        minutos_cobrables = max(0, minutos_totales - vehiculo.get_tolerancia_minutos())

        # Convertir a horas y calcular precio
        horas = minutos_cobrables / 60.0
        precio = vehiculo.get_tarifa_base() * horas

        return round(precio, 2)
