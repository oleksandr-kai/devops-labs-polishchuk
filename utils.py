import logging

def setup_logging():
    """Налаштування логування (знадобиться для Частини 2 [cite: 39])."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def format_result(data, status):
    """Форматує вивід результату."""
    return f"[{status.upper()}] Result: {data}"
