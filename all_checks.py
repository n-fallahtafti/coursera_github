import os
import sys
import shutil

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

def main():
    if check_reboot():
        print("pending reboot.")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("disk full.")
        sys.exit(1)
    print("everything ok.")
    sys.exit(0)

main()
