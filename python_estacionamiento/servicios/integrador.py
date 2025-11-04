"""
Archivo integrador generado automaticamente
Directorio: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\servicios
Fecha: 2025-11-04 15:58:22
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\servicios\__init__.py
# ================================================================================

# Standard library

# Local application


# ================================================================================
# ARCHIVO 2/3: parking_lot_manager.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\servicios\parking_lot_manager.py
# ================================================================================

"""Parking Lot Manager - Singleton.

Administra el estado del estacionamiento de forma centralizada.
"""

# Standard library
from __future__ import annotations
from threading import Lock
from typing import Dict
from datetime import datetime

# Local application
from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo
from python_estacionamiento.excepciones.estacionamiento_exception import (
    PlazasAgotadasException,
    VehiculoNoEncontradoException
)
from python_estacionamiento.constantes import CAPACIDAD_MAXIMA_PLAZAS
from python_estacionamiento.utils.logger import configurar_logger
from python_estacionamiento.persistencia.json_storage import JsonStorage
from python_estacionamiento.patrones.factory.vehiculo_factory import VehiculoFactory
from python_estacionamiento.patrones.observer.observable import Observable
from python_estacionamiento.sensores.eventos import (
    EventoEstacionamiento,
    VehiculoIngresoEvento,
    VehiculoEgresoEvento,
    PlazasAgotadasEvento,
    CapacidadCriticaEvento
)


class ParkingLotManager(Observable[EventoEstacionamiento]):
    """Gestor Singleton del estacionamiento.

    Implementa el patron Singleton con thread-safety para gestionar
    el estado global del estacionamiento.
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """Implementacion del patron Singleton.

        Garantiza que solo exista una instancia del gestor.
        Usa double-checked locking para thread-safety.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Inicializa el gestor del estacionamiento.

        Se ejecuta solo una vez gracias al patron Singleton.
        """
        # Evitar re-inicializacion en Singleton
        if hasattr(self, '_initialized'):
            return

        # Inicializar Observable
        Observable.__init__(self)

        self._initialized = True
        self._vehiculos_activos: Dict[str, Vehiculo] = {}
        self._capacidad_maxima = CAPACIDAD_MAXIMA_PLAZAS
        self._plazas_ocupadas = 0
        self._logger = configurar_logger('ParkingLotManager')
        self._storage = JsonStorage()
        self._logger.info('ParkingLotManager inicializado correctamente')

    @classmethod
    def get_instance(cls):
        """Obtiene la instancia unica del gestor.

        Returns:
            La instancia Singleton del gestor
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def ingresar_vehiculo(self, vehiculo: Vehiculo) -> None:
        """Registra el ingreso de un vehiculo al estacionamiento.

        Args:
            vehiculo: El vehiculo que ingresa

        Raises:
            PlazasAgotadasException: Si no hay plazas disponibles
        """
        if self._plazas_ocupadas >= self._capacidad_maxima:
            self._logger.warning(
                f'Intento de ingreso rechazado: plazas agotadas. Patente: {vehiculo.get_patente()}'
            )

            # Notificar evento de plazas agotadas
            evento = PlazasAgotadasEvento(
                timestamp=datetime.now(),
                mensaje=f"Acceso denegado a vehiculo {vehiculo.get_patente()}: Estacionamiento completo",
                patente_rechazada=vehiculo.get_patente()
            )
            self.notificar_observadores(evento)

            raise PlazasAgotadasException(self.get_plazas_disponibles())

        vehiculo.set_hora_ingreso(datetime.now())
        self._vehiculos_activos[vehiculo.get_patente()] = vehiculo
        self._plazas_ocupadas += 1
        self._logger.info(
            f'Vehiculo ingresado: {vehiculo.get_patente()} | '
            f'Tipo: {vehiculo.__class__.__name__} | '
            f'Plazas ocupadas: {self._plazas_ocupadas}/{self._capacidad_maxima}'
        )

        # Notificar evento de ingreso
        evento_ingreso = VehiculoIngresoEvento(
            timestamp=datetime.now(),
            mensaje=f"Vehiculo {vehiculo.get_patente()} ingreso al estacionamiento",
            vehiculo=vehiculo,
            plazas_ocupadas=self._plazas_ocupadas,
            plazas_disponibles=self.get_plazas_disponibles()
        )
        self.notificar_observadores(evento_ingreso)

        # Verificar capacidad critica (< 10% disponible)
        porcentaje_disponible = (self.get_plazas_disponibles() / self._capacidad_maxima) * 100
        if porcentaje_disponible < 10:
            evento_critico = CapacidadCriticaEvento(
                timestamp=datetime.now(),
                mensaje="Capacidad critica alcanzada",
                plazas_disponibles=self.get_plazas_disponibles(),
                porcentaje_ocupacion=(self._plazas_ocupadas / self._capacidad_maxima) * 100
            )
            self.notificar_observadores(evento_critico)

    def egresar_vehiculo(self, patente: str) -> Vehiculo:
        """Registra el egreso de un vehiculo del estacionamiento.

        Args:
            patente: Patente del vehiculo que egresa

        Returns:
            El vehiculo que egresa

        Raises:
            VehiculoNoEncontradoException: Si el vehiculo no esta en el estacionamiento
        """
        if patente not in self._vehiculos_activos:
            self._logger.error(f'Intento de egreso fallido: vehiculo no encontrado. Patente: {patente}')
            raise VehiculoNoEncontradoException(patente)

        vehiculo = self._vehiculos_activos.pop(patente)
        vehiculo.set_hora_egreso(datetime.now())
        self._plazas_ocupadas -= 1

        tiempo_estadia = vehiculo.get_hora_egreso() - vehiculo.get_hora_ingreso()
        self._logger.info(
            f'Vehiculo egresado: {patente} | '
            f'Tiempo estadia: {tiempo_estadia} | '
            f'Plazas ocupadas: {self._plazas_ocupadas}/{self._capacidad_maxima}'
        )

        # Notificar evento de egreso
        evento_egreso = VehiculoEgresoEvento(
            timestamp=datetime.now(),
            mensaje=f"Vehiculo {patente} egreso del estacionamiento",
            vehiculo=vehiculo,
            plazas_ocupadas=self._plazas_ocupadas,
            plazas_disponibles=self.get_plazas_disponibles(),
            tiempo_estadia=str(tiempo_estadia)
        )
        self.notificar_observadores(evento_egreso)

        return vehiculo

    def get_plazas_disponibles(self) -> int:
        """Obtiene la cantidad de plazas disponibles.

        Returns:
            Numero de plazas libres
        """
        return self._capacidad_maxima - self._plazas_ocupadas

    def get_plazas_ocupadas(self) -> int:
        """Obtiene la cantidad de plazas ocupadas.

        Returns:
            Numero de plazas ocupadas
        """
        return self._plazas_ocupadas

    def get_vehiculo(self, patente: str) -> Vehiculo | None:
        """Busca un vehiculo en el estacionamiento.

        Args:
            patente: Patente del vehiculo a buscar

        Returns:
            El vehiculo si esta en el estacionamiento, None si no
        """
        return self._vehiculos_activos.get(patente)

    def get_todos_vehiculos(self) -> Dict[str, Vehiculo]:
        """Obtiene todos los vehiculos activos.

        Returns:
            Diccionario de vehiculos activos (copia defensiva)
        """
        return self._vehiculos_activos.copy()

    def reset(self) -> None:
        """Resetea el estado del estacionamiento.

        Util para testing o limpieza.
        """
        self._vehiculos_activos.clear()
        self._plazas_ocupadas = 0

    def guardar_estado(self) -> bool:
        """Guarda el estado actual del estacionamiento.

        Returns:
            True si se guardó correctamente, False si hubo error
        """
        estado = {
            'plazas_ocupadas': self._plazas_ocupadas,
            'capacidad_maxima': self._capacidad_maxima,
            'vehiculos': self._vehiculos_activos
        }
        return self._storage.guardar_estado(estado)

    def cargar_estado(self) -> bool:
        """Carga el estado del estacionamiento desde archivo.

        Returns:
            True si se cargó correctamente, False si no existe o hay error
        """
        estado = self._storage.cargar_estado()
        if estado is None:
            self._logger.warning('No se pudo cargar estado, iniciando vacío')
            return False

        try:
            # Restaurar estado básico
            self._plazas_ocupadas = estado.get('plazas_ocupadas', 0)
            self._capacidad_maxima = estado.get('capacidad_maxima', CAPACIDAD_MAXIMA_PLAZAS)

            # Restaurar vehículos
            self._vehiculos_activos.clear()
            vehiculos_data = estado.get('vehiculos_data', [])

            for vehiculo_data in vehiculos_data:
                try:
                    # Recrear vehículo usando factory
                    tipo = vehiculo_data['tipo']
                    patente = vehiculo_data['patente']
                    vehiculo = VehiculoFactory.crear_vehiculo(tipo, patente)

                    # Restaurar timestamps
                    hora_ingreso_str = vehiculo_data.get('hora_ingreso')
                    if hora_ingreso_str:
                        hora_ingreso = datetime.fromisoformat(hora_ingreso_str)
                        vehiculo.set_hora_ingreso(hora_ingreso)

                    hora_egreso_str = vehiculo_data.get('hora_egreso')
                    if hora_egreso_str:
                        hora_egreso = datetime.fromisoformat(hora_egreso_str)
                        vehiculo.set_hora_egreso(hora_egreso)

                    self._vehiculos_activos[patente] = vehiculo

                except Exception as e:
                    self._logger.error(f'Error al restaurar vehículo {vehiculo_data.get("patente")}: {e}')

            self._logger.info(f'Estado cargado: {self._plazas_ocupadas} plazas ocupadas, {len(self._vehiculos_activos)} vehículos')
            return True

        except Exception as e:
            self._logger.error(f'Error al restaurar estado: {e}')
            return False


# ================================================================================
# ARCHIVO 3/3: pricing_registry.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\servicios\pricing_registry.py
# ================================================================================

"""Pricing Registry - Singleton.

