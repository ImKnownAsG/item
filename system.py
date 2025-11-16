import sys
import subprocess

print(sys.argv)
for _ in sys.argv:
    print(_)

#This would be a bad idea - it would loop endlessly
#result = subprocess.run(["python", "./system.py"], capture_output = True, 
#  text = True, check = True)

result = subprocess.run(["powershell", "-Command", "2+3"],
  capture_output = True, text = True, check = True)
print(result)
print(result.stdout)