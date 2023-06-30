import os
import sys

def check_reboot():
    "return True if the computer has a pending reboot"
    return os.path.exists("/run/reboot-required")

print("other person is working :)) ")
def main():
    if check_reboot():
        print("pending reboot.")
        sys.exit(1)
    print("everything ok.")
    sys.exit(0)

main()
