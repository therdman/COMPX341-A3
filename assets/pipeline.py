import subprocess
import sys
subprocess.run("npm install", shell=True)
try:
    subprocess.run("npm run build", shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(e.returncode)
    print(e.output)
    sys.exit(1)
subprocess.run("git add -A")
subprocess.run("git commit -m \"COMPX341-22A-A3 Commiting from CI/CD Pipeline\"", shell=True)
subprocess.run("git push origin", shell=True)
subprocess.run("npm run start", shell=True)
    
k = input("----")
