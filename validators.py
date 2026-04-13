import re

def validate_ip(ip):
    """Перевіряє, чи є рядок валідною IPv4 адресою."""
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(pattern, ip):
        return True
    return False

def validate_domain(domain):
    """Проста перевірка формату домену."""
    return "." in domain and len(domain) > 3
