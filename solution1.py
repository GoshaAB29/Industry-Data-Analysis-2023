import pandas as pd
import numpy as np

chat_id = 578001199

def solution(x: np.array) -> float:
	
    time = 10 
    length = len(x) 
    v0 = x 
    v1 = x + np.random.normal(-43, np.exp(1), size=length) 
    d = np.trapz(v1, dx=time)
    
    a = 2*(d - v0*time*length)/(time**2 * length)
    mse = ((pd.Series(a) - 2)**2).mean() 
    
    return x.mean()
	
