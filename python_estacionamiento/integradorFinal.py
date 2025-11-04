"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento
Fecha de generacion: 2025-11-04 15:58:22
Total de archivos integrados: 37
Total de directorios procesados: 15
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================


# DIRECTORIO: ..
#   1. main.py
#
# DIRECTORIO: .
#   2. __init__.py
#   3. constantes.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades\vehiculos
#   5. __init__.py
#   6. auto.py
#   7. camioneta.py
#   8. moto.py
#   9. vehiculo.py
#
# DIRECTORIO: excepciones
#   10. __init__.py
#   11. estacionamiento_exception.py
#
# DIRECTORIO: patrones
#   12. __init__.py
#
# DIRECTORIO: patrones\factory
#   13. __init__.py
#   14. vehiculo_factory.py
#
# DIRECTORIO: patrones\observer
#   15. __init__.py
#   16. observable.py
#   17. observer.py
#
# DIRECTORIO: patrones\singleton
#   18. __init__.py
#
# DIRECTORIO: patrones\strategy
#   19. __init__.py
#   20. pricing_strategy.py
#
# DIRECTORIO: patrones\strategy\impl
#   21. __init__.py
#   22. pricing_evento_strategy.py
#   23. pricing_happy_hour_strategy.py
#   24. pricing_standard_strategy.py
#   25. pricing_valet_strategy.py
#
# DIRECTORIO: persistencia
#   26. __init__.py
#   27. json_storage.py
#
# DIRECTORIO: sensores
#   28. __init__.py
#   29. eventos.py
#   30. sensor_camara.py
#   31. sensor_ocupacion.py
#   32. sensor_seguridad.py
#
# DIRECTORIO: servicios
#   33. __init__.py
#   34. parking_lot_manager.py
#   35. pricing_registry.py
#
# DIRECTORIO: utils
#   36. __init__.py
#   37. logger.py
#

################################################################################
# DIRECTORIO: ..
################################################################################

# ==============================================================================
# ARCHIVO 1/37: main.py
# Directorio: ..
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\main.py
# ==============================================================================

"""Sistema de Gestion de Estacionamiento - Demostracion de Patrones de Diseno.

Este archivo demuestra el uso de los cuatro patrones de diseno principales:
- SINGLETON: ParkingLotManager y PricingRegistry con instancia unica
- FACTORY: VehiculoFactory para crear vehiculos
- OBSERVER: Sensores para monitoreo (preparado para expansion)
- STRATEGY: Estrategias de precio diferenciadas
"""

# Standard library
from __future__ import annotations
from datetime import datetime, timedelta

# Local application
from python_estacionamiento.patrones.factory.vehiculo_factory import VehiculoFactory
from python_estacionamiento.servicios.parking_lot_manager import ParkingLotManager
from python_estacionamiento.servicios.pricing_registry import PricingRegistry
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.patrones.strategy.impl.pricing_happy_hour_strategy import PricingHappyHourStrategy
from python_estacionamiento.patrones.strategy.impl.pricing_valet_strategy import PricingValetStrategy
from python_estacionamiento.patrones.strategy.impl.pricing_evento_strategy import PricingEventoStrategy


def imprimir_separador(titulo: str = "", caracter: str = "=", ancho: int = 70) -> None:
    """Imprime un separador visual."""
    if titulo:
        padding = (ancho - len(titulo) - 2) // 2
        print(f"{caracter * padding} {titulo} {caracter * padding}")
    else:
        print(caracter * ancho)


