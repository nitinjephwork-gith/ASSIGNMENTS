import sys
from datetime import datetime

print("Dockerized Python Application")
print("-" * 30)

print("Python Version:")
print(sys.version)

print("\nCurrent Date and Time:")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))