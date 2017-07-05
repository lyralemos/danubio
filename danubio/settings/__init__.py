from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'common.py',  # standard django settings
    'database.py',  # postgres
    # 'emails.py',

    # Select the right env:
    '%s.py' % ENV,
    # Optionally override some settings:
    optional('local.py'),
]

# Include settings:
include(*base_settings)
