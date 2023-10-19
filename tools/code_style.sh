#!/bin/bash
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

# This script can be used to runs all of our code style tools: isort, djlint, black, pylint, eslint and prettier

# Import utility functions
# shellcheck source=./tools/utils/_functions.sh
source "$(dirname "${BASH_SOURCE[0]}")/utils/_functions.sh"

require_installed
ensure_not_root

# Run isort
bash "${DEV_TOOL_DIR}/isort.sh"

# Run black
bash "${DEV_TOOL_DIR}/black.sh"

# Run djlint
bash "${DEV_TOOL_DIR}/djlint.sh"

# Run pylint
bash "${DEV_TOOL_DIR}/pylint.sh"

# Run eslint
bash "${DEV_TOOL_DIR}/eslint.sh"

# Run prettier
bash "${DEV_TOOL_DIR}/prettier.sh"
