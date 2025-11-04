"""Sensores del estacionamiento - Patron Observer.

Este modulo implementa sensores que monitorean eventos del estacionamiento
usando el patron Observer.
"""

# Standard library

# Local application
from python_estacionamiento.sensores.eventos import (
    EventoEstacionamiento,
    VehiculoIngresoEvento,
    VehiculoEgresoEvento,
    PlazasAgotadasEvento,
    CapacidadCriticaEvento
)
from python_estacionamiento.sensores.sensor_ocupacion import SensorOcupacion
from python_estacionamiento.sensores.sensor_camara import SensorCamara
from python_estacionamiento.sensores.sensor_seguridad import SensorSeguridad

__all__ = [
    'EventoEstacionamiento',
    'VehiculoIngresoEvento',
    'VehiculoEgresoEvento',
    'PlazasAgotadasEvento',
    'CapacidadCriticaEvento',
    'SensorOcupacion',
    'SensorCamara',
    'SensorSeguridad'
]
