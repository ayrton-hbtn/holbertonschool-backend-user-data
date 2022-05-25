#!/usr/bin/env python3
"""Authentication"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Class for user authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ TO-DO implementation
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ TO-DO implementation
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ TO-DO implementation
        """
        return None
