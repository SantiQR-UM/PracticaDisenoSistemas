# IDEA.md — Sistema de Gestión de Estacionamiento (con Patrones de Diseño)

## 1. Contexto del Dominio
Un estacionamiento moderno necesita controlar de manera eficiente:
- El ingreso y egreso de vehículos.
- Disponibilidad de plazas.
- Facturación dinámica.
- Diferentes tipos de vehículos.
- Tarifas variables según condiciones (hora, evento, tamaño, etc.).
- Registro histórico de transacciones.

El sistema puede volverse complejo si se intenta manejar toda la lógica de negocio desde la interfaz. Por eso, se propone una arquitectura basada en patrones de diseño, similar a la usada en el proyecto forestal, pero aplicada al dominio de estacionamientos.

## 2. Objetivo General
Diseñar un sistema de software demostrativo que use patrones de diseño clásicos (Singleton, Factory, Strategy, Observer) y que simule operaciones reales de un estacionamiento.

Este sistema podrá integrarse con una app Android POS para la venta/cobro y con un backend que centralice estado, facturación e inventario de plazas.

---

## 3. Patrones de Diseño Implementados

### 3.1 Singleton — ParkingLotManager / PricingRegistry
Se utiliza para garantizar que:
- Exista una única instancia que mantenga el estado del estacionamiento.
- Se eviten inconsistencias en conteos de plazas.
- Se controlen las reglas de precio desde un único punto.

Casos donde un Singleton aplica aquí:
- Estado de plazas disponibles.
- Registro central de vehículos adentro.
- Motor de reglas de tarifas.
- Logger y auditoría.

Esto evita estados duplicados y colisiones entre subsistemas.

---

### 3.2 Factory — VehiculoFactory
Permite crear vehículos sin acoplar el código cliente a clases concretas.

Ejemplos de tipos:
- Moto
- Auto
- Camioneta

Cada uno tiene:
- Tamaño distinto.
- Tarifa base distinta.
- Tiempo de tolerancia distinto.

La fábrica encapsula toda la lógica de construcción, evitando condicionales y permitiendo agregar nuevos tipos fácilmente.

---

### 3.3 Strategy — PricingStrategy
Permite intercambiar algoritmos de cálculo de precio en tiempo de ejecución.

Ejemplos reales:
- Happy hour (descuento).
- Delivery/valet (recargo).
- Tarifas nocturnas.
- Eventos especiales (recital, partido, feria local).

De esta forma, se puede cambiar la lógica sin romper el resto del código.

---

### 3.4 Observer — Sensores y Eventos Internos
Permite notificar al sistema cuando ocurren cambios:
- Sensores de ocupación.
- Cámaras lectoras de patente.
- Alertas de incendio.
- Cambios de disponibilidad.

Los observadores reaccionan automáticamente a cambios y actualizan el estado general.

En una integración con hardware real, sensores notificarían eventos sin necesidad de que la aplicación pregunte continuamente.

---

## 4. Funcionalidades Principales
- Ingreso de vehículo.
- Cálculo de tarifa según estrategia activa.
- Control de disponibilidad de plazas.
- Registro de salida.
- Facturación.
- Persistencia de registros.
- Alertas de seguridad.

---

## 5. Flujo de Operaciones Típico
```
1. Vehículo ingresa → Se registra en ParkingLotManager.
2. Factory crea el objeto según tipo.
3. Strategy calcula tarifa en base a condiciones actuales.
4. Observer notifica cambios en disponibilidad.
5. Vehículo sale → Se calcula precio final y se persiste.
```

---

## 6. Casos de Uso
- Ver disponibilidad.
- Agregar vehículo.
- Marcar egreso y cobrar.
- Cambiar estrategia de precio en runtime.
- Registrar auditorías.
- Mostrar histórico.

---

## 7. Entidades Principales
- `Vehiculo` (abstracto)
  - `Moto`
  - `Auto`
  - `Camioneta`

- `ParkingLotManager` (Singleton)
- `VehiculoFactory` (Factory)
- `PricingRegistry` (Singleton + Strategy)
- `SensorHub` (Observer)

---

## 8. Ejemplo de Uso de los Patrones
```python
# Singleton de reglas de precio
pricing = PricingRegistry.get_instance()
pricing.strategy = HappyHourStrategy()

# Factory crea vehículos
vehiculo = VehiculoFactory.create("Auto")

# Parking lot manager registra entrada
ParkingLotManager.get_instance().entrar(vehiculo)
```

---

## 9. Persistencia y Trazabilidad
Podría usarse:
- Archivos binarios (demo educativa).
- SQLite local.
- JSON/CSV históricos.
- Backend vía API REST.

Registros necesarios:
- Hora de ingreso.
- Hora de salida.
- Tipo de vehículo.
- Tarifa aplicada.
- Evento o condición especial.

---

## 10. Escalabilidad y Extensión
El diseño está preparado para:
- Nuevos tipos de vehículos.
- Nuevas estrategias de precio.
- Integración con hardware real.
- Integración con app móvil.

Sin romper el código existente.

---

## 11. Beneficios del Uso de Patrones
- Fácil mantenimiento.
- Extensibilidad.
- Menos condicionales.
- Alta cohesión.
- Bajo acoplamiento.

Replicando buenas prácticas del sistema forestal, pero aplicado al tránsito urbano.

---

# Apéndice A — Integración con App Android POS

## Objetivo
Conectar la app con este backend para cobrar estacionamiento y administrar operaciones desde el celular.

### Necesidades del Backend
- Endpoints REST:
  - `POST /ingreso` → registra entrada
  - `POST /egreso` → calcula tarifa y cobra
  - `GET /disponibilidad` → plazas libres
  - `GET /historial` → registros de auditoría
  - `GET /precios` → reglas activas

- Base de datos (preferiblemente SQLite/PostgreSQL):
  - tabla `vehiculos_activos`
  - tabla `historico_transacciones`
  - tabla `estrategias_precio`

- Instancias Singleton:
  - `ParkingLotManager` → controla estado.
  - `PricingRegistry` → regla única de negocio.

---

### Necesidades en la App POS
- Pantalla de ingreso:
  - Selección tipo de vehículo.
  - Lectura opcional de patente.

- Pantalla de egreso:
  - Obtención del precio final.
  - Impresión/recibo.

- Observación en tiempo real:
  - Indicador de plazas libres.
  - Alertas de sensores.

- Sincronización offline-first:
  - Guardar ventas localmente si no hay internet.

- Integración con hardware opcional:
  - Impresoras térmicas.
  - QR.

---

## Flujo de Comunicación App ↔ Backend
```
APP → POST /ingreso → Backend actualiza ParkingLotManager
Backend → responde estado actualizado

APP → POST /egreso → calcula Strategy
Backend → persiste transacción
Backend → responde precio final
```

---

## Componentes Adicionales Recomendados
### En Backend
- Token JWT simple para seguridad.
- Logger central.
- Auditoría.
- Tareas programadas de limpieza.

### En App
- Cache local Room.
- Retrofit para consumir API.
- ViewModel para mantener estado.
- StateFlow/Livedata para observar cambios.

---

## Conclusión
Este proyecto permite:
- Practicar aplicación real de patrones clásicos.
- Aprender integración móvil-backend.
- Simular lógica comercial real.
- Escalar a hardware e IoT.

La arquitectura desacoplada permite que ambos crezcan de manera independiente, manteniendo orden, testabilidad y mantenibilidad.

