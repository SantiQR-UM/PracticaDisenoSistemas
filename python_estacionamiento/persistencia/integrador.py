"""
Archivo integrador generado automaticamente
Directorio: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\persistencia
Fecha: 2025-11-04 15:58:22
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\persistencia\__init__.py
# ================================================================================

# Standard library

# Local application


# ================================================================================
# ARCHIVO 2/2: json_storage.py
# Ruta: C:\Users\santi\OneDrive\Documents\Facultad\Tercer Año\Diseño de sistemas\Parcial\Trabajo miercoles\PythonEstacionamiento\python_estacionamiento\persistencia\json_storage.py
# ================================================================================

"""Sistema de persistencia con JSON.

Permite guardar y cargar el estado del estacionamiento.
"""

# Standard library
import json
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

# Local application
from python_estacionamiento.utils.logger import configurar_logger


class JsonStorage:
    """Gestor de persistencia JSON."""

    def __init__(self, archivo: str = "estacionamiento_estado.json"):
        """Inicializa el gestor de persistencia.

        Args:
            archivo: Nombre del archivo JSON
        """
        self._logger = configurar_logger('JsonStorage')
        self._archivo_path = Path(__file__).parent.parent.parent / 'data' / archivo
        self._archivo_path.parent.mkdir(parents=True, exist_ok=True)

    def guardar_estado(self, estado: Dict[str, Any]) -> bool:
        """Guarda el estado del estacionamiento.

        Args:
            estado: Diccionario con el estado a guardar

        Returns:
            True si se guardó correctamente, False si hubo error
        """
        try:
            # Convertir datetime a string para JSON
            estado_serializable = self._preparar_para_json(estado)

            with open(self._archivo_path, 'w', encoding='utf-8') as f:
                json.dump(estado_serializable, f, indent=2, ensure_ascii=False)

            self._logger.info(f'Estado guardado correctamente en {self._archivo_path}')
            return True

        except Exception as e:
            self._logger.error(f'Error al guardar estado: {e}')
            return False

    def cargar_estado(self) -> Dict[str, Any] | None:
        """Carga el estado del estacionamiento.

        Returns:
            Diccionario con el estado cargado, None si no existe o hay error
        """
        try:
            if not self._archivo_path.exists():
                self._logger.warning(f'Archivo de estado no encontrado: {self._archivo_path}')
                return None

            with open(self._archivo_path, 'r', encoding='utf-8') as f:
                estado = json.load(f)

            # Convertir strings a datetime
            estado_restaurado = self._restaurar_desde_json(estado)

            self._logger.info(f'Estado cargado correctamente desde {self._archivo_path}')
            return estado_restaurado

        except Exception as e:
            self._logger.error(f'Error al cargar estado: {e}')
            return None

    def eliminar_estado(self) -> bool:
        """Elimina el archivo de estado.

        Returns:
            True si se eliminó correctamente, False si no existe o hay error
        """
        try:
            if self._archivo_path.exists():
                self._archivo_path.unlink()
                self._logger.info(f'Estado eliminado: {self._archivo_path}')
                return True
            else:
                self._logger.warning('Archivo de estado no existe, nada que eliminar')
                return False

        except Exception as e:
            self._logger.error(f'Error al eliminar estado: {e}')
            return False

    def _preparar_para_json(self, estado: Dict[str, Any]) -> Dict[str, Any]:
        """Prepara el estado para serialización JSON.

        Args:
            estado: Estado original

        Returns:
            Estado serializable
        """
        estado_json = {
            'timestamp': datetime.now().isoformat(),
            'plazas_ocupadas': estado.get('plazas_ocupadas', 0),
            'capacidad_maxima': estado.get('capacidad_maxima', 100),
            'vehiculos': []
        }

        # Serializar vehículos
        vehiculos = estado.get('vehiculos', {})
        for patente, vehiculo in vehiculos.items():
            vehiculo_data = {
                'patente': patente,
                'tipo': vehiculo.__class__.__name__,
                'superficie': vehiculo.get_superficie(),
                'tarifa_base': vehiculo.get_tarifa_base(),
                'hora_ingreso': vehiculo.get_hora_ingreso().isoformat() if vehiculo.get_hora_ingreso() else None,
                'hora_egreso': vehiculo.get_hora_egreso().isoformat() if vehiculo.get_hora_egreso() else None
            }

            # Agregar atributos específicos por tipo
            if hasattr(vehiculo, 'get_cilindrada'):
                vehiculo_data['cilindrada'] = vehiculo.get_cilindrada()
            elif hasattr(vehiculo, 'get_marca'):
                vehiculo_data['marca'] = vehiculo.get_marca()
            elif hasattr(vehiculo, 'get_capacidad_carga'):
                vehiculo_data['capacidad_carga'] = vehiculo.get_capacidad_carga()

            estado_json['vehiculos'].append(vehiculo_data)

        return estado_json

    def _restaurar_desde_json(self, estado_json: Dict[str, Any]) -> Dict[str, Any]:
        """Restaura el estado desde JSON.

        Args:
            estado_json: Estado en formato JSON

        Returns:
            Estado restaurado
        """
        estado = {
            'plazas_ocupadas': estado_json.get('plazas_ocupadas', 0),
            'capacidad_maxima': estado_json.get('capacidad_maxima', 100),
            'vehiculos_data': estado_json.get('vehiculos', []),
            'timestamp': estado_json.get('timestamp')
        }

        return estado

    def existe_estado(self) -> bool:
        """Verifica si existe un archivo de estado guardado.

        Returns:
            True si existe, False si no
        """
        return self._archivo_path.exists()


