import logging
from typing import Optional

from app.core.config import settings


def setup_logging(
    log_level: Optional[str] = None,
    log_file: Optional[str] = None,
    log_format: Optional[str] = None
) -> None:
    """
    Настройка системы логирования

    Args:
        log_level: Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Путь к файлу логов
        log_format: Формат сообщений логов
    """
    # Используем настройки из конфигурации, если параметры не переданы
    log_level = log_level or settings.log_level
    log_file = log_file or settings.log_file
    log_format = log_format or settings.log_format

    formater = logging.Formatter(log_format)