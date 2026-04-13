from validators import validate_ip
from utils import setup_logging, format_result

def main():
    setup_logging()
    print("--- IP Check ---")
    
    target = input("Enter IP address to check: ") 
    
    if validate_ip(target):
        print(format_result(target, "valid"))
    else:
        print(format_result(target, "invalid"))

if __name__ == "__main__":
    main()