def main():
    """Funcion principal que demuestra todos los patrones."""

    imprimir_separador("SISTEMA DE GESTION DE ESTACIONAMIENTO")
    print()

    # =========================================================================
    # PATRON SINGLETON: Verificar instancia unica de los gestores
    # =========================================================================
    imprimir_separador("PATRON SINGLETON: Inicializando gestores", "-")

    parking_manager1 = ParkingLotManager.get_instance()
    parking_manager2 = ParkingLotManager.get_instance()

    pricing_registry1 = PricingRegistry.get_instance()
    pricing_registry2 = PricingRegistry.get_instance()

    if parking_manager1 is parking_manager2:
        print("[OK] SINGLETON verificado: ParkingLotManager tiene instancia unica")
        print(f"     ID de parking_manager1: {id(parking_manager1)}")
        print(f"     ID de parking_manager2: {id(parking_manager2)}")
    else:
        print("[ERROR] SINGLETON fallo en ParkingLotManager")

    if pricing_registry1 is pricing_registry2:
        print("[OK] SINGLETON verificado: PricingRegistry tiene instancia unica")
        print(f"     ID de pricing_registry1: {id(pricing_registry1)}")
        print(f"     ID de pricing_registry2: {id(pricing_registry2)}")
    else:
        print("[ERROR] SINGLETON fallo en PricingRegistry")

    print()

    # =========================================================================
    # PATRON FACTORY: Crear vehiculos usando Factory Method
    # =========================================================================
    imprimir_separador("PATRON FACTORY: Creando vehiculos", "-")

    parking_manager = ParkingLotManager.get_instance()

    print("\n1. Creando vehiculos usando VehiculoFactory...")
    try:
        # Crear diferentes tipos de vehiculos
        moto1 = VehiculoFactory.crear_vehiculo("Moto", "ABC123")
        auto1 = VehiculoFactory.crear_vehiculo("Auto", "XYZ789")
        camioneta1 = VehiculoFactory.crear_vehiculo("Camioneta", "DEF456")

        print(f"[OK] FACTORY verificado: Creados 3 vehiculos")
        print(f"     - Moto: {moto1.get_patente()} (tarifa base: ${moto1.get_tarifa_base()}/hora)")
        print(f"     - Auto: {auto1.get_patente()} (tarifa base: ${auto1.get_tarifa_base()}/hora)")
        print(f"     - Camioneta: {camioneta1.get_patente()} (tarifa base: ${camioneta1.get_tarifa_base()}/hora)")
    except Exception as e:
        print(f"[ERROR] FACTORY fallo: {e}")

    print()

    # =========================================================================
    # Ingresar vehiculos al estacionamiento
    # =========================================================================
    imprimir_separador("Ingresando vehiculos al estacionamiento", "-")

    print(f"\nPlazas disponibles antes del ingreso: {parking_manager.get_plazas_disponibles()}")

    try:
        parking_manager.ingresar_vehiculo(moto1)
        print(f"[OK] Moto {moto1.get_patente()} ingresada")

        parking_manager.ingresar_vehiculo(auto1)
        print(f"[OK] Auto {auto1.get_patente()} ingresado")

        parking_manager.ingresar_vehiculo(camioneta1)
        print(f"[OK] Camioneta {camioneta1.get_patente()} ingresada")

        print(f"\nPlazas disponibles despues del ingreso: {parking_manager.get_plazas_disponibles()}")
        print(f"Plazas ocupadas: {parking_manager.get_plazas_ocupadas()}")
    except Exception as e:
        print(f"[ERROR] al ingresar vehiculos: {e}")

    print()

    # =========================================================================
    # PATRON STRATEGY: Calcular precios con diferentes estrategias
    # =========================================================================
    imprimir_separador("PATRON STRATEGY: Estrategias de precio", "-")

    pricing_registry = PricingRegistry.get_instance()

    # Simular una estadia de 2 horas para el auto
    hora_ingreso = datetime.now() - timedelta(hours=2)
    hora_egreso = datetime.now()

    print("\n2. Calculando precios con diferentes estrategias...")
    print(f"   Vehiculo: Auto {auto1.get_patente()}")
    print(f"   Tiempo de estadia: 2 horas")
    print()

    # Estrategia 1: Precio Estandar
    pricing_registry.set_estrategia(PricingStandardStrategy())
    precio_estandar = pricing_registry.calcular_precio(auto1, hora_ingreso, hora_egreso)
    print(f"   - Estrategia ESTANDAR: ${precio_estandar}")

    # Estrategia 2: Happy Hour (descuento)
    pricing_registry.set_estrategia(PricingHappyHourStrategy())
    precio_happy_hour = pricing_registry.calcular_precio(auto1, hora_ingreso, hora_egreso)
    print(f"   - Estrategia HAPPY HOUR (20% desc): ${precio_happy_hour}")

    # Estrategia 3: Valet (recargo)
    pricing_registry.set_estrategia(PricingValetStrategy())
    precio_valet = pricing_registry.calcular_precio(auto1, hora_ingreso, hora_egreso)
    print(f"   - Estrategia VALET (30% rec): ${precio_valet}")

    # Estrategia 4: Evento Especial (recargo mayor)
    pricing_registry.set_estrategia(PricingEventoStrategy())
    precio_evento = pricing_registry.calcular_precio(auto1, hora_ingreso, hora_egreso)
    print(f"   - Estrategia EVENTO (50% rec): ${precio_evento}")

    print("\n[OK] STRATEGY verificado: 4 estrategias implementadas y funcionando")

    print()

    # =========================================================================
    # Egresar vehiculos y cobrar
    # =========================================================================
    imprimir_separador("Egreso de vehiculos y facturacion", "-")

    # Volver a estrategia estandar para el cobro
    pricing_registry.set_estrategia(PricingStandardStrategy())

    print(f"\n3. Egresando vehiculos y calculando cobro...")

    try:
        # Egresar moto
        moto_egresada = parking_manager.egresar_vehiculo(moto1.get_patente())
        precio_moto = pricing_registry.calcular_precio(
            moto_egresada,
            moto_egresada.get_hora_ingreso(),
            moto_egresada.get_hora_egreso()
        )
        print(f"\n[OK] Moto {moto_egresada.get_patente()} egresada")
        print(f"     Precio a cobrar: ${precio_moto}")

        # Egresar auto
        auto_egresado = parking_manager.egresar_vehiculo(auto1.get_patente())
        precio_auto = pricing_registry.calcular_precio(
            auto_egresado,
            auto_egresado.get_hora_ingreso(),
            auto_egresado.get_hora_egreso()
        )
        print(f"\n[OK] Auto {auto_egresado.get_patente()} egresado")
        print(f"     Precio a cobrar: ${precio_auto}")

        # Egresar camioneta
        camioneta_egresada = parking_manager.egresar_vehiculo(camioneta1.get_patente())
        precio_camioneta = pricing_registry.calcular_precio(
            camioneta_egresada,
            camioneta_egresada.get_hora_ingreso(),
            camioneta_egresada.get_hora_egreso()
        )
        print(f"\n[OK] Camioneta {camioneta_egresada.get_patente()} egresada")
        print(f"     Precio a cobrar: ${precio_camioneta}")

        print(f"\nPlazas disponibles despues del egreso: {parking_manager.get_plazas_disponibles()}")
        print(f"Plazas ocupadas: {parking_manager.get_plazas_ocupadas()}")
    except Exception as e:
        print(f"[ERROR] al egresar vehiculos: {e}")

    print()

    # =========================================================================
    # PATRON OBSERVER: Sistema de sensores en accion
    # =========================================================================
    imprimir_separador("PATRON OBSERVER: Sistema de sensores", "-")

    # Importar sensores
    from python_estacionamiento.sensores.sensor_ocupacion import SensorOcupacion
    from python_estacionamiento.sensores.sensor_camara import SensorCamara
    from python_estacionamiento.sensores.sensor_seguridad import SensorSeguridad

    print("\n4. Inicializando sensores del estacionamiento...")
    print()

    # Crear sensores (Observers)
    sensor_ocupacion = SensorOcupacion(umbral_critico=10)
    sensor_camara = SensorCamara(ubicacion="Principal")
    sensor_seguridad = SensorSeguridad()

    print()

    # Suscribir sensores al parking manager (Observable)
    parking_manager.agregar_observador(sensor_ocupacion)
    parking_manager.agregar_observador(sensor_camara)
    parking_manager.agregar_observador(sensor_seguridad)

    print("\n[OK] OBSERVER verificado: 3 sensores suscritos al estacionamiento")
    print()

    # Resetear el parking para demostrar sensores
    parking_manager.reset()

    print("\n5. Demostrando sensores en tiempo real...")
    imprimir_separador("", "-")

    # Crear nuevos vehiculos para demostrar sensores
    print("\n--- Ingresando vehiculos (sensores activos) ---\n")

    moto2 = VehiculoFactory.crear_vehiculo("Moto", "MOT999")
    auto2 = VehiculoFactory.crear_vehiculo("Auto", "AUT888")
    camioneta2 = VehiculoFactory.crear_vehiculo("Camioneta", "CAM777")

    parking_manager.ingresar_vehiculo(moto2)
    print()

    parking_manager.ingresar_vehiculo(auto2)
    print()

    parking_manager.ingresar_vehiculo(camioneta2)
    print()

    print("--- Egresando vehiculos (sensores activos) ---\n")

    parking_manager.egresar_vehiculo(moto2.get_patente())
    print()

    parking_manager.egresar_vehiculo(auto2.get_patente())
    print()

    print("[OK] OBSERVER verificado: Sensores notificados de todos los eventos")
    print()

    # =========================================================================
    # RESUMEN FINAL
    # =========================================================================
    imprimir_separador("EJEMPLO COMPLETADO EXITOSAMENTE")

    print("\n  [OK] SINGLETON   - ParkingLotManager y PricingRegistry (instancias unicas)")
    print("  [OK] FACTORY     - Creacion de vehiculos (Moto, Auto, Camioneta)")
    print("  [OK] OBSERVER    - Sistema de sensores funcionando (Ocupacion, Camaras, Seguridad)")
    print("  [OK] STRATEGY    - Estrategias de precio (Estandar, Happy Hour, Valet, Evento)")

    imprimir_separador()

    print("\n[INFO] Estructura del proyecto:")
    print("  - python_estacionamiento/entidades/     : Entidades de dominio")
    print("  - python_estacionamiento/servicios/     : Servicios de negocio")
    print("  - python_estacionamiento/patrones/      : Implementaciones de patrones")
    print("  - python_estacionamiento/sensores/      : Sistema de sensores (IMPLEMENTADO)")
    print("  - python_estacionamiento/persistencia/  : Sistema de persistencia JSON (IMPLEMENTADO)")
    print("  - python_estacionamiento/utils/         : Sistema de logging (IMPLEMENTADO)")
    print("  - python_estacionamiento/excepciones/   : Excepciones personalizadas")
    print("  - python_estacionamiento/constantes.py  : Constantes centralizadas")
    print("  - tests/                                : Suite completa de tests unitarios")
    print()


