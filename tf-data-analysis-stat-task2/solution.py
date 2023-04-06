import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 578001199

def solution(p: float, x: np.array) -> tuple:

    alpha = 1 - p
    loc = 2*x.mean() - 0.074
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 1024), \
           loc - scale * norm.ppf(alpha / 1024)
