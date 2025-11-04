"""Patron Factory Method - VehiculoFactory.

Fabrica para crear instancias de vehiculos sin acoplar el codigo cliente
a clases concretas.
"""

# Standard library
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class VehiculoFactory:
    """Factory Method para crear vehiculos.

    Encapsula la logica de creacion de diferentes tipos de vehiculos,
    permitiendo extensibilidad sin modificar codigo existente.
    """

    @staticmethod
    def crear_vehiculo(tipo: str, patente: str) -> Vehiculo:
        """Crea un vehiculo del tipo especificado.

        Args:
            tipo: Tipo de vehiculo ("Moto", "Auto", "Camioneta")
            patente: Patente del vehiculo

        Returns:
            Instancia del vehiculo creado

        Raises:
            ValueError: Si el tipo de vehiculo es desconocido
        """
        factories = {
            "Moto": VehiculoFactory._crear_moto,
            "Auto": VehiculoFactory._crear_auto,
            "Camioneta": VehiculoFactory._crear_camioneta
        }

        if tipo not in factories:
            raise ValueError(f"Tipo de vehiculo desconocido: {tipo}")

        return factories[tipo](patente)

    @staticmethod
    def _crear_moto(patente: str) -> Vehiculo:
        """Crea una moto.

        Args:
            patente: Patente de la moto

        Returns:
            Instancia de Moto
        """
        from python_estacionamiento.entidades.vehiculos.moto import Moto
        return Moto(patente=patente, cilindrada=150)

    @staticmethod
    def _crear_auto(patente: str) -> Vehiculo:
        """Crea un auto.

        Args:
            patente: Patente del auto

        Returns:
            Instancia de Auto
        """
        from python_estacionamiento.entidades.vehiculos.auto import Auto
        return Auto(patente=patente, marca="Sin especificar")

    @staticmethod
    def _crear_camioneta(patente: str) -> Vehiculo:
        """Crea una camioneta.

        Args:
            patente: Patente de la camioneta

        Returns:
            Instancia de Camioneta
        """
        from python_estacionamiento.entidades.vehiculos.camioneta import Camioneta
        return Camioneta(patente=patente, capacidad_carga=1000.0)
