"""Tests de concurrencia y thread-safety.

Verifica que el sistema funciona correctamente con múltiples hilos.
"""

# Standard library
import sys
from pathlib import Path
from threading import Thread
from time import sleep

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_dir))

# Local application
from python_estacionamiento.servicios.parking_lot_manager import ParkingLotManager
from python_estacionamiento.servicios.pricing_registry import PricingRegistry
from python_estacionamiento.patrones.factory.vehiculo_factory import VehiculoFactory


def test_singleton_thread_safety():
    """Verifica que Singleton es thread-safe."""
    instancias = []

    def obtener_instancia():
        """Obtiene instancia en hilo separado."""
        manager = ParkingLotManager.get_instance()
        instancias.append(manager)

    # Crear múltiples hilos
    hilos = [Thread(target=obtener_instancia) for _ in range(10)]

    # Iniciar todos los hilos simultáneamente
    for hilo in hilos:
        hilo.start()

    # Esperar a que terminen
    for hilo in hilos:
        hilo.join()

    # Verificar que todas las instancias son la misma
    primera_instancia = instancias[0]
    for instancia in instancias:
        assert instancia is primera_instancia
        assert id(instancia) == id(primera_instancia)

    print(f"[OK] Singleton thread-safe: {len(instancias)} hilos, 1 instancia única")


def test_ingreso_concurrente():
    """Verifica ingreso concurrente de vehículos."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    resultados = {'exitos': 0, 'errores': 0}

    def ingresar_vehiculo(numero: int):
        """Ingresa un vehículo en hilo separado."""
        try:
            vehiculo = VehiculoFactory.crear_vehiculo("Auto", f"THREAD{numero:03d}")
            manager.ingresar_vehiculo(vehiculo)
            resultados['exitos'] += 1
        except Exception:
            resultados['errores'] += 1

    # Crear 20 hilos intentando ingresar vehículos
    hilos = [Thread(target=ingresar_vehiculo, args=(i,)) for i in range(20)]

    # Iniciar todos
    for hilo in hilos:
        hilo.start()

    # Esperar
    for hilo in hilos:
        hilo.join()

    # Verificar consistencia
    plazas_ocupadas = manager.get_plazas_ocupadas()
    vehiculos_activos = len(manager.get_todos_vehiculos())

    assert plazas_ocupadas == vehiculos_activos
    assert plazas_ocupadas == resultados['exitos']

    print(f"[OK] Ingreso concurrente: {resultados['exitos']} éxitos, {resultados['errores']} errores")
    print(f"    Plazas ocupadas: {plazas_ocupadas}")


def test_egreso_concurrente():
    """Verifica egreso concurrente de vehículos."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    # Primero ingresar vehículos secuencialmente
    patentes = []
    for i in range(10):
        patente = f"EGRESO{i:03d}"
        vehiculo = VehiculoFactory.crear_vehiculo("Moto", patente)
        manager.ingresar_vehiculo(vehiculo)
        patentes.append(patente)

    sleep(0.1)  # Pequeña pausa para asegurar tiempo de estadía

    resultados = {'exitos': 0, 'errores': 0}

    def egresar_vehiculo(patente: str):
        """Egresa un vehículo en hilo separado."""
        try:
            manager.egresar_vehiculo(patente)
            resultados['exitos'] += 1
        except Exception:
            resultados['errores'] += 1

    # Crear hilos para egresar
    hilos = [Thread(target=egresar_vehiculo, args=(p,)) for p in patentes]

    # Iniciar todos
    for hilo in hilos:
        hilo.start()

    # Esperar
    for hilo in hilos:
        hilo.join()

    # Verificar que todos egresaron
    assert manager.get_plazas_ocupadas() == 0
    assert len(manager.get_todos_vehiculos()) == 0
    assert resultados['exitos'] == 10

    print(f"[OK] Egreso concurrente: {resultados['exitos']} éxitos")


def test_operaciones_mixtas_concurrentes():
    """Verifica operaciones mixtas concurrentes."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    # Pre-cargar algunos vehículos
    patentes_existentes = []
    for i in range(5):
        patente = f"PRELOAD{i:03d}"
        vehiculo = VehiculoFactory.crear_vehiculo("Camioneta", patente)
        manager.ingresar_vehiculo(vehiculo)
        patentes_existentes.append(patente)

    sleep(0.1)

    def operacion_mixta(numero: int):
        """Realiza operaciones mixtas."""
        try:
            if numero % 2 == 0:
                # Ingresar nuevo vehículo
                vehiculo = VehiculoFactory.crear_vehiculo("Auto", f"MIXTO{numero:03d}")
                manager.ingresar_vehiculo(vehiculo)
            else:
                # Consultar vehículo existente
                if numero < len(patentes_existentes):
                    manager.get_vehiculo(patentes_existentes[numero])
        except Exception:
            pass

    # Crear 15 hilos con operaciones mixtas
    hilos = [Thread(target=operacion_mixta, args=(i,)) for i in range(15)]

    plazas_antes = manager.get_plazas_ocupadas()

    # Ejecutar
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    plazas_despues = manager.get_plazas_ocupadas()

    # Verificar consistencia (no crashes, no inconsistencias)
    assert manager.get_plazas_ocupadas() == len(manager.get_todos_vehiculos())
    assert plazas_despues >= plazas_antes  # Solo agregamos, no quitamos

    print(f"[OK] Operaciones mixtas: {plazas_antes} -> {plazas_despues} plazas")


def test_pricing_registry_thread_safety():
    """Verifica que PricingRegistry es thread-safe."""
    instancias = []

    def obtener_registry():
        """Obtiene registry en hilo separado."""
        registry = PricingRegistry.get_instance()
        instancias.append(registry)

    # Crear hilos
    hilos = [Thread(target=obtener_registry) for _ in range(10)]

    # Ejecutar
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    # Verificar unicidad
    primera = instancias[0]
    for instancia in instancias:
        assert instancia is primera

    print(f"[OK] PricingRegistry thread-safe: {len(instancias)} hilos, 1 instancia")


if __name__ == "__main__":
    print("\n=============== TESTS DE CONCURRENCIA Y THREAD-SAFETY ===============\n")

    test_singleton_thread_safety()
    test_pricing_registry_thread_safety()
    test_ingreso_concurrente()
    test_egreso_concurrente()
    test_operaciones_mixtas_concurrentes()

    print("\n[OK] Todos los tests de concurrencia pasaron")
    print("     - Singleton thread-safe verificado")
    print("     - Operaciones concurrentes sin race conditions")
    print("     - Consistencia de datos mantenida")
