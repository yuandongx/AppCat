"""
Main the application entry.
"""
import os

from app.application import Application


if __name__ == "__main__":
    pid = os.getpid()
    pid_file = os.environ.get('APP_PID_FILE', 'pid')
    with open(pid_file, 'w') as f:
        f.write(f'{pid}')
    app = Application()
    app.run()
