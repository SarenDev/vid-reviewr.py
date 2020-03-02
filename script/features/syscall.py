import subprocess
import platform
from time import sleep
from .texts import texter

def syscall(cause):
    if platform.system()=="Linux":
        if cause=="pause":
            subprocess.run("read -n 1 -r -s -p 'Press any key to continue...'", shell=True, executable="/bin/bash")
        if cause=="cls":
            subprocess.run("clear", shell=True, executable="/bin/bash")
    elif platform.system()=="Windows":
        if cause=="pause":
            subprocess.run("pause", shell=True)
        if cause=="cls":
            subprocess.run("cls", shell=True)
    else:
        print(texter("incomp"))
        sleep(10)
        quit()