"""Nettacker main.py."""

import subprocess
import platform
import sys

from nettacker.core.app import Nettacker


def check_internet():
    """Check internet connection before running the application."""
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        subprocess.check_call(['ping', param, '1', 'www.google.com'], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        return True
    except:
        return False


def run():
    if not check_internet():
        print("Error: No internet connection! Please check your network.")
        sys.exit(1)
    app = Nettacker()
    app.run()
