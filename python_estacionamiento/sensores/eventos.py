"""Eventos del sistema de estacionamiento.

Define los eventos que los sensores pueden observar.
"""

# Standard library
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


@dataclass
class EventoEstacionamiento:
    """Evento base del estacionamiento.

    Attributes:
        timestamp: Momento en que ocurrio el evento
        mensaje: Descripcion del evento
    """
    timestamp: datetime
    mensaje: str


@dataclass
class VehiculoIngresoEvento(EventoEstacionamiento):
    """Evento de ingreso de vehiculo.

    Attributes:
        vehiculo: Vehiculo que ingreso
        plazas_ocupadas: Cantidad de plazas ocupadas despues del ingreso
        plazas_disponibles: Cantidad de plazas disponibles
    """
    vehiculo: Vehiculo
    plazas_ocupadas: int
    plazas_disponibles: int


@dataclass
class VehiculoEgresoEvento(EventoEstacionamiento):
    """Evento de egreso de vehiculo.

    Attributes:
        vehiculo: Vehiculo que egreso
        plazas_ocupadas: Cantidad de plazas ocupadas despues del egreso
        plazas_disponibles: Cantidad de plazas disponibles
        tiempo_estadia: Tiempo que estuvo estacionado
    """
    vehiculo: Vehiculo
    plazas_ocupadas: int
    plazas_disponibles: int
    tiempo_estadia: str


@dataclass
class PlazasAgotadasEvento(EventoEstacionamiento):
    """Evento de plazas agotadas.

    Attributes:
        patente_rechazada: Patente del vehiculo que fue rechazado
    """
    patente_rechazada: str


@dataclass
class CapacidadCriticaEvento(EventoEstacionamiento):
    """Evento de capacidad critica.

    Se dispara cuando quedan pocas plazas disponibles.

    Attributes:
        plazas_disponibles: Plazas que quedan disponibles
        porcentaje_ocupacion: Porcentaje de ocupacion actual
    """
    plazas_disponibles: int
    porcentaje_ocupacion: float
