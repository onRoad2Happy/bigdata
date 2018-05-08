#!/usr/bin/env python
import re
import hashlib

def get_bare_principal(normalized_principal_name):
    """
    Given a normalized principal name (nimbus/c6501.ambari.apache.org@EXAMPLE.COM) returns just the
    primary component (nimbus)
    :param normalized_principal_name: a string containing the principal name to process
    :return: a string containing the primary component value or None if not valid
    """

    bare_principal = None

    if normalized_principal_name:
        match = re.match(r"([^/@]+)(?:/[^@])?(?:@.*)?", normalized_principal_name)

    if match:
        bare_principal = match.group(1)

    return bare_principal

def sha256_checksum(password):
    sha256 = hashlib.sha256(password)
    return sha256.hexdigest()