#!/usr/bin/env python3
"""Personal data"""

import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str):
    """
    filters the data in message that match the field
    in fields list, and replace it's 'value' with redaction
    """
    for field in fields:
        for msg_field in message.split(separator)[:-1:]:
            msg_field = msg_field.split('=')
            parameter = msg_field[0]
            value = msg_field[1]
            if field == parameter:
                message = re.sub(value, redaction, message)

    return message
