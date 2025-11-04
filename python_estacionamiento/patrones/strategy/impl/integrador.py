"""
Archivo integrador generado automaticamente
Directorio: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl
Fecha: 2025-11-04 15:58:22
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\__init__.py
# ================================================================================

# Standard library

# Local application


# ================================================================================
# ARCHIVO 2/5: pricing_evento_strategy.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\pricing_evento_strategy.py
# ================================================================================

"""Estrategia de precio para eventos especiales.

Aplica recargo significativo durante eventos.
"""

# Standard library
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Local application
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.constantes import RECARGO_EVENTO_ESPECIAL

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingEventoStrategy(PricingStandardStrategy):
    """Estrategia de precio para eventos especiales.

    Aplica recargo mayor durante eventos como recitales, partidos, etc.
    """

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio con recargo de evento.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio con recargo de evento aplicado
        """
        # Calcular precio estandar
        precio_base = super().calcular_precio(vehiculo, hora_ingreso, hora_egreso)

        # Aplicar recargo de evento
        recargo = precio_base * RECARGO_EVENTO_ESPECIAL
        precio_final = precio_base + recargo

        return round(precio_final, 2)


# ================================================================================
# ARCHIVO 3/5: pricing_happy_hour_strategy.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\pricing_happy_hour_strategy.py
# ================================================================================

"""Estrategia de precio con descuento Happy Hour.

Aplica descuento en horario especifico.
"""

# Standard library
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Local application
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.constantes import DESCUENTO_HAPPY_HOUR

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingHappyHourStrategy(PricingStandardStrategy):
    """Estrategia de precio con descuento Happy Hour.

    Aplica descuento sobre el precio estandar.
    """

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio con descuento Happy Hour.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio con descuento aplicado
        """
        # Calcular precio estandar
        precio_base = super().calcular_precio(vehiculo, hora_ingreso, hora_egreso)

        # Aplicar descuento
        descuento = precio_base * DESCUENTO_HAPPY_HOUR
        precio_final = precio_base - descuento

        return round(precio_final, 2)


# ================================================================================
# ARCHIVO 4/5: pricing_standard_strategy.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\pricing_standard_strategy.py
# ================================================================================

"""Estrategia de precio estandar.

Calcula el precio basado en la tarifa base del vehiculo y el tiempo de estadia.
"""

# Standard library
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Local application
from python_estacionamiento.patrones.strategy.pricing_strategy import PricingStrategy

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingStandardStrategy(PricingStrategy):
    """Estrategia de precio estandar.

    Calcula: tarifa_base_por_hora * horas_de_estadia
    Considera tolerancia en minutos sin cargo.
    """

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio estandar.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio calculado considerando tolerancia
        """
        # Calcular tiempo de estadia en minutos
        delta = hora_egreso - hora_ingreso
        minutos_totales = delta.total_seconds() / 60.0

        # Restar tolerancia
        minutos_cobrables = max(0, minutos_totales - vehiculo.get_tolerancia_minutos())

        # Convertir a horas y calcular precio
        horas = minutos_cobrables / 60.0
        precio = vehiculo.get_tarifa_base() * horas

        return round(precio, 2)


# ================================================================================
# ARCHIVO 5/5: pricing_valet_strategy.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\pricing_valet_strategy.py
# ================================================================================

"""Estrategia de precio con recargo de valet.

Aplica recargo por servicio de valet parking.
"""

# Standard library
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Local application
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.constantes import RECARGO_VALET

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingValetStrategy(PricingStandardStrategy):
    """Estrategia de precio con recargo de valet.

    Aplica recargo sobre el precio estandar por servicio premium.
    """

    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio con recargo de valet.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso
            hora_egreso: Hora de egreso

        Returns:
            Precio con recargo aplicado
        """
        # Calcular precio estandar
        precio_base = super().calcular_precio(vehiculo, hora_ingreso, hora_egreso)

        # Aplicar recargo
        recargo = precio_base * RECARGO_VALET
        precio_final = precio_base + recargo

        return round(precio_final, 2)


