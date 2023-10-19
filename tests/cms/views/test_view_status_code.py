# Copyright [2019] [Integreat Project]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest

from .utils import check_view_status_code
from .view_config import PARAMETRIZED_VIEWS


@pytest.mark.django_db
@pytest.mark.parametrize("view_name,kwargs,post_data,roles", PARAMETRIZED_VIEWS)
def test_view_status_code_1(login_role_user, view_name, kwargs, post_data, roles):
    check_view_status_code(login_role_user, view_name, kwargs, post_data, roles)
