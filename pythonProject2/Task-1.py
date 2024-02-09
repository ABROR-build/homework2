import os
import platform

print("\nOs name:", platform.system())
print("OS version:", platform.release())
print("Current working directory: ", os.getcwd())
print("Current directories: ", os.listdir())