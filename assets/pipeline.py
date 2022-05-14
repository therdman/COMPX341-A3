import subprocess
import sys
if(len(sys.argv) != 2):
    print("Please give a commit message, and not other arguments")
    k = input("press enter to exit")
    sys.exit(1)
commitMessage = sys.argv[1]
subprocess.run("npm install", shell=True)
try:
    subprocess.run("npm run build", shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(e.returncode)
    print(e.output)
    k = input("press enter to exit")
    sys.exit(1)
subprocess.run("git add -A")
subprocess.run(f"git commit -m \"{commitMessage}\"", shell=True)
subprocess.run("git push origin", shell=True)
subprocess.run("npm run start", shell=True)

