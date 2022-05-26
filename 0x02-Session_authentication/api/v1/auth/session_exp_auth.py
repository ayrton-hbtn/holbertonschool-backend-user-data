#!/usr/bin/env python3

""" Session with expiration date
"""

from .session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    """
    def __init__(self):
        """
        """
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        """
        try:
            session_id = super().create_session(user_id)
            if not session_id:
                return None

            self.user_id_by_session_id[session_id] = {
                "user_id": user_id,
                "created_at": datetime.now()
            }

            return session_id

        except Exception:
            return None

    def user_id_for_session_id(self, session_id=None):
        """
        """
        if not session_id:
            return None

        session = self.user_id_by_session_id.get(session_id)

        if not session:
            return None

        if self.session_duration >= 0:
            if not session.get('created_at'):
                return None
            if session.get('created_at') +\
                    timedelta(seconds=self.session_duration) < datetime.now():
                return None

            return session.get('user_id')
