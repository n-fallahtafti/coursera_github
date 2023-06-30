import os
import sys
import shutil

def check_reboot():
    "return True if the computer has a pending reboot"
    return os.path.exists("/run/reboot-required")


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
