#!/usr/bin/env python

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

import os
import sys
from os.path import dirname, realpath, join

if __name__ == "__main__":
    sys.path.insert(0, join(dirname(realpath(__file__)), "app"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    if os.getuid() == 0:
        import pwd
        user = pwd.getpwnam('django-svcletovice')
        os.setgid(user.pw_gid)
        os.setuid(user.pw_uid)
        os.environ['USER']  = user.pw_name
        os.environ['HOME']  = user.pw_dir
        os.environ['SHELL'] = user.pw_shell
        if os.path.exists(os.environ['HOME']):
            os.chdir(os.environ['HOME'])

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