if __name__ == "__main__":
    main()



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 2/37: __init__.py
# Directorio: .
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 3/37: constantes.py
# Directorio: .
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\constantes.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/37: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\__init__.py
# ==============================================================================

# Standard library

# Local application



################################################################################
# DIRECTORIO: entidades\vehiculos
################################################################################

# ==============================================================================
# ARCHIVO 5/37: __init__.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 6/37: auto.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\auto.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 7/37: camioneta.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\camioneta.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 8/37: moto.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\moto.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 9/37: vehiculo.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\entidades\vehiculos\vehiculo.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 10/37: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\excepciones\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 11/37: estacionamiento_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\excepciones\estacionamiento_exception.py
# ==============================================================================

"""Excepciones personalizadas del sistema de estacionamiento."""

# Standard library
from __future__ import annotations


class EstacionamientoException(Exception):
    """Excepcion base para el sistema de estacionamiento."""

    def __init__(self, mensaje: str):
        """Inicializa la excepcion.

        Args:
            mensaje: Mensaje de error
        """
        super().__init__(mensaje)
        self._mensaje = mensaje

    def get_mensaje(self) -> str:
        """Obtiene el mensaje de error."""
        return self._mensaje


class PlazasAgotadasException(EstacionamientoException):
    """Excepcion lanzada cuando no hay plazas disponibles."""

    def __init__(self, plazas_disponibles: int):
        """Inicializa la excepcion.

        Args:
            plazas_disponibles: Cantidad de plazas disponibles
        """
        super().__init__(f"No hay plazas disponibles. Plazas actuales: {plazas_disponibles}")
        self._plazas_disponibles = plazas_disponibles

    def get_plazas_disponibles(self) -> int:
        """Obtiene las plazas disponibles."""
        return self._plazas_disponibles


