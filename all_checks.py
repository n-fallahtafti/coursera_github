import os
import shutil
import socket
import psutil

#these functions check the disk ! 
def check_reboot():
    "return True if the computer has a pending reboot"
    return os.path.exists("/run/reboot-required")
def check_disk_full(disk, min_gb, min_percent):
    "true = there is enough free disk space"
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30 
    if percent_free<min_percent or gigabytes_free < min_gb:
        return True
    return False
def check_root_full():
    "True = root partition is full."
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_cpu_constrained():
    """True = CPU is having too much usage"""
    return psutil.cpu_percent(1) > 75

def check_no_network():
    """true = fails to resolve Google's URL """
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def main():
    checks=[
        (check_reboot,"pending reboot"),
        (check_root_full,"root is full."),
        (check_cpu_constrained, "CPU load too high."),
        (check_no_network,"no working network")
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok=False
    
    if not everything_ok:
        os._exit(1)
    print("everything ok.")
    os._exit(0)

main()
