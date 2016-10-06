#!/usr/bin/python
#$Id$
#Copyright: ClearWind Consulting Ltd
#License: http://www.clearwind.ca/license

from zopeutils.core import setup

setup(name = "Plone SilverCity",
    version = "1.0",
    maintainer = "ClearWind Consulting Ltd.",
    maintainer_email = "andy@clearwind.ca",
    platforms = ["any",],
    package_dir = {'PloneSilverCity':'.'},
    packages = ['PloneSilverCity',],
    recurse_dirs = [ ['PloneSilverCity', ['skins', 'Extensions' ] ] ], 
    )
