#!/usr/bin/env python
import os


from resource_management.core.resources.system import Execute
from resource_management.libraries.functions import format
from resource_management.libraries.functions import Direction
from resource_management.core.exceptions import Fail
from resource_management.core.logger import Logger

def run_migration(env, upgrade_type):
  """
  If the acl migration script is present, then run it for either upgrade or downgrade.
  That script was introduced in JDP 2.3.4.0 and requires stopping all clickhouse server first.
  Requires configs to be present.
  :param env: Environment.
  :param upgrade_type: "rolling" or "nonrolling
  """
  pass