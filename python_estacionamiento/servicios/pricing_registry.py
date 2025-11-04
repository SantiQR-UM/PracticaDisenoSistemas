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
