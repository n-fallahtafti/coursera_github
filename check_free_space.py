import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    "true = there is enough free disk space"
    du = shutil.disk_usage(disk)
    percent_free = 00 * du.free / du.total
    gigabytes_free = du.free / 2**30 
    if percent_free<min_percent or gigabytes_free < min_absolute:
        return False
    return True

if not check_disk_usage("/", 2*2**30 , 10):
    print("Error : not enough space")
    sys.exit(1)

print("everything ok")
sys.exit(0)