#
# Copyright (C) 2018 SecurityCentral Contributors see COPYING for license
#

"""
This base platform module exports platform related tasks.
"""

from securitycentralplatform.os_detection import platform_detection

class SecurityCentralPlatformTasks(platform_detection("tasks")):
    pass

tasks = SecurityCentralPlatformTasks()
