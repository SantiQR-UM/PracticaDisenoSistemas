"""Tests para el patron Strategy.

Verifica que las diferentes estrategias de precio calculan
correctamente los montos.
"""

# Standard library
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Agregar el directorio raiz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

# Local application
from python_estacionamiento.patrones.factory.vehiculo_factory import VehiculoFactory
from python_estacionamiento.patrones.strategy.impl.pricing_standard_strategy import PricingStandardStrategy
from python_estacionamiento.patrones.strategy.impl.pricing_happy_hour_strategy import PricingHappyHourStrategy
from python_estacionamiento.patrones.strategy.impl.pricing_valet_strategy import PricingValetStrategy
from python_estacionamiento.patrones.strategy.impl.pricing_evento_strategy import PricingEventoStrategy


def test_pricing_standard():
    """Verifica que estrategia estandar calcula correctamente."""
    auto = VehiculoFactory.crear_vehiculo("Auto", "XYZ789")
    estrategia = PricingStandardStrategy()

    # 2 horas de estadia (120 minutos)
    # Tolerancia de 15 minutos
    # Cobrables: 105 minutos = 1.75 horas
    # Precio: 100 * 1.75 = 175
    hora_ingreso = datetime.now() - timedelta(hours=2)
    hora_egreso = datetime.now()

    precio = estrategia.calcular_precio(auto, hora_ingreso, hora_egreso)

    assert precio == 175.0


def test_pricing_happy_hour():
    """Verifica que estrategia happy hour aplica descuento."""
    auto = VehiculoFactory.crear_vehiculo("Auto", "XYZ789")
    estrategia = PricingHappyHourStrategy()

    hora_ingreso = datetime.now() - timedelta(hours=2)
    hora_egreso = datetime.now()

    precio = estrategia.calcular_precio(auto, hora_ingreso, hora_egreso)

    # Precio estandar es 175.0
    # Descuento 20%: 175 * 0.8 = 140.0
    assert precio == 140.0


def test_pricing_valet():
    """Verifica que estrategia valet aplica recargo."""
    auto = VehiculoFactory.crear_vehiculo("Auto", "XYZ789")
    estrategia = PricingValetStrategy()

    hora_ingreso = datetime.now() - timedelta(hours=2)
    hora_egreso = datetime.now()

    precio = estrategia.calcular_precio(auto, hora_ingreso, hora_egreso)

    # Precio estandar es 175.0
    # Recargo 30%: 175 * 1.3 = 227.5
    assert precio == 227.5


def test_pricing_evento():
    """Verifica que estrategia evento aplica recargo mayor."""
    auto = VehiculoFactory.crear_vehiculo("Auto", "XYZ789")
    estrategia = PricingEventoStrategy()

    hora_ingreso = datetime.now() - timedelta(hours=2)
    hora_egreso = datetime.now()

    precio = estrategia.calcular_precio(auto, hora_ingreso, hora_egreso)

    # Precio estandar es 175.0
    # Recargo 50%: 175 * 1.5 = 262.5
    assert precio == 262.5


def test_tolerancia_aplicada():
    """Verifica que la tolerancia se aplica correctamente."""
    moto = VehiculoFactory.crear_vehiculo("Moto", "ABC123")
    estrategia = PricingStandardStrategy()

    # 5 minutos de estadia (menor que tolerancia de 10 min)
    hora_ingreso = datetime.now() - timedelta(minutes=5)
    hora_egreso = datetime.now()

    precio = estrategia.calcular_precio(moto, hora_ingreso, hora_egreso)

    # Debe ser 0 porque esta dentro de la tolerancia
    assert precio == 0.0


if __name__ == "__main__":
    test_pricing_standard()
    test_pricing_happy_hour()
    test_pricing_valet()
    test_pricing_evento()
    test_tolerancia_aplicada()
    print("[OK] Todos los tests de Strategy pasaron")
