"""Excepciones personalizadas del sistema de estacionamiento."""

# Standard library
from __future__ import annotations


class EstacionamientoException(Exception):
    """Excepcion base para el sistema de estacionamiento."""

    def __init__(self, mensaje: str):
        """Inicializa la excepcion.

        Args:
            mensaje: Mensaje de error
        """
        super().__init__(mensaje)
        self._mensaje = mensaje

    def get_mensaje(self) -> str:
        """Obtiene el mensaje de error."""
        return self._mensaje


class PlazasAgotadasException(EstacionamientoException):
    """Excepcion lanzada cuando no hay plazas disponibles."""

    def __init__(self, plazas_disponibles: int):
        """Inicializa la excepcion.

        Args:
            plazas_disponibles: Cantidad de plazas disponibles
        """
        super().__init__(f"No hay plazas disponibles. Plazas actuales: {plazas_disponibles}")
        self._plazas_disponibles = plazas_disponibles

    def get_plazas_disponibles(self) -> int:
        """Obtiene las plazas disponibles."""
        return self._plazas_disponibles


class VehiculoNoEncontradoException(EstacionamientoException):
    """Excepcion lanzada cuando un vehiculo no se encuentra en el estacionamiento."""

    def __init__(self, patente: str):
        """Inicializa la excepcion.

        Args:
            patente: Patente del vehiculo no encontrado
        """
        super().__init__(f"Vehiculo con patente {patente} no encontrado en el estacionamiento")
        self._patente = patente

    def get_patente(self) -> str:
        """Obtiene la patente del vehiculo."""
        return self._patente
