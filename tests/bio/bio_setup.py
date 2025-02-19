import pytest

import numpy as np
from numpy.testing import (assert_almost_equal, assert_allclose, assert_,
                           assert_equal, assert_raises, assert_raises_regex,
                           assert_array_equal, assert_warns)

import jax
import jax.numpy as jnp
from jax import random, lax, vmap


import cr.nimble as cnb
import cr.sparse as crs
import cr.sparse.lop as lop
import cr.sparse.sls as sls
import cr.sparse.dict as crdict
import cr.sparse.bio as bio

rtol = 1e-8 if jax.config.jax_enable_x64 else 1e-6
atol = 1e-7 if jax.config.jax_enable_x64 else 1e-5
