"""
Archivo integrador generado automaticamente
Directorio: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos
Fecha: 2025-11-04 15:58:22
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\__init__.py
# ================================================================================

# Standard library

# Local application


# ================================================================================
# ARCHIVO 2/5: auto.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\auto.py
# ================================================================================

"""Entidad Auto.

Representa un automovil en el estacionamiento.
"""

# Standard library
from __future__ import annotations

# Local application
from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo
from python_estacionamiento.constantes import (
    SUPERFICIE_AUTO,
    TARIFA_BASE_AUTO,
    TOLERANCIA_AUTO
)


class Auto(Vehiculo):
    """Entidad Auto.

    Representa un automovil con caracteristicas especificas.
    """

    def __init__(self, patente: str, marca: str = "Sin especificar"):
        """Inicializa un auto.

        Args:
            patente: Patente del auto
            marca: Marca del auto (default: "Sin especificar")
        """
        super().__init__(
            patente=patente,
            superficie=SUPERFICIE_AUTO,
            tarifa_base=TARIFA_BASE_AUTO,
            tolerancia_minutos=TOLERANCIA_AUTO
        )
        self._marca = marca

    def get_marca(self) -> str:
        """Obtiene la marca del auto."""
        return self._marca

    def set_marca(self, marca: str) -> None:
        """Establece la marca del auto."""
        self._marca = marca


# ================================================================================
# ARCHIVO 3/5: camioneta.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\camioneta.py
# ================================================================================

"""Entidad Camioneta.

Representa una camioneta en el estacionamiento.
"""

# Standard library
from __future__ import annotations

# Local application
from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo
from python_estacionamiento.constantes import (
    SUPERFICIE_CAMIONETA,
    TARIFA_BASE_CAMIONETA,
    TOLERANCIA_CAMIONETA
)


class Camioneta(Vehiculo):
    """Entidad Camioneta.

    Representa una camioneta con caracteristicas especificas.
    """

    def __init__(self, patente: str, capacidad_carga: float = 1000.0):
        """Inicializa una camioneta.

        Args:
            patente: Patente de la camioneta
            capacidad_carga: Capacidad de carga en kg (default: 1000.0)
        """
        super().__init__(
            patente=patente,
            superficie=SUPERFICIE_CAMIONETA,
            tarifa_base=TARIFA_BASE_CAMIONETA,
            tolerancia_minutos=TOLERANCIA_CAMIONETA
        )
        self._capacidad_carga = capacidad_carga

    def get_capacidad_carga(self) -> float:
        """Obtiene la capacidad de carga de la camioneta."""
        return self._capacidad_carga

    def set_capacidad_carga(self, capacidad: float) -> None:
        """Establece la capacidad de carga de la camioneta."""
        if capacidad <= 0:
            raise ValueError("La capacidad de carga debe ser mayor a cero")
        self._capacidad_carga = capacidad


# ================================================================================
# ARCHIVO 4/5: moto.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\moto.py
# ================================================================================

"""Entidad Moto.

Representa una motocicleta en el estacionamiento.
"""

# Standard library
from __future__ import annotations

# Local application
from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo
from python_estacionamiento.constantes import (
    SUPERFICIE_MOTO,
    TARIFA_BASE_MOTO,
    TOLERANCIA_MOTO
)


class Moto(Vehiculo):
    """Entidad Moto.

    Representa una motocicleta con caracteristicas especificas.
    """

    def __init__(self, patente: str, cilindrada: int = 150):
        """Inicializa una moto.

        Args:
            patente: Patente de la moto
            cilindrada: Cilindrada en cc (default: 150)
        """
        super().__init__(
            patente=patente,
            superficie=SUPERFICIE_MOTO,
            tarifa_base=TARIFA_BASE_MOTO,
            tolerancia_minutos=TOLERANCIA_MOTO
        )
        self._cilindrada = cilindrada

    def get_cilindrada(self) -> int:
        """Obtiene la cilindrada de la moto."""
        return self._cilindrada

    def set_cilindrada(self, cilindrada: int) -> None:
        """Establece la cilindrada de la moto."""
        if cilindrada <= 0:
            raise ValueError("La cilindrada debe ser mayor a cero")
        self._cilindrada = cilindrada


# ================================================================================
# ARCHIVO 5/5: vehiculo.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\vehiculo.py
# ================================================================================

"""Entidad base Vehiculo.

Define la interfaz comun para todos los tipos de vehiculos del estacionamiento.
"""

# Standard library
from __future__ import annotations
from abc import ABC
from datetime import datetime


class Vehiculo(ABC):
    """Entidad base abstracta para vehiculos.

    Esta clase define los atributos y metodos comunes a todos los vehiculos.
    Solo contiene datos (DTO), sin logica de negocio.
    """

    def __init__(
        self,
        patente: str,
        superficie: float,
        tarifa_base: float,
        tolerancia_minutos: int
    ):
        """Inicializa un vehiculo.

        Args:
            patente: Patente del vehiculo
            superficie: Superficie ocupada en metros cuadrados
            tarifa_base: Tarifa base por hora
            tolerancia_minutos: Minutos de tolerancia sin cargo
        """
        self._patente = patente
        self._superficie = superficie
        self._tarifa_base = tarifa_base
        self._tolerancia_minutos = tolerancia_minutos
        self._hora_ingreso: datetime | None = None
        self._hora_egreso: datetime | None = None

    # Getters y setters
    def get_patente(self) -> str:
        """Obtiene la patente del vehiculo."""
        return self._patente

    def set_patente(self, patente: str) -> None:
        """Establece la patente del vehiculo."""
        self._patente = patente

    def get_superficie(self) -> float:
        """Obtiene la superficie ocupada."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """Establece la superficie ocupada."""
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def get_tarifa_base(self) -> float:
        """Obtiene la tarifa base por hora."""
        return self._tarifa_base

    def set_tarifa_base(self, tarifa: float) -> None:
        """Establece la tarifa base por hora."""
        if tarifa < 0:
            raise ValueError("La tarifa no puede ser negativa")
        self._tarifa_base = tarifa

    def get_tolerancia_minutos(self) -> int:
        """Obtiene los minutos de tolerancia."""
        return self._tolerancia_minutos

    def set_tolerancia_minutos(self, minutos: int) -> None:
        """Establece los minutos de tolerancia."""
        if minutos < 0:
            raise ValueError("La tolerancia no puede ser negativa")
        self._tolerancia_minutos = minutos

    def get_hora_ingreso(self) -> datetime | None:
        """Obtiene la hora de ingreso."""
        return self._hora_ingreso

    def set_hora_ingreso(self, hora: datetime) -> None:
        """Establece la hora de ingreso."""
        self._hora_ingreso = hora

    def get_hora_egreso(self) -> datetime | None:
        """Obtiene la hora de egreso."""
        return self._hora_egreso

    def set_hora_egreso(self, hora: datetime) -> None:
        """Establece la hora de egreso."""
        self._hora_egreso = hora


