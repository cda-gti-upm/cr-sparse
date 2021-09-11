# Copyright 2021 CR.Sparse Development Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Utility functions for ND arrays
"""

from jax import jit
import jax.numpy as jnp

from .util import promote_arg_dtypes


def arr_largest_index(x):
    """Returns the unraveled index of the largest entry (by magnitude) in an n-d array

    Args:
        x (jax.numpy.ndarray): An nd-array

    Returns:
        tuple: n-dim index of the largest entry in x 
    """
    x = jnp.asarray(x)
    return jnp.unravel_index(jnp.argmax(jnp.abs(x)), x.shape)
