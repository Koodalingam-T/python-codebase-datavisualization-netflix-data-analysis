import os
import pandas as pd

# Path Configurations
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DATA_PATH = os.path.join(BASE_DIR, "data", "netflix_sample_data.csv")

# Plotly Visual Theme Settings
COLOR_PRIMARY = "#E50914"  # Netflix Red
COLOR_SECONDARY = "#222222"  # Charcoal Dark
FONT_FAMILY = "consolas"

def apply_pandas_settings():
    """Applies standardized data display choices."""
    pd.set_option("display.max_columns", None)
    pd.options.display.float_format = "{:,.3f}".format

