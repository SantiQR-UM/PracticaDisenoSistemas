"""Tests para el patron Singleton.

Verifica que ParkingLotManager y PricingRegistry implementan
correctamente el patron Singleton.
"""

# Standard library
import sys
from pathlib import Path

# Agregar el directorio raiz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

# Local application
from python_estacionamiento.servicios.parking_lot_manager import ParkingLotManager
from python_estacionamiento.servicios.pricing_registry import PricingRegistry


def test_parking_lot_manager_singleton():
    """Verifica que ParkingLotManager es Singleton."""
    # Obtener dos referencias
    manager1 = ParkingLotManager.get_instance()
    manager2 = ParkingLotManager.get_instance()

    # Deben ser la misma instancia
    assert manager1 is manager2
    assert id(manager1) == id(manager2)


def test_pricing_registry_singleton():
    """Verifica que PricingRegistry es Singleton."""
    # Obtener dos referencias
    registry1 = PricingRegistry.get_instance()
    registry2 = PricingRegistry.get_instance()

    # Deben ser la misma instancia
    assert registry1 is registry2
    assert id(registry1) == id(registry2)


def test_singleton_new_constructor():
    """Verifica que usar constructor tambien retorna misma instancia."""
    # Usando get_instance()
    manager1 = ParkingLotManager.get_instance()

    # Usando constructor
    manager2 = ParkingLotManager()

    # Deben ser la misma instancia
    assert manager1 is manager2


if __name__ == "__main__":
    test_parking_lot_manager_singleton()
    test_pricing_registry_singleton()
    test_singleton_new_constructor()
    print("[OK] Todos los tests de Singleton pasaron")
