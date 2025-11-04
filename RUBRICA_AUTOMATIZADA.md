# Rubrica de Evaluacion Automatizada - Sistema de Estacionamiento

**Proyecto**: PythonEstacionamiento
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Proposito**: Automatizacion de correccion de proyectos

---

## Introduccion

Este documento define criterios de evaluacion automatizables para proyectos de software que implementen patrones de diseno. Cada criterio incluye:

- **ID unico**: Para referencia en workflows
- **Tipo de verificacion**: Estatica (codigo) o Dinamica (ejecucion)
- **Metodo de deteccion**: Como automatizar la verificacion
- **Comando/Regex**: Script o patron para ejecutar
- **Puntaje**: Puntos asignados al criterio
- **Threshold**: Umbral de aprobacion

---

## Seccion 1: Verificaciones Estaticas (Analisis de Codigo)

### 1.1 Patron SINGLETON

**SING-001: Atributo de Instancia Unica**
```json
{
  "id": "SING-001",
  "categoria": "Singleton",
  "descripcion": "Verificar atributo _instance en clase",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn '_instance = None' --include='*.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
```

**SING-002: Metodo __new__ Implementado**
```json
{
  "id": "SING-002",
  "categoria": "Singleton",
  "descripcion": "Verificar metodo __new__ para control de instancia",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def __new__' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

**SING-003: Thread-Safety con Lock**
```json
{
  "id": "SING-003",
  "categoria": "Singleton",
  "descripcion": "Verificar uso de threading.Lock",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'threading.Lock\\|from threading import Lock' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
```

**SING-004: Metodo get_instance()**
```json
{
  "id": "SING-004",
  "categoria": "Singleton",
  "descripcion": "Verificar metodo get_instance()",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def get_instance' --include='*.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "medio"
}
```

### 1.2 Patron FACTORY METHOD

**FACT-001: Metodo Factory Estatico**
```json
{
  "id": "FACT-001",
  "categoria": "Factory",
  "descripcion": "Verificar metodo factory estatico",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn '@staticmethod' --include='*factory*.py' .",
  "puntaje": 3,
  "threshold": 2,
  "peso": "critico"
}
```

**FACT-002: Clase Factory Existe**
```json
{
  "id": "FACT-002",
  "categoria": "Factory",
  "descripcion": "Verificar existencia de clase Factory",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -name '*factory*.py' -type f",
  "puntaje": 2,
  "threshold": 1,
  "peso": "critico"
}
```

**FACT-003: Diccionario de Factories**
```json
{
  "id": "FACT-003",
  "categoria": "Factory",
  "descripcion": "Verificar uso de diccionario para dispatch",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'factories = {' --include='*factory*.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "medio"
}
```

### 1.3 Patron OBSERVER

**OBSR-001: Clase Observable Existe**
```json
{
  "id": "OBSR-001",
  "categoria": "Observer",
  "descripcion": "Verificar clase Observable",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Observable' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

**OBSR-002: Clase Observer Existe**
```json
{
  "id": "OBSR-002",
  "categoria": "Observer",
  "descripcion": "Verificar interfaz Observer",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class Observer' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

**OBSR-003: Uso de Generics**
```json
{
  "id": "OBSR-003",
  "categoria": "Observer",
  "descripcion": "Verificar uso de Generic[T]",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'Generic\\[T\\]\\|Observable\\[' --include='*.py' .",
  "puntaje": 4,
  "threshold": 2,
  "peso": "alto"
}
```

**OBSR-004: Metodo notificar_observadores**
```json
{
  "id": "OBSR-004",
  "categoria": "Observer",
  "descripcion": "Verificar metodo de notificacion",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def notificar_observadores' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
```

### 1.4 Patron STRATEGY

**STRT-001: Interfaz Strategy Abstracta**
```json
{
  "id": "STRT-001",
  "categoria": "Strategy",
  "descripcion": "Verificar interfaz Strategy abstracta",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class.*Strategy.*ABC' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
```

**STRT-002: Implementaciones de Strategy**
```json
{
  "id": "STRT-002",
  "categoria": "Strategy",
  "descripcion": "Verificar al menos 2 implementaciones",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'Strategy):' --include='*.py' .",
  "puntaje": 4,
  "threshold": 2,
  "peso": "critico"
}
```

### 1.5 Calidad de Codigo

**QUAL-001: Constantes Centralizadas**
```json
{
  "id": "QUAL-001",
  "categoria": "Calidad",
  "descripcion": "Verificar archivo constantes.py existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -name 'constantes.py' -type f",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
```

**QUAL-002: NO Lambdas**
```json
{
  "id": "QUAL-002",
  "categoria": "Calidad",
  "descripcion": "Verificar ausencia de lambdas",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'lambda ' --include='*.py' . | wc -l",
  "puntaje": 2,
  "threshold": 0,
  "peso": "medio",
  "inverted": true
}
```

**QUAL-003: Type Hints**
```json
{
  "id": "QUAL-003",
  "categoria": "Calidad",
  "descripcion": "Verificar uso de type hints",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def.*->\\|: str\\|: int\\|: float' --include='*.py' . | wc -l",
  "puntaje": 3,
  "threshold": 50,
  "peso": "medio"
}
```

### 1.6 Estructura del Proyecto

**STRC-001: Paquete entidades/**
```json
{
  "id": "STRC-001",
  "categoria": "Estructura",
  "descripcion": "Verificar paquete entidades existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -type d -name 'entidades'",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
```

**STRC-002: Paquete servicios/**
```json
{
  "id": "STRC-002",
  "categoria": "Estructura",
  "descripcion": "Verificar paquete servicios existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -type d -name 'servicios'",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
```

**STRC-003: Paquete patrones/**
```json
{
  "id": "STRC-003",
  "categoria": "Estructura",
  "descripcion": "Verificar paquete patrones existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -type d -name 'patrones'",
  "puntaje": 2,
  "threshold": 1,
  "peso": "critico"
}
```

---

## Seccion 2: Verificaciones Dinamicas (Ejecucion)

### 2.1 Ejecucion Exitosa

**EXEC-001: Ejecutar main.py Sin Errores**
```json
{
  "id": "EXEC-001",
  "categoria": "Ejecucion",
  "descripcion": "Verificar que main.py ejecuta sin errores",
  "tipo": "dinamica",
  "metodo": "python",
  "comando": "timeout 30 python main.py",
  "puntaje": 10,
  "threshold": 0,
  "peso": "critico",
  "validacion": "return_code == 0"
}
```

**EXEC-002: Mensaje de Exito Final**
```json
{
  "id": "EXEC-002",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje EJEMPLO COMPLETADO EXITOSAMENTE",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep 'EJEMPLO COMPLETADO EXITOSAMENTE'",
  "puntaje": 5,
  "threshold": 1,
  "peso": "critico"
}
```

**EXEC-003: No Excepciones No Manejadas**
```json
{
  "id": "EXEC-003",
  "categoria": "Ejecucion",
  "descripcion": "Verificar ausencia de tracebacks",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'traceback\\|error:' | wc -l",
  "puntaje": 5,
  "threshold": 0,
  "peso": "alto",
  "inverted": true
}
```

### 2.2 Patrones en Accion

**EXEC-004: Patron Singleton Demostrado**
```json
{
  "id": "EXEC-004",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje de Singleton en output",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'singleton'",
  "puntaje": 3,
  "threshold": 1,
  "peso": "medio"
}
```

**EXEC-005: Patron Factory Demostrado**
```json
{
  "id": "EXEC-005",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje de Factory en output",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'factory'",
  "puntaje": 3,
  "threshold": 1,
  "peso": "medio"
}
```

**EXEC-006: Patron Strategy Demostrado**
```json
{
  "id": "EXEC-006",
  "categoria": "Ejecucion",
  "descripcion": "Verificar mensaje de Strategy en output",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'strategy'",
  "puntaje": 3,
  "threshold": 1,
  "peso": "medio"
}
```

### 2.3 Funcionalidad

**EXEC-007: Vehiculos Funcionando**
```json
{
  "id": "EXEC-007",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar ingreso/egreso de vehiculos",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'ingres\\|egres\\|vehiculo'",
  "puntaje": 3,
  "threshold": 4,
  "peso": "alto"
}
```

**EXEC-008: Pricing Funcional**
```json
{
  "id": "EXEC-008",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar calculo de precios",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'precio\\|estrategia'",
  "puntaje": 3,
  "threshold": 2,
  "peso": "alto"
}
```

---

## Configuracion JSON Completa

```json
{
  "evaluacion": {
    "version": "1.0.0",
    "proyecto": "PythonEstacionamiento",
    "puntaje_maximo": 260,
    "umbral_aprobacion": 182,
    "criterios": [
      {
        "id": "SING-001",
        "categoria": "Singleton",
        "tipo": "estatica",
        "comando": "grep -rn '_instance = None' --include='*.py' .",
        "puntaje": 2,
        "threshold": 1,
        "peso": "alto"
      },
      {
        "id": "SING-002",
        "categoria": "Singleton",
        "tipo": "estatica",
        "comando": "grep -rn 'def __new__' --include='*.py' .",
        "puntaje": 3,
        "threshold": 1,
        "peso": "critico"
      },
      {
        "id": "FACT-001",
        "categoria": "Factory",
        "tipo": "estatica",
        "comando": "grep -rn '@staticmethod' --include='*factory*.py' .",
        "puntaje": 3,
        "threshold": 2,
        "peso": "critico"
      },
      {
        "id": "OBSR-001",
        "categoria": "Observer",
        "tipo": "estatica",
        "comando": "grep -rn 'class Observable' --include='*.py' .",
        "puntaje": 3,
        "threshold": 1,
        "peso": "critico"
      },
      {
        "id": "STRT-001",
        "categoria": "Strategy",
        "tipo": "estatica",
        "comando": "grep -rn 'class.*Strategy.*ABC' --include='*.py' .",
        "puntaje": 3,
        "threshold": 1,
        "peso": "critico"
      },
      {
        "id": "EXEC-001",
        "categoria": "Ejecucion",
        "tipo": "dinamica",
        "comando": "timeout 30 python main.py",
        "puntaje": 10,
        "threshold": 0,
        "peso": "critico",
        "validacion": "return_code == 0"
      },
      {
        "id": "QUAL-001",
        "categoria": "Calidad",
        "tipo": "estatica",
        "comando": "find . -name 'constantes.py' -type f",
        "puntaje": 3,
        "threshold": 1,
        "peso": "alto"
      }
    ]
  }
}
```

---

## Pesos de Criterios

| Peso | Valor Numerico | Uso |
|------|----------------|-----|
| critico | 1.5x | Criterios fundamentales (patrones principales) |
| alto | 1.2x | Criterios importantes (calidad, estructura) |
| medio | 1.0x | Criterios deseables (documentacion, type hints) |
| bajo | 0.8x | Criterios opcionales (metricas, extras) |
| bonus | 0.5x | Criterios adicionales (tests, CI/CD) |

---

## Conclusiones

Este sistema de evaluacion automatizada permite:

- **Evaluacion objetiva**: Criterios verificables automaticamente
- **Escalabilidad**: Evaluar multiples proyectos simultaneamente
- **Consistencia**: Mismos criterios para todos los proyectos
- **Rapidez**: Evaluacion completa en < 1 minuto
- **Trazabilidad**: Reportes detallados en JSON/Markdown

---

**Version**: 1.0.0
**Ultima Actualizacion**: Octubre 2025
**Proyecto**: PythonEstacionamiento
