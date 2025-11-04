"""Tests para el sistema de persistencia.

Verifica que el guardado y carga de estado funciona correctamente.
"""

# Standard library
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_dir))

# Local application
from python_estacionamiento.servicios.parking_lot_manager import ParkingLotManager
from python_estacionamiento.patrones.factory.vehiculo_factory import VehiculoFactory


def test_guardar_estado():
    """Verifica que se puede guardar el estado."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    # Ingresar algunos vehículos
    vehiculos = [
        VehiculoFactory.crear_vehiculo("Moto", "PERSIST001"),
        VehiculoFactory.crear_vehiculo("Auto", "PERSIST002"),
        VehiculoFactory.crear_vehiculo("Camioneta", "PERSIST003")
    ]

    for v in vehiculos:
        manager.ingresar_vehiculo(v)

    # Guardar estado
    resultado = manager.guardar_estado()

    assert resultado is True
    print(f"[OK] Estado guardado: {len(vehiculos)} vehículos")


def test_cargar_estado():
    """Verifica que se puede cargar el estado guardado."""
    manager = ParkingLotManager.get_instance()

    # Limpiar primero
    manager.reset()

    # Cargar estado guardado
    resultado = manager.cargar_estado()

    assert resultado is True

    # Verificar que los vehículos se cargaron
    vehiculos_cargados = manager.get_todos_vehiculos()

    assert len(vehiculos_cargados) == 3
    assert "PERSIST001" in vehiculos_cargados
    assert "PERSIST002" in vehiculos_cargados
    assert "PERSIST003" in vehiculos_cargados

    print(f"[OK] Estado cargado: {len(vehiculos_cargados)} vehículos restaurados")


def test_ciclo_completo_persistencia():
    """Verifica un ciclo completo de guardar y cargar."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    # Paso 1: Ingresar vehículos
    patentes_originales = ["CICLO001", "CICLO002", "CICLO003", "CICLO004", "CICLO005"]
    for i, patente in enumerate(patentes_originales):
        tipo = ["Moto", "Auto", "Camioneta"][i % 3]
        vehiculo = VehiculoFactory.crear_vehiculo(tipo, patente)
        manager.ingresar_vehiculo(vehiculo)

    plazas_ocupadas_antes = manager.get_plazas_ocupadas()

    # Paso 2: Guardar
    assert manager.guardar_estado() is True

    # Paso 3: Resetear (simular reinicio)
    manager.reset()
    assert manager.get_plazas_ocupadas() == 0

    # Paso 4: Cargar
    assert manager.cargar_estado() is True

    # Paso 5: Verificar
    plazas_ocupadas_despues = manager.get_plazas_ocupadas()
    vehiculos_restaurados = manager.get_todos_vehiculos()

    assert plazas_ocupadas_despues == plazas_ocupadas_antes
    assert len(vehiculos_restaurados) == len(patentes_originales)

    for patente in patentes_originales:
        assert patente in vehiculos_restaurados

    print(f"[OK] Ciclo completo: {plazas_ocupadas_antes} -> {plazas_ocupadas_despues} plazas")


if __name__ == "__main__":
    print("\n=============== TESTS DE PERSISTENCIA ===============\n")

    test_guardar_estado()
    test_cargar_estado()
    test_ciclo_completo_persistencia()

    print("\n[OK] Todos los tests de persistencia pasaron")
    print("     - Guardado de estado funcional")
    print("     - Carga de estado funcional")
    print("     - Integridad de datos mantenida")
