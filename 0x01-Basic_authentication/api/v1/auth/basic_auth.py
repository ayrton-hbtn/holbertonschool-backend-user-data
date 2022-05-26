#!/usr/bin/env python3
"""Basic Authentication"""

from asyncio.base_events import _ExceptionHandler
from .auth import Auth
from typing import Tuple, TypeVar
import base64


class BasicAuth(Auth):
    """Basic authentication"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""

        if authorization_header is None or\
                not isinstance(authorization_header, str) or\
                not authorization_header.startswith('Basic '):

            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """decodes the Basic Authorization header value from Base64"""

        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):

            return None
        try:
            value = base64.b64decode(base64_authorization_header)
            return value.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        returns the user email and password from
        the Base64 decoded value
        """

        if decoded_base64_authorization_header is None or\
                not isinstance(decoded_base64_authorization_header, str) or\
                ":" not in decoded_base64_authorization_header:

            return (None, None)
        else:
            credentials = decoded_base64_authorization_header.split(":")
            return (credentials[0], credentials[1])

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on their email and password
        """

        if user_email is None or not isinstance(user_email, str) or\
                user_pwd is None or not isinstance(user_pwd, str):

            return None
        try:
            from models.user import User

            users = User.search({"email": user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None
