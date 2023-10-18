"""
This module contains helpers for the account activation process
(also see :class:`~ycms.cms.views.authentication.account_activation_view.AccountActivationView`).
"""
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    This token generator is identical to the default password reset token generator of :mod:`django.contrib.auth` with
    the exception of the used HMAC salt.
    """

    key_salt = "ycms.cms.utils.token_generator.AccountActivationTokenGenerator"


class CustomPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    """
    This token generator is identical to the default password reset token generator of :mod:`django.contrib.auth` with
    the exception of the used HMAC salt.
    This means password reset tokens are no longer accepted for the account activation and vice versa.
    """

    key_salt = "ycms.cms.utils.token_generator.PasswordResetTokenGenerator"


account_activation_token_generator = AccountActivationTokenGenerator()
password_reset_token_generator = CustomPasswordResetTokenGenerator()