class VehiculoNoEncontradoException(EstacionamientoException):
    """Excepcion lanzada cuando un vehiculo no se encuentra en el estacionamiento."""

    def __init__(self, patente: str):
        """Inicializa la excepcion.

        Args:
            patente: Patente del vehiculo no encontrado
        """
        super().__init__(f"Vehiculo con patente {patente} no encontrado en el estacionamiento")
        self._patente = patente

    def get_patente(self) -> str:
        """Obtiene la patente del vehiculo."""
        return self._patente



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 12/37: __init__.py
# Directorio: patrones
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\__init__.py
# ==============================================================================

# Standard library

# Local application



################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 13/37: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\factory\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 14/37: vehiculo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\factory\vehiculo_factory.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 15/37: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\observer\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 16/37: observable.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\observer\observable.py
# ==============================================================================

"""Patron Observer - Clase Observable.

Define la clase base para objetos observables.
"""

# Standard library
from __future__ import annotations
from abc import ABC
from typing import List, TypeVar, Generic, TYPE_CHECKING

if TYPE_CHECKING:
    from python_estacionamiento.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """Clase base Observable generica.

    Los observables mantienen una lista de observadores y los notifican
    cuando su estado cambia.
    """

    def __init__(self):
        """Inicializa el observable con una lista vacia de observadores."""
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un observador a la lista.

        Args:
            observador: El observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista.

        Args:
            observador: El observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores de un cambio.

        Args:
            evento: El evento o dato a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)


