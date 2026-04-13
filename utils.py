# Start of logging logic

import logging

def setup_logging():
    print("DEBUG: Logger initialized")
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def format_result(data, status):
    """Форматує вивід результату."""
    return f"[{status.upper()}] Result: {data}"
