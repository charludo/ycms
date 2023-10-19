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
from django.conf import settings
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.translation import gettext_lazy as _


def file_size_limit(value):
    """
    This function checks if the uploaded file exceeds the file size limit

    :param value: the size of upload file
    :type value: int

    :raises ~django.core.exceptions.ValidationError: when the file size exceeds the size given in the settings.

    """
    if value.size > settings.MEDIA_MAX_UPLOAD_SIZE:
        raise ValidationError(
            _("File too large. Size should not exceed {}.").format(
                filesizeformat(settings.MEDIA_MAX_UPLOAD_SIZE)
            )
        )
