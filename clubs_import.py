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

    school_year = SchoolYear.objects.get_or_create(name='2014/2015')[0]

    i = 0
    for c in rows:
        i += 1
        try:
            category = ClubCategory.objects.get(name=c[3])
        except:
            category = ClubCategory(name=c[3], order=i)
            category.save()
        print c[5]
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
        club = Club(category=category, school_year=school_year)
        club.name = c[0]
        club.description = c[4]
        club.price = int(c[1])
        club.unit  = c[2]
        club.start = '2014-10-01'
        club.end = '2015-06-30'
        club.reg_active = True
        club.save()
        for leader in leaders:
            club.leaders.add(leader)
        
        


if __name__ == "__main__":
    sys.path.insert(0, join(dirname(realpath(__file__)), "app"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    import_clubs()

