"""Sistema de logging centralizado.

Proporciona configuración de logging para todo el sistema.
"""

# Standard library
import logging
import sys
from pathlib import Path
from datetime import datetime


def configurar_logger(nombre: str, nivel: int = logging.INFO) -> logging.Logger:
    """Configura y retorna un logger.

    Args:
        nombre: Nombre del logger
        nivel: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        Logger configurado
    """
    logger = logging.getLogger(nombre)
    logger.setLevel(nivel)

    # Evitar duplicar handlers
    if logger.handlers:
        return logger

    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(nivel)

    # Handler para archivo
    logs_dir = Path(__file__).parent.parent.parent / 'logs'
    logs_dir.mkdir(exist_ok=True)

    fecha = datetime.now().strftime('%Y%m%d')
    file_handler = logging.FileHandler(
        logs_dir / f'estacionamiento_{fecha}.log',
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)

    # Formato de mensajes
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Agregar handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
