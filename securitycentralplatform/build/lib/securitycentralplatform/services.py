#
# Copyright (C) 2018 SecurityCentral Contributors see COPYING for license
#

"""
This base platform module exports platform related services.
"""

from securitycentralplatform.os_detection import platform_detection

class SecurityCentralPlatformServices(platform_detection("services")):
    pass

services = SecurityCentralPlatformServices()
