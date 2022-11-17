import subprocess
import sys

zz = subprocess.check_output(["arp", "-a"], timeout=5).decode("cp866")
print(zz)