#!/usr/bin/env python3

from distutils.core import setup

setup(name='securitycentralplatform',
      package_dir={'securitycentralplatform': ''},
      namespace_packages=['securitycentralplatform'],
      packages=['securitycentralplatform', 'securitycentralplatform.base'],
     )
