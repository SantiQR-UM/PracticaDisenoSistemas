"""Tests para el sistema de sensores.

Verifica que los sensores funcionan correctamente con el patron Observer.
"""

# Standard library
import sys
from pathlib import Path
from datetime import datetime

# Agregar el directorio raiz al path para imports
root_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_dir))

# Local application
from python_estacionamiento.sensores.sensor_ocupacion import SensorOcupacion
from python_estacionamiento.sensores.sensor_camara import SensorCamara
from python_estacionamiento.sensores.sensor_seguridad import SensorSeguridad
from python_estacionamiento.sensores.eventos import (
    VehiculoIngresoEvento,
    VehiculoEgresoEvento,
    PlazasAgotadasEvento,
    CapacidadCriticaEvento
)
from python_estacionamiento.entidades.vehiculos.moto import Moto


def test_sensor_ocupacion_recibe_ingreso():
    """Verifica que sensor de ocupacion recibe eventos de ingreso."""
    sensor = SensorOcupacion(umbral_critico=10)
    vehiculo = Moto(patente="TEST123", cilindrada=150)

    evento = VehiculoIngresoEvento(
        timestamp=datetime.now(),
        mensaje="Test ingreso",
        vehiculo=vehiculo,
        plazas_ocupadas=1,
        plazas_disponibles=99
    )

    # Verificar que no lanza excepcion
    sensor.actualizar(evento)
    print("[OK] Sensor de ocupacion procesa ingreso correctamente")


def test_sensor_ocupacion_recibe_egreso():
    """Verifica que sensor de ocupacion recibe eventos de egreso."""
    sensor = SensorOcupacion(umbral_critico=10)
    vehiculo = Moto(patente="TEST123", cilindrada=150)
    vehiculo.set_hora_ingreso(datetime.now())
    vehiculo.set_hora_egreso(datetime.now())

    evento = VehiculoEgresoEvento(
        timestamp=datetime.now(),
        mensaje="Test egreso",
        vehiculo=vehiculo,
        plazas_ocupadas=0,
        plazas_disponibles=100,
        tiempo_estadia="0:00:00"
    )

    # Verificar que no lanza excepcion
    sensor.actualizar(evento)
    print("[OK] Sensor de ocupacion procesa egreso correctamente")


def test_sensor_ocupacion_detecta_capacidad_critica():
    """Verifica que sensor detecta capacidad critica."""
    sensor = SensorOcupacion(umbral_critico=10)

    evento = CapacidadCriticaEvento(
        timestamp=datetime.now(),
        mensaje="Capacidad critica",
        plazas_disponibles=5,
        porcentaje_ocupacion=95.0
    )

    # Verificar que no lanza excepcion
    sensor.actualizar(evento)
    print("[OK] Sensor de ocupacion detecta capacidad critica")


def test_sensor_camara_registra_patentes():
    """Verifica que sensor de camara registra patentes."""
    sensor = SensorCamara(ubicacion="Test")
    vehiculo = Moto(patente="CAM999", cilindrada=150)

    evento_ingreso = VehiculoIngresoEvento(
        timestamp=datetime.now(),
        mensaje="Test ingreso camara",
        vehiculo=vehiculo,
        plazas_ocupadas=1,
        plazas_disponibles=99
    )

    sensor.actualizar(evento_ingreso)

    # Verificar que registro el ingreso
    registros = sensor.get_registros()
    assert len(registros) == 1
    assert registros[0]['tipo'] == 'INGRESO'
    assert registros[0]['patente'] == 'CAM999'

    print("[OK] Sensor de camara registra patentes correctamente")


def test_sensor_camara_registra_entrada_y_salida():
    """Verifica que sensor de camara registra entrada y salida."""
    sensor = SensorCamara(ubicacion="Test")
    vehiculo = Moto(patente="CAM888", cilindrada=150)
    vehiculo.set_hora_ingreso(datetime.now())
    vehiculo.set_hora_egreso(datetime.now())

    # Ingreso
    evento_ingreso = VehiculoIngresoEvento(
        timestamp=datetime.now(),
        mensaje="Test ingreso",
        vehiculo=vehiculo,
        plazas_ocupadas=1,
        plazas_disponibles=99
    )
    sensor.actualizar(evento_ingreso)

    # Egreso
    evento_egreso = VehiculoEgresoEvento(
        timestamp=datetime.now(),
        mensaje="Test egreso",
        vehiculo=vehiculo,
        plazas_ocupadas=0,
        plazas_disponibles=100,
        tiempo_estadia="0:00:00"
    )
    sensor.actualizar(evento_egreso)

    # Verificar registros
    registros = sensor.get_registros()
    assert len(registros) == 2
    assert registros[0]['tipo'] == 'INGRESO'
    assert registros[1]['tipo'] == 'EGRESO'

    print("[OK] Sensor de camara registra entrada y salida")


