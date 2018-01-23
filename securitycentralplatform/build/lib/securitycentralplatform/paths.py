#
# Copyright (C) 2018 SecurityCentral Contributors see COPYING for license
#

'''
This base platform module exports default filesystem paths.
'''

from securitycentralplatform.os_detection import platform_detection

class SecurityCentralPlatformPaths(platform_detection("paths")):
    pass

paths = SecurityCentralPlatformPaths()

