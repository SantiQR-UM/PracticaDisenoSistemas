"""Entidad Auto.

Representa un automovil en el estacionamiento.
"""

# Standard library
from __future__ import annotations

# Local application
from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo
from python_estacionamiento.constantes import (
    SUPERFICIE_AUTO,
    TARIFA_BASE_AUTO,
    TOLERANCIA_AUTO
)


class Auto(Vehiculo):
    """Entidad Auto.

    Representa un automovil con caracteristicas especificas.
    """

    def __init__(self, patente: str, marca: str = "Sin especificar"):
        """Inicializa un auto.

        Args:
            patente: Patente del auto
            marca: Marca del auto (default: "Sin especificar")
        """
        super().__init__(
            patente=patente,
            superficie=SUPERFICIE_AUTO,
            tarifa_base=TARIFA_BASE_AUTO,
            tolerancia_minutos=TOLERANCIA_AUTO
        )
        self._marca = marca

    def get_marca(self) -> str:
        """Obtiene la marca del auto."""
        return self._marca

    def set_marca(self, marca: str) -> None:
        """Establece la marca del auto."""
        self._marca = marca
