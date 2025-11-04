"""Entidad Camioneta.

Representa una camioneta en el estacionamiento.
"""

# Standard library
from __future__ import annotations

# Local application
from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo
from python_estacionamiento.constantes import (
    SUPERFICIE_CAMIONETA,
    TARIFA_BASE_CAMIONETA,
    TOLERANCIA_CAMIONETA
)


class Camioneta(Vehiculo):
    """Entidad Camioneta.

    Representa una camioneta con caracteristicas especificas.
    """

    def __init__(self, patente: str, capacidad_carga: float = 1000.0):
        """Inicializa una camioneta.

        Args:
            patente: Patente de la camioneta
            capacidad_carga: Capacidad de carga en kg (default: 1000.0)
        """
        super().__init__(
            patente=patente,
            superficie=SUPERFICIE_CAMIONETA,
            tarifa_base=TARIFA_BASE_CAMIONETA,
            tolerancia_minutos=TOLERANCIA_CAMIONETA
        )
        self._capacidad_carga = capacidad_carga

    def get_capacidad_carga(self) -> float:
        """Obtiene la capacidad de carga de la camioneta."""
        return self._capacidad_carga

    def set_capacidad_carga(self, capacidad: float) -> None:
        """Establece la capacidad de carga de la camioneta."""
        if capacidad <= 0:
            raise ValueError("La capacidad de carga debe ser mayor a cero")
        self._capacidad_carga = capacidad
