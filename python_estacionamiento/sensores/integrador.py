"""
Archivo integrador generado automaticamente
Directorio: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores
Fecha: 2025-11-04 15:58:22
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\__init__.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 2/5: eventos.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\eventos.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: sensor_camara.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\sensor_camara.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/5: sensor_ocupacion.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\sensor_ocupacion.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: sensor_seguridad.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\sensor_seguridad.py
# ================================================================================

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


