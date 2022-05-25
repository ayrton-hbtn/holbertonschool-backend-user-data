#!/usr/bin/env python3
"""Basic Authentication"""

from .auth import Auth


class BasicAuth(Auth):
    """Basic authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header is None or\
                not isinstance(authorization_header, str) or\
                not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split()[1]
