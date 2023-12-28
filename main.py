"""
Main the application entry.
"""
import sys
from api.application import Application


if __name__ == "__main__":
    app = Application()
    app.run()