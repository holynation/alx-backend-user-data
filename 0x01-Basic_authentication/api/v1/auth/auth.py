#!/usr/bin/env python3
""" Authentication template module
"""

from flask import request
from typing import List, Pattern, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """requires authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        for _path in excluded_paths:
            if path == _path or path == _path[:-1] or\
                    path.startswith(_path.split('*')[0]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """this function add authorization header"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """this method gets the current user"""
        None
