"""Tests para el patron Observer.

Verifica que Observable y Observer funcionan correctamente
con tipo-seguridad.
"""

# Standard library
import sys
from pathlib import Path

# Agregar el directorio raiz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

# Local application
from python_estacionamiento.patrones.observer.observable import Observable
from python_estacionamiento.patrones.observer.observer import Observer


class TestObservable(Observable[int]):
    """Observable de prueba que emite enteros."""

    def emitir_valor(self, valor: int):
        """Emite un valor a los observadores."""
        self.notificar_observadores(valor)


class TestObserver(Observer[int]):
    """Observer de prueba que recibe enteros."""

    def __init__(self):
        self.ultimo_valor = None
        self.cantidad_notificaciones = 0

    def actualizar(self, evento: int) -> None:
        """Recibe notificacion."""
        self.ultimo_valor = evento
        self.cantidad_notificaciones += 1


def test_observador_recibe_notificacion():
    """Verifica que observador recibe notificaciones."""
    observable = TestObservable()
    observador = TestObserver()

    observable.agregar_observador(observador)
    observable.emitir_valor(42)

    assert observador.ultimo_valor == 42
    assert observador.cantidad_notificaciones == 1


def test_multiples_observadores():
    """Verifica que multiples observadores reciben notificaciones."""
    observable = TestObservable()
    observador1 = TestObserver()
    observador2 = TestObserver()

    observable.agregar_observador(observador1)
    observable.agregar_observador(observador2)
    observable.emitir_valor(100)

    assert observador1.ultimo_valor == 100
    assert observador2.ultimo_valor == 100


def test_eliminar_observador():
    """Verifica que se puede eliminar un observador."""
    observable = TestObservable()
    observador = TestObserver()

    observable.agregar_observador(observador)
    observable.emitir_valor(1)
    assert observador.cantidad_notificaciones == 1

    observable.eliminar_observador(observador)
    observable.emitir_valor(2)
    assert observador.cantidad_notificaciones == 1  # No se incrementa


def test_mismo_observador_no_se_agrega_dos_veces():
    """Verifica que el mismo observador no se agrega duplicado."""
    observable = TestObservable()
    observador = TestObserver()

    observable.agregar_observador(observador)
    observable.agregar_observador(observador)  # Segundo intento
    observable.emitir_valor(50)

    # Solo debe recibir una notificacion
    assert observador.cantidad_notificaciones == 1


if __name__ == "__main__":
    test_observador_recibe_notificacion()
    test_multiples_observadores()
    test_eliminar_observador()
    test_mismo_observador_no_se_agrega_dos_veces()
    print("[OK] Todos los tests de Observer pasaron")
