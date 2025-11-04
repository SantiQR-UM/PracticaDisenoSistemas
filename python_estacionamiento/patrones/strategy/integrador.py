"""
Archivo integrador generado automaticamente
Directorio: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy
Fecha: 2025-11-04 15:58:22
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\__init__.py
# ================================================================================

# Standard library

# Local application


# ================================================================================
# ARCHIVO 2/2: pricing_strategy.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\pricing_strategy.py
# ================================================================================

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


