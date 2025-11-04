"""Sensor de Camara - Patron Observer.

Sensor que simula camaras de lectura de patentes.
"""

# Standard library
from python_estacionamiento.patrones.observer.observer import Observer
from python_estacionamiento.sensores.eventos import (
    EventoEstacionamiento,
    VehiculoIngresoEvento,
    VehiculoEgresoEvento
)
from python_estacionamiento.utils.logger import configurar_logger


class SensorCamara(Observer[EventoEstacionamiento]):
    """Sensor de camara que registra patentes.

    Simula camaras de lectura automatica de patentes
    implementando el patron Observer.
    """

    def __init__(self, ubicacion: str = "Principal"):
        """Inicializa el sensor de camara.

        Args:
            ubicacion: Ubicacion de la camara (ej: "Principal", "Salida", "Piso 2")
        """
        self._logger = configurar_logger('SensorCamara')
        self._ubicacion = ubicacion
        self._registros = []
        print(f"[CAMARA {self._ubicacion}] Camara inicializada y capturando patentes...")

    def actualizar(self, evento: EventoEstacionamiento) -> None:
        """Procesa eventos del estacionamiento.

        Args:
            evento: Evento notificado por el observable
        """
        if isinstance(evento, VehiculoIngresoEvento):
            self._registrar_ingreso(evento)
        elif isinstance(evento, VehiculoEgresoEvento):
            self._registrar_egreso(evento)

    def _registrar_ingreso(self, evento: VehiculoIngresoEvento) -> None:
        """Registra ingreso de vehiculo.

        Args:
            evento: Evento de ingreso
        """
        vehiculo = evento.vehiculo
        tipo = vehiculo.__class__.__name__
        print(f"[CAMARA {self._ubicacion}] Patente detectada: {vehiculo.get_patente()}")
        print(f"                  Tipo vehiculo: {tipo}")
        print(f"                  Hora: {evento.timestamp.strftime('%H:%M:%S')}")

        self._registros.append({
            'tipo': 'INGRESO',
            'patente': vehiculo.get_patente(),
            'timestamp': evento.timestamp
        })

    def _registrar_egreso(self, evento: VehiculoEgresoEvento) -> None:
        """Registra egreso de vehiculo.

        Args:
            evento: Evento de egreso
        """
        vehiculo = evento.vehiculo
        print(f"[CAMARA {self._ubicacion}] Patente detectada: {vehiculo.get_patente()}")
        print(f"                  Accion: SALIDA")
        print(f"                  Hora: {evento.timestamp.strftime('%H:%M:%S')}")

        self._registros.append({
            'tipo': 'EGRESO',
            'patente': vehiculo.get_patente(),
            'timestamp': evento.timestamp
        })

    def get_registros(self) -> list:
        """Obtiene todos los registros capturados.

        Returns:
            Lista de registros de la camara
        """
        return self._registros.copy()