# ==============================================================================
# ARCHIVO 17/37: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\observer\observer.py
# ==============================================================================

"""Patron Observer - Interfaz Observer.

Define la interfaz que deben implementar todos los observadores.
"""

# Standard library
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """Interfaz Observer generica.

    Los observadores implementan esta interfaz para recibir notificaciones
    cuando el estado del observable cambia.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Metodo llamado cuando el observable notifica un cambio.

        Args:
            evento: El evento o dato notificado por el observable
        """
        pass



################################################################################
# DIRECTORIO: patrones\singleton
################################################################################

# ==============================================================================
# ARCHIVO 18/37: __init__.py
# Directorio: patrones\singleton
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\singleton\__init__.py
# ==============================================================================

# Standard library

# Local application



################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 19/37: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 20/37: pricing_strategy.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\pricing_strategy.py
# ==============================================================================

"""Patron Strategy - Interfaz PricingStrategy.

Define la interfaz para estrategias de calculo de precios.
"""

# Standard library
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_estacionamiento.entidades.vehiculos.vehiculo import Vehiculo


class PricingStrategy(ABC):
    """Interfaz Strategy para calcular precios.

    Define el contrato que deben cumplir todas las estrategias de precios.
    """

    @abstractmethod
    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        """Calcula el precio a cobrar por el estacionamiento.

        Args:
            vehiculo: El vehiculo a calcular
            hora_ingreso: Hora de ingreso al estacionamiento
            hora_egreso: Hora de egreso del estacionamiento

        Returns:
            El precio total a cobrar
        """
        pass



