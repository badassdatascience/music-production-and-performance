
#
# get the configuration
#
from music_production_and_performance.config import config

#
# load useful libraries
#
import django
from django.conf import settings

#
# configure Django settings
#
settings.configure(
    DEBUG=True,
    INSTALLED_APPS=['theory_western.apps.TheoryWesternConfig'],
    DATABASES = {
        'default' : {
            'ENGINE' : config['django']['database']['ENGINE'],
            'NAME' : config['django']['database']['NAME'],
        }
    }
)

#
# set up Django
#
django.setup()
