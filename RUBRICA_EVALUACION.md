# Rubrica de Evaluacion Tecnica - Sistema de Gestion de Estacionamiento

**Proyecto**: PythonEstacionamiento
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Tipo de Evaluacion**: Tecnica Academica / Profesional

---

## Instrucciones de Uso

Esta rubrica esta disenada para evaluar proyectos de software que implementen patrones de diseno en Python. Se utiliza para:

1. **Evaluacion academica**: Proyectos de estudiantes en cursos de Ingenieria de Software
2. **Evaluacion tecnica**: Entrevistas tecnicas para desarrolladores
3. **Code review**: Revision de calidad de codigo en proyectos profesionales
4. **Autoevaluacion**: Chequeo de cumplimiento de buenas practicas

### Escala de Puntuacion

- **Excelente (4 puntos)**: Cumple completamente con criterio, implementacion superior
- **Bueno (3 puntos)**: Cumple con criterio, implementacion correcta con minimos detalles
- **Suficiente (2 puntos)**: Cumple parcialmente, implementacion funcional con deficiencias
- **Insuficiente (1 punto)**: No cumple o cumplimiento minimo, implementacion deficiente
- **No Implementado (0 puntos)**: Criterio no implementado

### Puntaje Total

- **Puntaje Maximo**: 260 puntos
- **Puntaje de Aprobacion**: 182 puntos (70%)
- **Puntaje de Excelencia**: 234 puntos (90%)

---

## Seccion 1: Patrones de Diseno (80 puntos)

### 1.1 Patron SINGLETON (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Clase implementa Singleton con instancia unica | `__new__` con control de instancia unica |
| **Thread-safety** | 5 | Implementacion thread-safe con Lock | Uso de `threading.Lock` con double-checked locking |
| **Acceso consistente** | 3 | Metodo `get_instance()` disponible | Metodo de clase que retorna instancia |
| **Inicializacion perezosa** | 3 | Lazy initialization correcta | Instancia se crea solo cuando se solicita |
| **Uso apropiado en el sistema** | 4 | Singleton usado donde corresponde (Managers) | ParkingLotManager y PricingRegistry son Singleton |

**Puntaje Seccion 1.1**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Singleton]
```

---

### 1.2 Patron FACTORY METHOD (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Factory encapsula creacion de objetos | Metodo estatico `crear_vehiculo(tipo, patente)` |
| **Desacoplamiento** | 5 | Cliente no conoce clases concretas | Retorna tipo base `Vehiculo`, no tipos concretos |
| **Extensibilidad** | 4 | Facil agregar nuevos tipos | Diccionario de factories, no if/elif cascades |
| **Validacion de entrada** | 3 | Valida parametros y lanza excepciones | Lanza `ValueError` si tipo desconocido |
| **Uso apropiado en el sistema** | 3 | Factory usado en main.py | `crear_vehiculo()` usado para crear instancias |

**Puntaje Seccion 1.2**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Factory]
```

---

### 1.3 Patron OBSERVER (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Observable y Observer implementados | Clases `Observable[T]` y `Observer[T]` |
| **Generics para tipo-seguridad** | 5 | Uso de TypeVar y Generic[T] | `Observable[T]`, `Observer[T]` |
| **Notificaciones automaticas** | 4 | Observadores notificados al cambiar estado | `notificar_observadores()` implementado |
| **Desacoplamiento** | 3 | Observable no conoce detalles de Observer | Lista generica de observadores |
| **Uso apropiado en el sistema** | 3 | Preparado para sensores y eventos | Observable y Observer listos para expansion |

**Puntaje Seccion 1.3**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Observer]
```

---

### 1.4 Patron STRATEGY (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Interfaz Strategy con implementaciones | `PricingStrategy` (abstracta) |
| **Algoritmos intercambiables** | 5 | Multiples estrategias implementadas | 4 estrategias (Standard, HappyHour, Valet, Evento) |
| **Inyeccion de dependencias** | 4 | Estrategia inyectada via set_estrategia() | PricingRegistry gestiona estrategia activa |
| **Delegacion correcta** | 3 | Servicios delegan calculo a estrategia | `calcular_precio()` llamado desde registry |
| **Uso apropiado en el sistema** | 3 | Estrategias usadas segun contexto | Diferentes precios segun estrategia |

**Puntaje Seccion 1.4**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Strategy]
```

---

**PUNTAJE TOTAL SECCION 1**: _____ / 80

---

## Seccion 2: Arquitectura y Diseno (60 puntos)

### 2.1 Separacion de Responsabilidades (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Entidades vs Servicios** | 5 | Entidades solo datos, servicios solo logica | Clases en `entidades/` vs `servicios/` |
| **Service Layer Pattern** | 5 | Capa de servicios bien definida | Servicios contienen toda la logica de negocio |
| **Principio SRP** | 4 | Cada clase una unica responsabilidad | Una clase = un concepto de dominio |
| **Cohesion alta** | 3 | Elementos relacionados agrupados | Modulos tematicos (vehiculos, patrones, servicios) |
| **Acoplamiento bajo** | 3 | Dependencias minimizadas | Uso de interfaces, inyeccion de dependencias |

