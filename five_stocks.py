# =============================================================================
# IMPORTS — All necessary libraries for this lesson
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import statsmodels.api as sm
from scipy import stats

# Configure display options
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 120)
pd.set_option('display.precision', 4)
np.set_printoptions(precision=4, suppress=True)

# Configure plot style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# Set random seed for reproducibility
np.random.seed(42)
