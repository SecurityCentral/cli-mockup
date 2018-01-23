#
# Copyright (C) 2018 SecurityCentral Contributors see COPYING for license
#

import os
import distro

rh_derivatives = ("fedora", "centos", "rhel", "scientific")
dist = None
system = platform.system()

def platform_detection(module_type):
    if system == "Linux":
        dist = platform.linux_distribution()[0]
        if distro.id() in rh_derivatives:
            if module_type == "paths":
                from securitycentralplatform.base.paths import SecurityCentralBasePaths
                return SecurityCentralBasePaths

            if module_type == "constants":
                from securitycentralplatform.base.constants import SecurityCentralBaseConstants
                return SecurityCentralBaseConstants

            if module_type == "services":
                from securitycentralplatform.base.services import SecurityCentralBaseServices
                return SecurityCentralBaseServices

            if module_type == "tasks":
                from securitycentralplatform.base.tasks import SecurityCentralBaseTasks
                return SecurityCentralBaseTasks
