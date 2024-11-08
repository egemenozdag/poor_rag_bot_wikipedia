# main.py
from app_interface import AppInterface  # Import AppInterface class from app_interface.py
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['DYLD_LIBRARY_PATH'] = '/usr/local/lib'


def main():
    # Start the RAG system
    app = AppInterface()
    app.run()

if __name__ == "__main__":
    main()
