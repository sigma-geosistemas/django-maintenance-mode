# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.core.management.base import BaseCommand
from maintenance_mode import core


class Command(BaseCommand):

    args = '<on|off>'
    help = 'run python manage.py maintenance_mode %s to change maintenance-mode state' % args

    def add_arguments(self, parser):
        parser.add_argument('mode', type=str)

    def handle(self, *args, **options):

        mode = options.get('mode')

        if len(mode) > 0:

            mode = mode.lower()

            if mode in ['on', 'yes', 'true', '1']:
                core.set_maintenance_mode(True)
                print('maintenance on')
                return

            elif mode in ['off', 'no', 'false', '0']:
                core.set_maintenance_mode(False)
                print('maintenance off')
                return
        print(self.help)
