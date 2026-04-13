import logging

def setup_logging():
    logging.info("Logging system started")
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def format_result(data, status):
    """Форматує вивід результату."""
    return f"[{status.upper()}] Result: {data}"
