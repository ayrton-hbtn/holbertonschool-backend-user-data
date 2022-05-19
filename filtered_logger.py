#!/usr/bin/env python3
"""Handling personal data with the logging module"""

import csv
import logging
import re

with open('user_data.csv', 'r') as f:
    PII_FIELDS: tuple = ()
    reader = csv.reader(f)
    fields = next(reader)
    PII = ['name', 'address', 'email', 'ssn', 'passport', 'dl',
           'cc', 'birth', 'dob', 'born', 'phone', 'telephone',
           'vin', 'username', 'password', 'mac', 'ip']
    for field in fields:
        if field in PII:
            if len(PII_FIELDS) < 5:
                PII_FIELDS += (field,)
            else:
                break


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


def get_logger() -> logging.Logger:
    user_logger = logging.Logger("user_data")
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    user_logger.addHandler(handler)
    return user_logger


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
        log: logging.Formatter = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log, self.SEPARATOR)
