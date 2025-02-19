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
First order conic solvers
"""
from cr.sparse._src.focs.util import (
    matrix_affine_func
)

from cr.sparse._src.focs.focs import focs
from cr.sparse._src.focs.l1rls import (l1rls, l1rls_jit)
from cr.sparse._src.focs.lasso import (lasso, lasso_jit)
from cr.sparse._src.focs.owl1rls import (owl1rls, owl1rls_jit)

from cr.sparse._src.focs.defs import (
    FOCSOptions,
    FOCSState
)
