import pandas as pd
import numpy as np

chat_id = 578001199


def solution(x: np.array) -> float:
	time = 10
	d = -31+np.exp(1) 
	a =  ((np.mean(x) - d) / time)
    return a

