print("Test")
from datetime import datetime

delta = datetime.now() - datetime(1900,12,31)
delta_a = datetime.now() - datetime(1990,3,14,18,30)

print(delta.days)
print(delta_a.days)
