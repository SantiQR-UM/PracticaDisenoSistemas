"""Entidad Moto.

Representa una motocicleta en el estacionamiento.
"""

# Standard library
from __future__ import annotations

# Local application
from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo
from python_estacionamiento.constantes import (
    SUPERFICIE_MOTO,
    TARIFA_BASE_MOTO,
    TOLERANCIA_MOTO
)


class Moto(Vehiculo):
    """Entidad Moto.

    Representa una motocicleta con caracteristicas especificas.
    """

    def __init__(self, patente: str, cilindrada: int = 150):
        """Inicializa una moto.

        Args:
            patente: Patente de la moto
            cilindrada: Cilindrada en cc (default: 150)
        """
        super().__init__(
            patente=patente,
            superficie=SUPERFICIE_MOTO,
            tarifa_base=TARIFA_BASE_MOTO,
            tolerancia_minutos=TOLERANCIA_MOTO
        )
        self._cilindrada = cilindrada

    def get_cilindrada(self) -> int:
        """Obtiene la cilindrada de la moto."""
        return self._cilindrada

    def set_cilindrada(self, cilindrada: int) -> None:
        """Establece la cilindrada de la moto."""
        if cilindrada <= 0:
            raise ValueError("La cilindrada debe ser mayor a cero")
        self._cilindrada = cilindrada
