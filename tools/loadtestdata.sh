#!/bin/bash
# Copyright [2019] [Integreat Project]
# Copyright [2023] [YCMS]
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

# This script imports test data into the database.

# Import utility functions
# shellcheck source=./tools/utils/_functions.sh
source "$(dirname "${BASH_SOURCE[0]}")/utils/_functions.sh"

require_installed
require_database

# temporarily disabled some of these until after the midterm
deescalate_privileges ycms-cli loaddata "${PACKAGE_DIR}/cms/fixtures/icd10_test_data.json" --verbosity "${SCRIPT_VERBOSITY}"
deescalate_privileges ycms-cli loaddata "${PACKAGE_DIR}/cms/fixtures/test_data.json" --verbosity "${SCRIPT_VERBOSITY}"
# deescalate_privileges ycms-cli loaddata "${PACKAGE_DIR}/cms/fixtures/test_data_extended.json" --verbosity "${SCRIPT_VERBOSITY}"
deescalate_privileges ycms-cli loaddata "${PACKAGE_DIR}/cms/fixtures/midterm_data.json" --verbosity "${SCRIPT_VERBOSITY}"

echo "✔ Imported test data" | print_success
