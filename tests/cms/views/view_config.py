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
"""
This modules contains the config for the view tests
"""

from ...conftest import MEDICAL_PERSONNEL, ROOT, STATION_MANAGEMENT

#: This list contains the config for all views
#: Each element is a tuple which consists of two elements: A list of view configs and the keyword arguments that are
#: identical for all views in this list. Each view config item consists of the name of the view, the list of roles that
#: are allowed to access that view and optionally post data that is sent with the request. The post data can either be
#: a dict to send form data or a string to send JSON.
VIEWS = [
    (
        [
            ("cms:protected:patients", [ROOT, STATION_MANAGEMENT, MEDICAL_PERSONNEL]),
            ("cms:protected:intake", [ROOT, STATION_MANAGEMENT, MEDICAL_PERSONNEL]),
            (
                "cms:protected:intake",
                [ROOT, STATION_MANAGEMENT, MEDICAL_PERSONNEL],
                {
                    "patient": "185",
                    "diagnosis_code": "80173",
                    "admission_date": "2023-01-01",
                },
            ),
            (
                "cms:protected:intake",
                [ROOT, STATION_MANAGEMENT, MEDICAL_PERSONNEL],
                {
                    "first_name": "Firstname",
                    "last_name": "Lastname",
                    "insurance_type": True,
                    "date_of_birth": "2023-01-01",
                    "gender": "d",
                    "diagnosis_code": "80173",
                    "admission_date": "2023-01-01",
                    "accompanied": True,
                    "note": "test note",
                },
            ),
        ],
        {},
    )
]

#: In order for these views to be used as parameters, we have to flatten the nested structure
PARAMETRIZED_VIEWS = [
    (view_name, kwargs, post_data[0] if post_data else {}, roles)
    for view_conf, kwargs in VIEWS
    for view_name, roles, *post_data in view_conf
]
