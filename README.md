# Sistema de Gestion de Estacionamiento

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema integral de gestion de estacionamiento que demuestra la implementacion de multiples patrones de diseno de software con enfoque educativo y profesional.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Patrones de Diseno Implementados](#patrones-de-diseno-implementados)
- [Instalacion y Ejecucion](#instalacion-y-ejecucion)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Funcionalidades Principales](#funcionalidades-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)

---

## Contexto del Dominio

El sistema **PythonEstacionamiento** aborda los desafios de la gestion moderna de estacionamientos, un dominio que requiere:

1. **Gestion de Multiples Tipos de Vehiculos**
   - Motos con caracteristicas especificas (cilindrada)
   - Autos con diferentes marcas
   - Camionetas con capacidad de carga
   - Cada tipo con tarifas y tolerancias particulares

2. **Control de Disponibilidad**
   - Registro de plazas disponibles y ocupadas
   - Control de capacidad maxima
   - Manejo de excepciones cuando no hay espacios

3. **Facturacion Dinamica**
   - Estrategias de precio intercambiables
   - Descuentos y recargos segun condiciones
   - Calculo automatico basado en tiempo de estadia

4. **Sistema Extensible**
   - Preparado para sensores de ocupacion
   - Arquitectura lista para camaras de patentes
   - Patron Observer implementado para eventos

---

## Patrones de Diseno Implementados

### 1. SINGLETON Pattern

**Ubicacion**:
- `python_estacionamiento/servicios/parking_lot_manager.py`
- `python_estacionamiento/servicios/pricing_registry.py`

**Problema que resuelve**:
- Garantizar una unica instancia del gestor de estacionamiento
- Compartir estado entre todos los componentes del sistema
- Evitar multiples instancias inconsistentes

**Implementacion**:
```python
class ParkingLotManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe double-checked locking
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

**Uso en el sistema**:
```python
parking_manager = ParkingLotManager.get_instance()
```

**Ventajas**:
- Thread-safe mediante Lock
- Inicializacion perezosa (lazy initialization)
- Punto unico de control del estado

---

### 2. FACTORY METHOD Pattern

**Ubicacion**: `python_estacionamiento/patrones/factory/vehiculo_factory.py`

**Problema que resuelve**:
- Creacion de vehiculos sin conocer clases concretas
- Encapsulacion de logica de construccion
- Extensibilidad para nuevos tipos de vehiculos

**Implementacion**:
```python
class VehiculoFactory:
    @staticmethod
    def crear_vehiculo(tipo: str, patente: str) -> Vehiculo:
        factories = {
            "Moto": VehiculoFactory._crear_moto,
            "Auto": VehiculoFactory._crear_auto,
            "Camioneta": VehiculoFactory._crear_camioneta
        }

        if tipo not in factories:
            raise ValueError(f"Tipo de vehiculo desconocido: {tipo}")

        return factories[tipo](patente)
```

**Uso en el sistema**:
```python
vehiculo = VehiculoFactory.crear_vehiculo("Auto", "ABC123")
```

**Ventajas**:
- Codigo cliente independiente de clases concretas
- Facil agregar nuevos tipos de vehiculos
- Validacion centralizada de tipos

---

### 3. OBSERVER Pattern

**Ubicacion**: `python_estacionamiento/patrones/observer/`

**Problema que resuelve**:
- Notificacion automatica a multiples observadores
- Desacoplamiento entre sensores y consumidores
- Sistema de eventos tipo-seguro

**Implementacion**:
```python
class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Ventajas**:
- Tipo-seguro con Generics
- Desacoplamiento total
- Multiples observadores permitidos
- Preparado para expansion con sensores reales

---

### 4. STRATEGY Pattern

**Ubicacion**: `python_estacionamiento/patrones/strategy/`

**Problema que resuelve**:
- Algoritmos de calculo de precio intercambiables
- Eliminar condicionales tipo if/else
- Permitir cambios en tiempo de ejecucion

**Implementacion**:
```python
class PricingStrategy(ABC):
    @abstractmethod
    def calcular_precio(
        self,
        vehiculo: Vehiculo,
        hora_ingreso: datetime,
        hora_egreso: datetime
    ) -> float:
        pass

# Estrategia 1: Estandar
class PricingStandardStrategy(PricingStrategy):
    def calcular_precio(self, vehiculo, hora_ingreso, hora_egreso):
        # Calculo basado en tarifa base y tiempo

# Estrategia 2: Happy Hour (descuento 20%)
class PricingHappyHourStrategy(PricingStandardStrategy):
    def calcular_precio(self, vehiculo, hora_ingreso, hora_egreso):
        precio_base = super().calcular_precio(vehiculo, hora_ingreso, hora_egreso)
        return precio_base * (1 - DESCUENTO_HAPPY_HOUR)
```

**Uso en el sistema**:
```python
# Cambiar estrategia en runtime
pricing_registry = PricingRegistry.get_instance()
pricing_registry.set_estrategia(PricingHappyHourStrategy())
precio = pricing_registry.calcular_precio(vehiculo, hora_ingreso, hora_egreso)
```

**Estrategias implementadas**:
- **PricingStandardStrategy**: Calculo estandar por hora
- **PricingHappyHourStrategy**: Descuento del 20%
- **PricingValetStrategy**: Recargo del 30% por servicio premium
- **PricingEventoStrategy**: Recargo del 50% durante eventos especiales

---

## Instalacion y Ejecucion

### Requisitos

- **Python 3.13** o superior
- Solo biblioteca estandar de Python (sin dependencias externas)

### Pasos para ejecutar

1. **Clonar o descargar el proyecto**

2. **Navegar al directorio del proyecto**
```bash
cd PythonEstacionamiento
```

3. **Ejecutar el sistema**
```bash
python main.py
```

**Salida esperada**:
```
=============== SISTEMA DE GESTION DE ESTACIONAMIENTO ===============

-------------- PATRON SINGLETON: Inicializando gestores --------------
[OK] SINGLETON verificado: ParkingLotManager tiene instancia unica
[OK] SINGLETON verificado: PricingRegistry tiene instancia unica

----------------- PATRON FACTORY: Creando vehiculos -----------------
[OK] FACTORY verificado: Creados 3 vehiculos

--------------- PATRON STRATEGY: Estrategias de precio ---------------
[OK] STRATEGY verificado: 4 estrategias implementadas y funcionando

================== EJEMPLO COMPLETADO EXITOSAMENTE ==================
```

---

## Estructura del Proyecto

```
PythonEstacionamiento/
|
+-- main.py                          # Punto de entrada del sistema
+-- README.md                        # Este archivo
+-- idea.md                          # Documento de diseno original
|
+-- data/                            # Datos persistidos (para expansion futura)
|
+-- python_estacionamiento/          # Paquete principal
    |
    +-- __init__.py
    +-- constantes.py                # Constantes centralizadas del sistema
    |
    +-- entidades/                   # Objetos de dominio (DTOs)
    |   +-- __init__.py
    |   |
    |   +-- vehiculos/               # Vehiculos del sistema
    |       +-- __init__.py
    |       +-- vehiculo.py          # Clase base abstracta
    |       +-- moto.py              # Vehiculo tipo Moto
    |       +-- auto.py              # Vehiculo tipo Auto
    |       +-- camioneta.py         # Vehiculo tipo Camioneta
    |
    +-- patrones/                    # Implementaciones de patrones
    |   +-- __init__.py
    |   |
    |   +-- singleton/               # Patron Singleton (usado en servicios)
    |   |   +-- __init__.py
    |   |
    |   +-- factory/                 # Patron Factory Method
    |   |   +-- __init__.py
    |   |   +-- vehiculo_factory.py # Factory de vehiculos
    |   |
    |   +-- observer/                # Patron Observer
    |   |   +-- __init__.py
    |   |   +-- observable.py       # Clase Observable[T]
    |   |   +-- observer.py         # Interfaz Observer[T]
    |   |
    |   +-- strategy/                # Patron Strategy
    |       +-- __init__.py
    |       +-- pricing_strategy.py # Interfaz Strategy
    |       +-- impl/
    |           +-- __init__.py
    |           +-- pricing_standard_strategy.py
    |           +-- pricing_happy_hour_strategy.py
    |           +-- pricing_valet_strategy.py
    |           +-- pricing_evento_strategy.py
    |
    +-- servicios/                   # Logica de negocio
    |   +-- __init__.py
    |   +-- parking_lot_manager.py  # Gestor Singleton del estacionamiento
    |   +-- pricing_registry.py     # Registro Singleton de estrategias
    |
    +-- sensores/                    # Sistema de sensores (preparado)
    |   +-- __init__.py
    |
    +-- excepciones/                 # Excepciones personalizadas
        +-- __init__.py
        +-- estacionamiento_exception.py
```

---

## Funcionalidades Principales

### 1. Gestion de Vehiculos

- **Creacion dinamica** de 3 tipos de vehiculos mediante Factory Pattern
  - **Moto**: Con cilindrada configurable
  - **Auto**: Con marca configurable
  - **Camioneta**: Con capacidad de carga configurable

- **Tarifas diferenciadas** por tipo:
  - Moto: $50/hora
  - Auto: $100/hora
  - Camioneta: $150/hora

### 2. Control del Estacionamiento

- **Ingreso y egreso de vehiculos**
  - Registro de hora de ingreso/egreso
  - Control de capacidad maxima (100 plazas por defecto)
  - Excepciones cuando no hay espacio

- **Consulta de disponibilidad**
  - Plazas disponibles
  - Plazas ocupadas
  - Busqueda de vehiculos por patente

### 3. Sistema de Facturacion

- **Calculo de precios** con tolerancia
  - Moto: 10 minutos sin cargo
  - Auto: 15 minutos sin cargo
  - Camioneta: 15 minutos sin cargo

- **Estrategias de precio**:
  - Estandar: Precio base x horas
  - Happy Hour: 20% descuento
  - Valet: 30% recargo
  - Evento: 50% recargo

### 4. Persistencia (Preparado)

- Arquitectura lista para:
  - Guardado de historico de transacciones
  - Recuperacion de datos persistidos
  - Integracion con base de datos

---

## Arquitectura del Sistema

### Principios Arquitectonicos

El sistema esta disenado siguiendo principios SOLID:

- **Single Responsibility**: Cada clase tiene una unica razon para cambiar
  - Entidades: Solo contienen datos (DTOs)
  - Servicios: Solo contienen logica de negocio
  - Patrones: Implementaciones aisladas y reutilizables

- **Open/Closed**: Abierto a extension, cerrado a modificacion
  - Nuevos vehiculos: Agregar sin modificar factory existente
  - Nuevas estrategias: Implementar interfaz sin cambiar servicios

- **Liskov Substitution**: Subtipos intercambiables
  - Todos los vehiculos son Vehiculo
  - Todas las estrategias implementan PricingStrategy

- **Interface Segregation**: Interfaces especificas
  - Observer[T]: Generico para cualquier tipo de evento
  - PricingStrategy: Especifico para calculo de precios

- **Dependency Inversion**: Dependencias de abstracciones
  - Servicios dependen de Strategy (abstraccion), no implementaciones
  - Factory retorna Vehiculo (interfaz), no tipos concretos

### Separacion de Capas

```
+----------------------------------+
|        PRESENTACION              |
|  (main.py - Demostracion CLI)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE NEGOCIO        |
|  (ParkingLotManager, etc.)       |
+----------------------------------+
                |
                v
+----------------------------------+
|          ENTIDADES               |
|  (Vehiculo, Moto, Auto, etc.)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      PATRONES / UTILIDADES       |
|  (Factory, Strategy, Observer)   |
+----------------------------------+
```

---

## Convenciones de Codigo

### Nomenclatura

- **Variables/funciones**: `snake_case`
- **Clases**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE` (definidas en `constantes.py`)
- **Privados**: Prefijo `_nombre`

### Type Hints

- Todas las funciones tienen type hints para parametros y return values
- Uso de `TYPE_CHECKING` para evitar imports circulares

### Docstrings

- Estilo Google para todas las clases y metodos publicos
- Incluye Args, Returns, y Raises cuando corresponde

---

## Diferencias con PythonForestal

Este proyecto replica la estructura de PythonForestal pero aplicado al dominio de estacionamiento:

| PythonForestal | PythonEstacionamiento |
|----------------|----------------------|
| Cultivos (Pino, Olivo, Lechuga, Zanahoria) | Vehiculos (Moto, Auto, Camioneta) |
| Plantacion | Estacionamiento |
| Absorcion de agua | Calculo de precio |
| Sensores de temperatura/humedad | Sensores de ocupacion/camaras (preparado) |
| Riego automatizado | Facturacion automatizada |
| Registro Forestal | Registro de Transacciones (preparado) |

---

## Proximos Pasos

El sistema esta preparado para:
- Integracion con sensores de ocupacion
- Camaras de lectura de patentes
- Persistencia de transacciones historicas
- Integracion con app Android POS
- Sistema de reservas online
- Integracion con hardware de barreras

---

## Licencia

Este proyecto es de codigo abierto con fines educativos.

---

**Ultima actualizacion**: Octubre 2025
**Version del sistema**: 1.0.0
**Python requerido**: 3.13+
