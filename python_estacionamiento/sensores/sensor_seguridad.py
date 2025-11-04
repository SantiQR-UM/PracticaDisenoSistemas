"""Sensor de Seguridad - Patron Observer.

Sensor que monitorea eventos de seguridad en el estacionamiento.
"""

# Standard library
from python_estacionamiento.patrones.observer.observer import Observer
from python_estacionamiento.sensores.eventos import (
    EventoEstacionamiento,
    VehiculoIngresoEvento,
    VehiculoEgresoEvento,
    PlazasAgotadasEvento
)
from python_estacionamiento.utils.logger import configurar_logger


class SensorSeguridad(Observer[EventoEstacionamiento]):
    """Sensor de seguridad del estacionamiento.

    Monitorea eventos de seguridad y genera alertas
    implementando el patron Observer.
    """

    def __init__(self):
        """Inicializa el sensor de seguridad."""
        self._logger = configurar_logger('SensorSeguridad')
        self._alertas = []
        self._vehiculos_monitoreados = set()
        print("[SENSOR SEGURIDAD] Sistema de seguridad activado...")

    def actualizar(self, evento: EventoEstacionamiento) -> None:
        """Procesa eventos del estacionamiento.

        Args:
            evento: Evento notificado por el observable
        """
        if isinstance(evento, VehiculoIngresoEvento):
            self._monitorear_ingreso(evento)
        elif isinstance(evento, VehiculoEgresoEvento):
            self._monitorear_egreso(evento)
        elif isinstance(evento, PlazasAgotadasEvento):
            self._alerta_acceso_denegado(evento)

    def _monitorear_ingreso(self, evento: VehiculoIngresoEvento) -> None:
        """Monitorea ingreso de vehiculo.

        Args:
            evento: Evento de ingreso
        """
        patente = evento.vehiculo.get_patente()
        self._vehiculos_monitoreados.add(patente)

        print(f"[SENSOR SEGURIDAD] Vehiculo registrado en sistema: {patente}")
        print(f"                   Total vehiculos monitoreados: {len(self._vehiculos_monitoreados)}")

    def _monitorear_egreso(self, evento: VehiculoEgresoEvento) -> None:
        """Monitorea egreso de vehiculo.

        Args:
            evento: Evento de egreso
        """
        patente = evento.vehiculo.get_patente()

        if patente in self._vehiculos_monitoreados:
            self._vehiculos_monitoreados.remove(patente)
            print(f"[SENSOR SEGURIDAD] Vehiculo autorizado para salir: {patente}")
            print(f"                   Vehiculos restantes: {len(self._vehiculos_monitoreados)}")
        else:
            # Alerta de seguridad
            alerta = f"ALERTA: Vehiculo {patente} intenta salir sin registro de ingreso"
            self._alertas.append(alerta)
            print(f"[SENSOR SEGURIDAD] {alerta}")

    def _alerta_acceso_denegado(self, evento: PlazasAgotadasEvento) -> None:
        """Genera alerta de acceso denegado.

        Args:
            evento: Evento de plazas agotadas
        """
        print(f"[SENSOR SEGURIDAD] ACCESO DENEGADO: {evento.patente_rechazada}")
        print(f"                   Razon: Estacionamiento completo")

    def get_alertas(self) -> list:
        """Obtiene todas las alertas de seguridad.

        Returns:
            Lista de alertas generadas
        """
        return self._alertas.copy()

    def get_vehiculos_monitoreados(self) -> set:
        """Obtiene vehiculos actualmente monitoreados.

        Returns:
            Set de patentes monitoreadas
        """
        return self._vehiculos_monitoreados.copy()
