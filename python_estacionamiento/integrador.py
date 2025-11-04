"""
Archivo integrador generado automaticamente
Directorio: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento
Fecha: 2025-11-04 15:58:22
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\__init__.py
# ================================================================================

# Standard library

# Local application


# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\constantes.py
# ================================================================================

"""Constantes centralizadas del sistema de gestion de estacionamiento.

Este modulo contiene todas las constantes utilizadas en el sistema,
centralizando valores magicos y configuraciones.
"""

# Standard library
from __future__ import annotations

# Configuracion del estacionamiento
CAPACIDAD_MAXIMA_PLAZAS = 100
AGUA_DISPONIBLE_INICIAL = 0  # No aplica para estacionamiento

# Tarifas base por tipo de vehiculo (en pesos por hora)
TARIFA_BASE_MOTO = 50.0
TARIFA_BASE_AUTO = 100.0
TARIFA_BASE_CAMIONETA = 150.0

# Espacios requeridos por tipo de vehiculo (en metros cuadrados)
SUPERFICIE_MOTO = 4.0
SUPERFICIE_AUTO = 12.0
SUPERFICIE_CAMIONETA = 20.0

# Tiempos de tolerancia (en minutos)
TOLERANCIA_MOTO = 10
TOLERANCIA_AUTO = 15
TOLERANCIA_CAMIONETA = 15

# Configuracion de sensores
INTERVALO_SENSOR_OCUPACION = 5.0  # segundos
INTERVALO_SENSOR_CAMARA = 3.0  # segundos
INTERVALO_VERIFICACION_SEGURIDAD = 10.0  # segundos

# Configuracion de precios especiales
DESCUENTO_HAPPY_HOUR = 0.20  # 20% de descuento
RECARGO_VALET = 0.30  # 30% de recargo
DESCUENTO_NOCTURNO = 0.15  # 15% de descuento
RECARGO_EVENTO_ESPECIAL = 0.50  # 50% de recargo

# Horarios especiales
HORA_INICIO_HAPPY_HOUR = 14
HORA_FIN_HAPPY_HOUR = 17
HORA_INICIO_NOCTURNO = 22
HORA_FIN_NOCTURNO = 6

# Configuracion de threading
THREAD_JOIN_TIMEOUT = 2.0

# Configuracion de persistencia
DIRECTORIO_PERSISTENCIA = "data"
EXTENSION_ARCHIVO = ".pkl"

__all__ = [
    "CAPACIDAD_MAXIMA_PLAZAS",
    "TARIFA_BASE_MOTO",
    "TARIFA_BASE_AUTO",
    "TARIFA_BASE_CAMIONETA",
    "SUPERFICIE_MOTO",
    "SUPERFICIE_AUTO",
    "SUPERFICIE_CAMIONETA",
    "TOLERANCIA_MOTO",
    "TOLERANCIA_AUTO",
    "TOLERANCIA_CAMIONETA",
    "INTERVALO_SENSOR_OCUPACION",
    "INTERVALO_SENSOR_CAMARA",
    "INTERVALO_VERIFICACION_SEGURIDAD",
    "DESCUENTO_HAPPY_HOUR",
    "RECARGO_VALET",
    "DESCUENTO_NOCTURNO",
    "RECARGO_EVENTO_ESPECIAL",
    "HORA_INICIO_HAPPY_HOUR",
    "HORA_FIN_HAPPY_HOUR",
    "HORA_INICIO_NOCTURNO",
    "HORA_FIN_NOCTURNO",
    "THREAD_JOIN_TIMEOUT",
    "DIRECTORIO_PERSISTENCIA",
    "EXTENSION_ARCHIVO",
]


