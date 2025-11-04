"""Tests para ParkingLotManager.

Verifica que el gestor del estacionamiento funciona correctamente.
"""

# Standard library
import sys
from pathlib import Path

# Agregar el directorio raiz al path para imports
root_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_dir))

# Local application
from python_estacionamiento.servicios.parking_lot_manager import ParkingLotManager
from python_estacionamiento.patrones.factory.vehiculo_factory import VehiculoFactory
from python_estacionamiento.excepciones.estacionamiento_exception import (
    PlazasAgotadasException,
    VehiculoNoEncontradoException
)


def test_ingresar_vehiculo():
    """Verifica que un vehiculo puede ingresar."""
    manager = ParkingLotManager.get_instance()
    manager.reset()  # Limpiar estado previo

    moto = VehiculoFactory.crear_vehiculo("Moto", "TEST001")

    plazas_antes = manager.get_plazas_disponibles()
    manager.ingresar_vehiculo(moto)
    plazas_despues = manager.get_plazas_disponibles()

    assert plazas_despues == plazas_antes - 1
    assert manager.get_plazas_ocupadas() == 1
    assert moto.get_hora_ingreso() is not None


def test_egresar_vehiculo():
    """Verifica que un vehiculo puede egresar."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    auto = VehiculoFactory.crear_vehiculo("Auto", "TEST002")
    manager.ingresar_vehiculo(auto)

    plazas_antes = manager.get_plazas_disponibles()
    vehiculo_egresado = manager.egresar_vehiculo("TEST002")
    plazas_despues = manager.get_plazas_disponibles()

    assert plazas_despues == plazas_antes + 1
    assert manager.get_plazas_ocupadas() == 0
    assert vehiculo_egresado.get_hora_egreso() is not None


def test_vehiculo_no_encontrado():
    """Verifica que se lanza excepcion si vehiculo no existe."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    try:
        manager.egresar_vehiculo("NOEXISTE")
        assert False, "Deberia haber lanzado VehiculoNoEncontradoException"
    except VehiculoNoEncontradoException as e:
        assert "NOEXISTE" in e.get_patente()


def test_obtener_vehiculo():
    """Verifica que se puede buscar un vehiculo."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    camioneta = VehiculoFactory.crear_vehiculo("Camioneta", "TEST003")
    manager.ingresar_vehiculo(camioneta)

    vehiculo_encontrado = manager.get_vehiculo("TEST003")

    assert vehiculo_encontrado is not None
    assert vehiculo_encontrado.get_patente() == "TEST003"


def test_vehiculo_no_existe_retorna_none():
    """Verifica que buscar vehiculo inexistente retorna None."""
    manager = ParkingLotManager.get_instance()
    manager.reset()

    vehiculo = manager.get_vehiculo("INEXISTENTE")

    assert vehiculo is None


if __name__ == "__main__":
    test_ingresar_vehiculo()
    test_egresar_vehiculo()
    test_vehiculo_no_encontrado()
    test_obtener_vehiculo()
    test_vehiculo_no_existe_retorna_none()
    print("[OK] Todos los tests de ParkingLotManager pasaron")