def test_sensor_seguridad_monitorea_vehiculos():
    """Verifica que sensor de seguridad monitorea vehiculos."""
    sensor = SensorSeguridad()
    vehiculo = Moto(patente="SEC777", cilindrada=150)

    evento_ingreso = VehiculoIngresoEvento(
        timestamp=datetime.now(),
        mensaje="Test ingreso seguridad",
        vehiculo=vehiculo,
        plazas_ocupadas=1,
        plazas_disponibles=99
    )

    sensor.actualizar(evento_ingreso)

    # Verificar que monitorea el vehiculo
    monitoreados = sensor.get_vehiculos_monitoreados()
    assert 'SEC777' in monitoreados
    assert len(monitoreados) == 1

    print("[OK] Sensor de seguridad monitorea vehiculos")


def test_sensor_seguridad_libera_vehiculos():
    """Verifica que sensor de seguridad libera vehiculos al salir."""
    sensor = SensorSeguridad()
    vehiculo = Moto(patente="SEC666", cilindrada=150)
    vehiculo.set_hora_ingreso(datetime.now())
    vehiculo.set_hora_egreso(datetime.now())

    # Ingreso
    evento_ingreso = VehiculoIngresoEvento(
        timestamp=datetime.now(),
        mensaje="Test ingreso",
        vehiculo=vehiculo,
        plazas_ocupadas=1,
        plazas_disponibles=99
    )
    sensor.actualizar(evento_ingreso)

    assert 'SEC666' in sensor.get_vehiculos_monitoreados()

    # Egreso
    evento_egreso = VehiculoEgresoEvento(
        timestamp=datetime.now(),
        mensaje="Test egreso",
        vehiculo=vehiculo,
        plazas_ocupadas=0,
        plazas_disponibles=100,
        tiempo_estadia="0:00:00"
    )
    sensor.actualizar(evento_egreso)

    # Verificar que libero el vehiculo
    monitoreados = sensor.get_vehiculos_monitoreados()
    assert 'SEC666' not in monitoreados
    assert len(monitoreados) == 0

    print("[OK] Sensor de seguridad libera vehiculos")


def test_sensor_seguridad_alerta_plazas_agotadas():
    """Verifica que sensor de seguridad alerta cuando plazas agotadas."""
    sensor = SensorSeguridad()

    evento = PlazasAgotadasEvento(
        timestamp=datetime.now(),
        mensaje="Plazas agotadas",
        patente_rechazada="DENY123"
    )

    sensor.actualizar(evento)
    # Verificar que no lanza excepcion
    print("[OK] Sensor de seguridad procesa alerta de plazas agotadas")


def test_multiples_sensores_reciben_mismo_evento():
    """Verifica que multiples sensores pueden recibir el mismo evento."""
    sensor_ocupacion = SensorOcupacion(umbral_critico=10)
    sensor_camara = SensorCamara(ubicacion="Test")
    sensor_seguridad = SensorSeguridad()

    vehiculo = Moto(patente="MULTI123", cilindrada=150)
    evento = VehiculoIngresoEvento(
        timestamp=datetime.now(),
        mensaje="Test multi",
        vehiculo=vehiculo,
        plazas_ocupadas=1,
        plazas_disponibles=99
    )

    # Todos los sensores procesan el evento
    sensor_ocupacion.actualizar(evento)
    sensor_camara.actualizar(evento)
    sensor_seguridad.actualizar(evento)

    # Verificar cada sensor
    assert len(sensor_camara.get_registros()) == 1
    assert 'MULTI123' in sensor_seguridad.get_vehiculos_monitoreados()

    print("[OK] Multiples sensores procesan el mismo evento")


if __name__ == "__main__":
    print("\n=== Ejecutando Tests de Sensores ===\n")

    test_sensor_ocupacion_recibe_ingreso()
    test_sensor_ocupacion_recibe_egreso()
    test_sensor_ocupacion_detecta_capacidad_critica()
    test_sensor_camara_registra_patentes()
    test_sensor_camara_registra_entrada_y_salida()
    test_sensor_seguridad_monitorea_vehiculos()
    test_sensor_seguridad_libera_vehiculos()
    test_sensor_seguridad_alerta_plazas_agotadas()
    test_multiples_sensores_reciben_mismo_evento()

    print("\n[OK] Todos los tests de Sensores pasaron\n")
