# coding: utf-8
"""
This module contains various helpers for migrations testing.
"""
import os

from django import VERSION, setup


setup()


MIGRATION_NAME = 'test'


def makemigrations():
    from django.core.management import call_command
    from django.core.management.commands.makemigrations import Command

    os.system('find . -name \*.pyc -delete')
    if VERSION >= (1, 10):
        call_command('makemigrations', 'money_app', name=MIGRATION_NAME)
    else:
        # In Django 1.8 & 1.9 first argument name clashes with command option.
        Command().execute('money_app', name=MIGRATION_NAME, verbosity=1)


def get_migration(name):
    return __import__('money_app.migrations.%s_%s' % (name, MIGRATION_NAME), fromlist=['Migration']).Migration


def get_operations(migration_name):
    return get_migration(migration_name).operations


def migrate():
    from django.core.management import call_command

    call_command('migrate', 'money_app')
