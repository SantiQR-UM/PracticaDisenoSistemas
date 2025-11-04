"""Tests para el patron Factory Method.

Verifica que VehiculoFactory crea correctamente los diferentes
tipos de vehiculos.
"""

# Standard library
import sys
from pathlib import Path

# Agregar el directorio raiz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

# Local application
from python_estacionamiento.patrones.factory.vehiculo_factory import VehiculoFactory
from python_estacionamiento.entidades.vehiculos.moto import Moto
from python_estacionamiento.entidades.vehiculos.auto import Auto
from python_estacionamiento.entidades.vehiculos.camioneta import Camioneta


def test_crear_moto():
    """Verifica que Factory crea Moto correctamente."""
    vehiculo = VehiculoFactory.crear_vehiculo("Moto", "ABC123")

    assert isinstance(vehiculo, Moto)
    assert vehiculo.get_patente() == "ABC123"
    assert vehiculo.get_tarifa_base() == 50.0
    assert vehiculo.get_superficie() == 4.0


def test_crear_auto():
    """Verifica que Factory crea Auto correctamente."""
    vehiculo = VehiculoFactory.crear_vehiculo("Auto", "XYZ789")

    assert isinstance(vehiculo, Auto)
    assert vehiculo.get_patente() == "XYZ789"
    assert vehiculo.get_tarifa_base() == 100.0
    assert vehiculo.get_superficie() == 12.0


def test_crear_camioneta():
    """Verifica que Factory crea Camioneta correctamente."""
    vehiculo = VehiculoFactory.crear_vehiculo("Camioneta", "DEF456")

    assert isinstance(vehiculo, Camioneta)
    assert vehiculo.get_patente() == "DEF456"
    assert vehiculo.get_tarifa_base() == 150.0
    assert vehiculo.get_superficie() == 20.0


def test_tipo_desconocido_lanza_excepcion():
    """Verifica que tipo desconocido lanza ValueError."""
    try:
        VehiculoFactory.crear_vehiculo("Bicicleta", "BIC123")
        assert False, "Deberia haber lanzado ValueError"
    except ValueError as e:
        assert "desconocido" in str(e).lower()


if __name__ == "__main__":
    test_crear_moto()
    test_crear_auto()
    test_crear_camioneta()
    test_tipo_desconocido_lanza_excepcion()
    print("[OK] Todos los tests de Factory pasaron")
