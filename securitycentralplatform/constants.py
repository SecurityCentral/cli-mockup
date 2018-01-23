#
# Copyright (C) 2018 SecurityCentral Contributors see LICENSE for license
#

'''
This base platform module exports platform related constants.
'''

from securitycentralplatform.os_detection import platform_detection

class SecurityCentralPlatformConstants(platform_detection("constants")):
    pass

constants = SecurityCentralPlatformConstants()
