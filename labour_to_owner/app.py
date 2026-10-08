"""
Redirect wrapper for backwards compatibility with Streamlit Cloud and legacy scripts.
Runs the main SalaryScope application.
"""

import sys
import os

# Add parent directory to path so imports resolve
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from app import main

if __name__ == "__main__":
    main()
