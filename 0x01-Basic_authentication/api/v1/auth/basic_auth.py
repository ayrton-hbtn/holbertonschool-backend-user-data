#!/usr/bin/env python3
"""Basic Authentication"""

from .auth import Auth
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
