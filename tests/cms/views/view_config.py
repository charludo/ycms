"""
This modules contains the config for the view tests
"""

from ...conftest import ALL_ROLES, DOCTOR, MANAGER, ROOT

#: This list contains the config for all views
#: Each element is a tuple which consists of two elements: A list of view configs and the keyword arguments that are
#: identical for all views in this list. Each view config item consists of the name of the view, the list of roles that
#: are allowed to access that view and optionally post data that is sent with the request. The post data can either be
#: a dict to send form data or a string to send JSON.
VIEWS = [
    (
        [
            ("cms:public:index", ALL_ROLES),
            (
                "cms:public:index",
                [ROOT, MANAGER, DOCTOR],
                {
                    "first_name": "Firstname",
                    "last_name": "Lastname",
                    "private_patient": True,
                    "diagnosis_code": "Testcode",
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
