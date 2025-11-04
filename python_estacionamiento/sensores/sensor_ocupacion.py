"""Sensor de Ocupacion - Patron Observer.

Sensor que monitorea la ocupacion del estacionamiento.
"""

# Standard library
from python_estacionamiento.patrones.observer.observer import Observer
from python_estacionamiento.sensores.eventos import (
    EventoEstacionamiento,
    VehiculoIngresoEvento,
    VehiculoEgresoEvento,
    CapacidadCriticaEvento
)
from python_estacionamiento.utils.logger import configurar_logger


class SensorOcupacion(Observer[EventoEstacionamiento]):
    """Sensor que monitorea la ocupacion de plazas.

    Implementa el patron Observer para recibir notificaciones
    de eventos del estacionamiento.
    """

    def __init__(self, umbral_critico: int = 10):
        """Inicializa el sensor.

        Args:
            umbral_critico: Cantidad de plazas bajo la cual se considera critico
        """
        self._logger = configurar_logger('SensorOcupacion')
        self._umbral_critico = umbral_critico
        print("[SENSOR OCUPACION] Sensor inicializado y monitoreando...")

    def actualizar(self, evento: EventoEstacionamiento) -> None:
        """Procesa eventos del estacionamiento.

        Args:
            evento: Evento notificado por el observable
        """
        if isinstance(evento, VehiculoIngresoEvento):
            self._procesar_ingreso(evento)
        elif isinstance(evento, VehiculoEgresoEvento):
            self._procesar_egreso(evento)
        elif isinstance(evento, CapacidadCriticaEvento):
            self._procesar_capacidad_critica(evento)

    def _procesar_ingreso(self, evento: VehiculoIngresoEvento) -> None:
        """Procesa evento de ingreso de vehiculo.

        Args:
            evento: Evento de ingreso
        """
        print(f"[SENSOR OCUPACION] Vehiculo {evento.vehiculo.get_patente()} ingreso")
        print(f"                   Ocupacion: {evento.plazas_ocupadas} plazas")
        print(f"                   Disponibles: {evento.plazas_disponibles} plazas")

        if evento.plazas_disponibles <= self._umbral_critico:
            print(f"                   ALERTA: Capacidad critica!")

    def _procesar_egreso(self, evento: VehiculoEgresoEvento) -> None:
        """Procesa evento de egreso de vehiculo.

        Args:
            evento: Evento de egreso
        """
        print(f"[SENSOR OCUPACION] Vehiculo {evento.vehiculo.get_patente()} egreso")
        print(f"                   Tiempo estadia: {evento.tiempo_estadia}")
        print(f"                   Disponibles: {evento.plazas_disponibles} plazas")

    def _procesar_capacidad_critica(self, evento: CapacidadCriticaEvento) -> None:
        """Procesa evento de capacidad critica.

        Args:
            evento: Evento de capacidad critica
        """
        print(f"[SENSOR OCUPACION] CAPACIDAD CRITICA!")
        print(f"                   Solo {evento.plazas_disponibles} plazas disponibles")
        print(f"                   Ocupacion: {evento.porcentaje_ocupacion:.1f}%")
