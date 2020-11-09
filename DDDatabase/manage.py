#!/usr/bin/env python
# 这里要注意source root的使用
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DDDatabase.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