**Puntaje Seccion 2.1**: _____ / 20

---

### 2.2 Jerarquia de Clases (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Herencia apropiada** | 5 | Jerarquia logica de clases | `Vehiculo` → `Moto`, `Auto`, `Camioneta` |
| **Eliminacion de duplicacion** | 4 | Codigo compartido en clases base | Atributos comunes en `Vehiculo` base |
| **Polimorfismo** | 3 | Subtipos intercambiables | Todos los vehiculos son `Vehiculo` |
| **Interfaces bien definidas** | 3 | Contratos claros entre clases | Metodos abstractos en clases base |

**Puntaje Seccion 2.2**: _____ / 15

---

### 2.3 Manejo de Excepciones (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Jerarquia de excepciones** | 5 | Excepciones personalizadas heredan de base | `EstacionamientoException` base |
| **Excepciones especificas** | 4 | Excepciones de dominio implementadas | `PlazasAgotadasException`, `VehiculoNoEncontradoException` |
| **Mensajes descriptivos** | 3 | Mensajes claros para usuario | Separacion mensaje usuario/tecnico |
| **Uso apropiado** | 3 | Excepciones usadas en puntos correctos | Validaciones lanzan excepciones apropiadas |

**Puntaje Seccion 2.3**: _____ / 15

---

### 2.4 Organizacion del Codigo (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Estructura de paquetes** | 3 | Organizacion logica de modulos | Paquetes: entidades, servicios, patrones, sensores, excepciones |
| **Modulos tematicos** | 3 | Agrupacion por dominio | vehiculos/, factory/, strategy/, observer/, singleton/ |
| **Archivos `__init__.py`** | 2 | Inicializacion de paquetes | Todos los paquetes con `__init__.py` |
| **Importaciones limpias** | 2 | Sin imports circulares | Uso de TYPE_CHECKING para forward references |

**Puntaje Seccion 2.4**: _____ / 10

---

**PUNTAJE TOTAL SECCION 2**: _____ / 60

---

## Seccion 3: Calidad de Codigo (60 puntos)

### 3.1 PEP 8 Compliance (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Nombres de variables** | 4 | snake_case, descriptivos, sin abreviaciones | `superficie` no `sup`, `tarifa_base` no `tar` |
| **Nombres de clases** | 3 | PascalCase consistente | `VehiculoFactory`, `ParkingLotManager` |
| **Nombres de constantes** | 3 | UPPER_SNAKE_CASE en modulo centralizado | Todas en `constantes.py` |
| **Organizacion de imports** | 4 | PEP 8: Standard → Third-party → Local | Secciones comentadas |
| **Longitud de linea** | 2 | Maximo 100-120 caracteres | No lineas excesivamente largas |
| **Espaciado y formato** | 4 | Espaciado consistente segun PEP 8 | 2 lineas entre clases, 1 entre metodos |

**Puntaje Seccion 3.1**: _____ / 20

---

### 3.2 Documentacion (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Docstrings en clases** | 4 | Todas las clases documentadas | Docstring en cada clase publica |
| **Docstrings en metodos** | 4 | Metodos publicos documentados | Google Style: Args, Returns, Raises |
| **Formato Google Style** | 3 | Estilo consistente (NO JavaDoc) | Args: / Returns: / Raises: |
| **Comentarios en codigo complejo** | 2 | Explicacion de logica no obvia | Comentarios donde necesario |
| **README y documentacion externa** | 2 | Documentacion de proyecto completa | README.md detallado |

**Puntaje Seccion 3.2**: _____ / 15

---

### 3.3 Type Hints (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Type hints en firmas** | 4 | Parametros y retornos tipados | `def metodo(param: str) -> int:` |
| **Uso de TYPE_CHECKING** | 3 | Evita imports circulares | `if TYPE_CHECKING: from ...` |
| **Generics donde apropiado** | 3 | TypeVar y Generic[T] usados | `Observable[T]`, `Observer[T]` |

**Puntaje Seccion 3.3**: _____ / 10

---

### 3.4 Principios de Codigo Limpio (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **NO magic numbers** | 5 | Constantes centralizadas | CERO valores hardcodeados |
| **NO lambdas** | 4 | Funciones/metodos nombrados | Metodos estaticos en lugar de lambdas |
| **Funciones pequenas** | 3 | Metodos con responsabilidad unica | Funciones < 30 lineas idealmente |
| **Nombres descriptivos** | 3 | Variables y metodos autoexplicativos | `calcular_precio()` no `calc()` |

**Puntaje Seccion 3.4**: _____ / 15

---

**PUNTAJE TOTAL SECCION 3**: _____ / 60

---

## Seccion 4: Funcionalidad del Sistema (40 puntos)

