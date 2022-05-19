#!/usr/bin/env python3
"""Personal data"""

import logging
import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str):
    """
    filters the data in message that match the field
    in fields list, and replace it's 'value' with redaction
    """
    for field in message.split(separator):
        if field.split('=')[0] in fields:
            message = re.sub(field.split('=')[1], redaction, message)

    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """inherits init from Formatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        uses the format() method from parent and
        applies and extra filter with filter_datum()
        """
        log = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log, self.SEPARATOR)
