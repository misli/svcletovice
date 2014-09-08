#!/usr/bin/env python
# -*- encoding: utf8 -*-

import os
import sys
from os.path import dirname, realpath, join


def import_clubs():
    from django.utils.text import slugify
    from domecek.models import *
    from clubs import rows
    from django.contrib.auth.models import User

    # prvni radek jsou hlavicky
    del(rows[0])

    for c in rows:
        try:
            club = Club.objects.get(name=c[0])
        except:
            print c[0]
            continue
        leaders = []
        for leader_name in c[5] and c[5].strip().split(' a ') or []:
            leader_name = leader_name.strip()
            leader_username = slugify(leader_name)
            try:
                leader = User.objects.get(username=leader_username)
            except:
                leader = User()
                leader.first_name, leader.last_name = leader_name.split(' ')
                leader.username = leader_username
                leader.save()
            leaders.append(leader)
        club.leaders = leaders


if __name__ == "__main__":
    sys.path.insert(0, join(dirname(realpath(__file__)), "app"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    import_clubs()