### 4.1 Gestion de Vehiculos (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Multiples tipos de vehiculos** | 4 | Al menos 3 tipos implementados | Moto, Auto, Camioneta |
| **Ingreso funcional** | 4 | Sistema ingresa y valida plazas | `ingresar_vehiculo()` con validacion |
| **Egreso funcional** | 4 | Sistema egresa y calcula tiempo | `egresar_vehiculo()` con calculo de estadia |

**Puntaje Seccion 4.1**: _____ / 12

---

### 4.2 Sistema de Facturacion (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Calculo de precios** | 4 | Precio basado en tiempo de estadia | Calculo con tolerancia |
| **Estrategias intercambiables** | 4 | Multiple estrategias funcionando | 4 estrategias implementadas |
| **Precios correctos** | 4 | Calculos matematicos correctos | Precios coherentes con tarifas |

**Puntaje Seccion 4.2**: _____ / 12

---

### 4.3 Control de Plazas (8 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Disponibilidad de plazas** | 4 | Sistema controla plazas libres/ocupadas | Contador funcional |
| **Excepciones de capacidad** | 4 | Lanza excepcion cuando esta lleno | `PlazasAgotadasException` |

**Puntaje Seccion 4.3**: _____ / 8

---

### 4.4 Sistema Extensible (8 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Patron Observer implementado** | 4 | Observable y Observer listos | Clases genericas implementadas |
| **Preparado para sensores** | 4 | Arquitectura permite expansion | Paquete sensores/ creado |

**Puntaje Seccion 4.4**: _____ / 8

---

**PUNTAJE TOTAL SECCION 4**: _____ / 40

---

## Seccion 5: Buenas Practicas Avanzadas (20 puntos)

### 5.1 Threading y Concurrencia (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Thread-safety en Singleton** | 4 | Operaciones thread-safe donde necesario | Lock en Singleton |
| **Preparado para threading** | 3 | Arquitectura soporta concurrencia | Observer listo para threads |
| **Manejo de recursos** | 3 | Diseno permite gestion correcta | Patron Observer con notificaciones |

**Puntaje Seccion 5.1**: _____ / 10

---

### 5.2 Validacion y Robustez (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Validacion de entrada** | 4 | Parametros validados en setters | Superficie > 0, tarifa >= 0 |
| **Defensive copying** | 3 | Diccionarios con copy() donde apropiado | `get_todos_vehiculos()` retorna copia |
| **Manejo de errores** | 3 | Try/except apropiados | Excepciones personalizadas usadas |

**Puntaje Seccion 5.2**: _____ / 10

---

**PUNTAJE TOTAL SECCION 5**: _____ / 20

---

## Resumen de Evaluacion

### Desglose por Seccion

| Seccion | Puntaje Obtenido | Puntaje Maximo | Porcentaje |
|---------|------------------|----------------|------------|
| 1. Patrones de Diseno | _____ | 80 | _____% |
| 2. Arquitectura y Diseno | _____ | 60 | _____% |
| 3. Calidad de Codigo | _____ | 60 | _____% |
| 4. Funcionalidad del Sistema | _____ | 40 | _____% |
| 5. Buenas Practicas Avanzadas | _____ | 20 | _____% |
| **TOTAL** | **_____** | **260** | **_____%** |

### Calificacion Final

| Rango de Puntaje | Calificacion | Descripcion |
|------------------|--------------|-------------|
| 234 - 260 (90%+) | **Excelente** | Implementacion profesional de alta calidad |
| 208 - 233 (80-89%) | **Muy Bueno** | Implementacion solida con practicas avanzadas |
| 182 - 207 (70-79%) | **Bueno** | Implementacion correcta que cumple requisitos |
| 156 - 181 (60-69%) | **Suficiente** | Implementacion funcional con deficiencias |
| 0 - 155 (<60%) | **Insuficiente** | Requiere mejoras significativas |

**CALIFICACION FINAL**: ________________

---

## Comentarios Generales del Evaluador

### Fortalezas Identificadas
```
[Espacio para comentarios sobre aspectos destacados del proyecto]

Ejemplo:
- Excelente implementacion de patrones de diseno
- Codigo muy limpio y bien documentado
- Arquitectura bien pensada
```

### Areas de Mejora
```
[Espacio para comentarios sobre aspectos a mejorar]

Ejemplo:
- Faltan tests unitarios
- Documentacion de API podria ser mas detallada
- Considerar agregar logging
```

### Recomendaciones
```
[Espacio para recomendaciones especificas]

Ejemplo:
- Agregar tests con pytest
- Implementar sensores reales con threading
- Considerar persistencia con base de datos
```

---

**Evaluador**: ________________________________
**Fecha de Evaluacion**: ____________________
**Firma**: ___________________________________

---

**Version de Rubrica**: 1.0.0
**Ultima Actualizacion**: Octubre 2025
**Proyecto de Referencia**: PythonEstacionamiento v1.0.0