################################################################################
# DIRECTORIO: patrones\strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 21/37: __init__.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 22/37: pricing_evento_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\pricing_evento_strategy.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 23/37: pricing_happy_hour_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\pricing_happy_hour_strategy.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 24/37: pricing_standard_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\pricing_standard_strategy.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 25/37: pricing_valet_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\patrones\strategy\impl\pricing_valet_strategy.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: persistencia
################################################################################

# ==============================================================================
# ARCHIVO 26/37: __init__.py
# Directorio: persistencia
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\persistencia\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 27/37: json_storage.py
# Directorio: persistencia
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\persistencia\json_storage.py
# ==============================================================================

"""Sistema de persistencia con JSON.

Permite guardar y cargar el estado del estacionamiento.
"""

# Standard library
import json
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

# Local application
from python_estacionamiento.utils.logger import configurar_logger


class JsonStorage:
    """Gestor de persistencia JSON."""

    def __init__(self, archivo: str = "estacionamiento_estado.json"):
        """Inicializa el gestor de persistencia.

        Args:
            archivo: Nombre del archivo JSON
        """
        self._logger = configurar_logger('JsonStorage')
        self._archivo_path = Path(__file__).parent.parent.parent / 'data' / archivo
        self._archivo_path.parent.mkdir(parents=True, exist_ok=True)

    def guardar_estado(self, estado: Dict[str, Any]) -> bool:
        """Guarda el estado del estacionamiento.

        Args:
            estado: Diccionario con el estado a guardar

        Returns:
            True si se guardó correctamente, False si hubo error
        """
        try:
            # Convertir datetime a string para JSON
            estado_serializable = self._preparar_para_json(estado)

            with open(self._archivo_path, 'w', encoding='utf-8') as f:
                json.dump(estado_serializable, f, indent=2, ensure_ascii=False)

            self._logger.info(f'Estado guardado correctamente en {self._archivo_path}')
            return True

        except Exception as e:
            self._logger.error(f'Error al guardar estado: {e}')
            return False

    def cargar_estado(self) -> Dict[str, Any] | None:
        """Carga el estado del estacionamiento.

        Returns:
            Diccionario con el estado cargado, None si no existe o hay error
        """
        try:
            if not self._archivo_path.exists():
                self._logger.warning(f'Archivo de estado no encontrado: {self._archivo_path}')
                return None

            with open(self._archivo_path, 'r', encoding='utf-8') as f:
                estado = json.load(f)

            # Convertir strings a datetime
            estado_restaurado = self._restaurar_desde_json(estado)

            self._logger.info(f'Estado cargado correctamente desde {self._archivo_path}')
            return estado_restaurado

        except Exception as e:
            self._logger.error(f'Error al cargar estado: {e}')
            return None

    def eliminar_estado(self) -> bool:
        """Elimina el archivo de estado.

        Returns:
            True si se eliminó correctamente, False si no existe o hay error
        """
        try:
            if self._archivo_path.exists():
                self._archivo_path.unlink()
                self._logger.info(f'Estado eliminado: {self._archivo_path}')
                return True
            else:
                self._logger.warning('Archivo de estado no existe, nada que eliminar')
                return False

        except Exception as e:
            self._logger.error(f'Error al eliminar estado: {e}')
            return False

    def _preparar_para_json(self, estado: Dict[str, Any]) -> Dict[str, Any]:
        """Prepara el estado para serialización JSON.

        Args:
            estado: Estado original

        Returns:
            Estado serializable
        """
        estado_json = {
            'timestamp': datetime.now().isoformat(),
            'plazas_ocupadas': estado.get('plazas_ocupadas', 0),
            'capacidad_maxima': estado.get('capacidad_maxima', 100),
            'vehiculos': []
        }

        # Serializar vehículos
        vehiculos = estado.get('vehiculos', {})
        for patente, vehiculo in vehiculos.items():
            vehiculo_data = {
                'patente': patente,
                'tipo': vehiculo.__class__.__name__,
                'superficie': vehiculo.get_superficie(),
                'tarifa_base': vehiculo.get_tarifa_base(),
                'hora_ingreso': vehiculo.get_hora_ingreso().isoformat() if vehiculo.get_hora_ingreso() else None,
                'hora_egreso': vehiculo.get_hora_egreso().isoformat() if vehiculo.get_hora_egreso() else None
            }

            # Agregar atributos específicos por tipo
            if hasattr(vehiculo, 'get_cilindrada'):
                vehiculo_data['cilindrada'] = vehiculo.get_cilindrada()
            elif hasattr(vehiculo, 'get_marca'):
                vehiculo_data['marca'] = vehiculo.get_marca()
            elif hasattr(vehiculo, 'get_capacidad_carga'):
                vehiculo_data['capacidad_carga'] = vehiculo.get_capacidad_carga()

            estado_json['vehiculos'].append(vehiculo_data)

        return estado_json

    def _restaurar_desde_json(self, estado_json: Dict[str, Any]) -> Dict[str, Any]:
        """Restaura el estado desde JSON.

        Args:
            estado_json: Estado en formato JSON

        Returns:
            Estado restaurado
        """
        estado = {
            'plazas_ocupadas': estado_json.get('plazas_ocupadas', 0),
            'capacidad_maxima': estado_json.get('capacidad_maxima', 100),
            'vehiculos_data': estado_json.get('vehiculos', []),
            'timestamp': estado_json.get('timestamp')
        }

        return estado

    def existe_estado(self) -> bool:
        """Verifica si existe un archivo de estado guardado.

        Returns:
            True si existe, False si no
        """
        return self._archivo_path.exists()



