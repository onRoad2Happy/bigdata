#!/usr/bin/env python
from resource_management.libraries.functions import format
from resource_management.libraries.script.script import Script

config = Script.get_config()

clickhouse_pid_dir = config['configurations']['clickhouse-env']['clickhouse_pid_dir']
clickhouse_pid_file = format("{clickhouse_pid_dir}/clickhouse-server.pid")
