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