################################################################################
# DIRECTORIO: sensores
################################################################################

# ==============================================================================
# ARCHIVO 28/37: __init__.py
# Directorio: sensores
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\__init__.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 29/37: eventos.py
# Directorio: sensores
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\eventos.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 30/37: sensor_camara.py
# Directorio: sensores
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\sensor_camara.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 31/37: sensor_ocupacion.py
# Directorio: sensores
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\sensor_ocupacion.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 32/37: sensor_seguridad.py
# Directorio: sensores
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\sensores\sensor_seguridad.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 33/37: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\servicios\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 34/37: parking_lot_manager.py
# Directorio: servicios
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\servicios\parking_lot_manager.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 35/37: pricing_registry.py
# Directorio: servicios
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\servicios\pricing_registry.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: utils
################################################################################

# ==============================================================================
# ARCHIVO 36/37: __init__.py
# Directorio: utils
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\utils\__init__.py
# ==============================================================================

# Standard library

# Local application


# ==============================================================================
# ARCHIVO 37/37: logger.py
# Directorio: utils
# Ruta completa: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\utils\logger.py
# ==============================================================================

"""Sistema de logging centralizado.

Proporciona configuración de logging para todo el sistema.
"""

# Standard library
import logging
import sys
from pathlib import Path
from datetime import datetime


def configurar_logger(nombre: str, nivel: int = logging.INFO) -> logging.Logger:
    """Configura y retorna un logger.

    Args:
        nombre: Nombre del logger
        nivel: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        Logger configurado
    """
    logger = logging.getLogger(nombre)
    logger.setLevel(nivel)

    # Evitar duplicar handlers
    if logger.handlers:
        return logger

    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(nivel)

    # Handler para archivo
    logs_dir = Path(__file__).parent.parent.parent / 'logs'
    logs_dir.mkdir(exist_ok=True)

    fecha = datetime.now().strftime('%Y%m%d')
    file_handler = logging.FileHandler(
        logs_dir / f'estacionamiento_{fecha}.log',
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)

    # Formato de mensajes
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Agregar handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 37
# Generado: 2025-11-04 15:58:22
################################################################################
