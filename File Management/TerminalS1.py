import subprocess
#subprocess library : that allows python script to interact with command line terminal or shell.
#check_Call : it runs in executable in terminal and waits untill the process has finished in before 
#continuing the script

for i in range(0,10):
    subprocess.check_call(['python','HelloScript.py'])