Gestiona las estrategias de precio de forma centralizada.
"""

# Standard library
from __future__ import annotations
from threading import Lock
from datetime import datetime

# Local application
from python_estacionamiento.patrones.strategy.pricing_strategy import PricingStrategy
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingRegistry:
    """Registro Singleton de estrategias de precio.

    Implementa el patron Singleton con thread-safety para gestionar
    la estrategia de precio activa.
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """Implementacion del patron Singleton.

        Garantiza que solo exista una instancia del registro.
        Usa double-checked locking para thread-safety.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Inicializa el registro de precios.

        Se ejecuta solo una vez gracias al patron Singleton.
        """
        # Evitar re-inicializacion en Singleton
        if hasattr(self, '_initialized'):
            return

        self._initialized = True
        self._estrategia_actual: PricingStrategy = PricingStandardStrategy()

    @classmethod
    def get_instance(cls):
        """Obtiene la instancia unica del registro.

        Returns:
            La instancia Singleton del registro
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def set_estrategia(self, estrategia: PricingStrategy) -> None:
        """Establece la estrategia de precio activa.

        Args:
            estrategia: La nueva estrategia de precio
        """
        self._estrategia_actual = estrategia

    def get_estrategia(self) -> PricingStrategy:
        """Obtiene la estrategia de precio actual.

        Returns:
            La estrategia activa
        """
        return self._estrategia_actual

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio usando la estrategia actual.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio calculado
        """
        return self._estrategia_actual.calcular_precio(vehiculo, hora_ingreso, hora_egreso)


