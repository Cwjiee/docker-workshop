import datetime
import platform
import socket

def get_system_info():
    now = datetime.datetime.now()
    hostname = socket.gethostname()
    python_version = platform.python_version()
    os_info = platform.system()

    print("=" * 40)
    print("   Welcome to the Docker Challenge!")
    print("=" * 40)
    print(f"  Time        : {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Hostname    : {hostname}")
    print(f"  OS          : {os_info}")
    print(f"  Python      : {python_version}")
    print("=" * 40)
    print("  You successfully containerised a")
    print("  Python app. Nice work!")
    print("=" * 40)

if __name__ == "__main__":
    get_system_info()
