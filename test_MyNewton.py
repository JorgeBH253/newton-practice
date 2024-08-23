import pytest
import numpy as np
import math

import newton

## Important: structure of tests assumes a dictionary with an 'x'
## key as the output. 

def test_basic_function():
    assert np.isclose(newton.optimize(2.95, np.cos), math.pi)

def test_bad_input():
    with pytest.raises(TypeError):
        newton.optimize(np.cos, 2.95)
    
def test_large_input():
    with pytest.raises(RuntimeError):
        newton.optimize(1e8, np.cos)
        

