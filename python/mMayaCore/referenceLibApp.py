#
# Copyright 2020 Safak Oner.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file    mMayaCore/referenceLibApp.py @brief [ FILE ] - Application info module.
## @package mMayaCore.referenceLibApp    @brief [ FILE ] - Application info module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import mApplication.applicationInfoAbs
import mApplication.parentApplicationLib

import mDeveloper.developers.sonerLib


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
#
## @brief [ APPLICATION INFO CLASS ] - Class provides application information for the application.
class DuplicateSelectedNodes(mApplication.applicationInfoAbs.ApplicationInfo):
    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self):

        ## [ str ] - Name of the application.
        self._name                  = 'Duplicate Selected Nodes'

        ## [ int ] - Major version.
        self._versionMajor          = 1

        ## [ int ] - Minor version.
        self._versionMinor          = 0

        ## [ int ] - Fix version.
        self._versionFix            = 0


        ## [ str ] - Description about the application.
        self._description           = 'Duplicate selected nodes.'

        ## [ str ] - Name of the icon file.
        self._iconFileName          = 'reference.png'

        ## [ list of enum ] - Parent applications which this application designed to work in @see mApplication.parentApplicationLib.Application
        self._parentApplications    = [mApplication.parentApplicationLib.Application.kMaya]

        ## [ list of str ] - Keywords.
        self._keywords              = ['node', 'reference', 'duplicate']

        ## [ list of dict ] - Documentations, keys of dict instances are: title, url.
        self._documents             = [{'title':'Web Site...', 'url':'https://www.safakoner.com'}]

        ## [ str ] - Python command to run the application.
        self._pythonCommand         = 'import mMayaCore.referenceLib;mMayaCore.referenceLib.Reference.duplicateSelected()'

        ## [ str ] - Menu path. Use / as separator to give a complete path.
        self._menuPath              = 'Reference'

        ## [ list of dict ] - Developers, keys of dict instances are userName, name, email, web.
        self._developers            = [mDeveloper.developers.sonerLib.INFO]

        mApplication.applicationInfoAbs.ApplicationInfo.__dict__['__init__'](self)

#
## @brief [ APPLICATION INFO CLASS ] - Class provides application information for the application.
class RemoveSelectedNodes(mApplication.applicationInfoAbs.ApplicationInfo):
    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self):

        ## [ str ] - Name of the application.
        self._name                  = 'Remove Selected Nodes'

        ## [ int ] - Major version.
        self._versionMajor          = 1

        ## [ int ] - Minor version.
        self._versionMinor          = 0

        ## [ int ] - Fix version.
        self._versionFix            = 0


        ## [ str ] - Description about the application.
        self._description           = 'Remove selected nodes.'

        ## [ str ] - Name of the icon file.
        self._iconFileName          = 'reference.png'

        ## [ list of enum ] - Parent applications which this application designed to work in @see mApplication.parentApplicationLib.Application
        self._parentApplications    = [mApplication.parentApplicationLib.Application.kMaya]

        ## [ list of str ] - Keywords.
        self._keywords              = ['node', 'reference', 'remove']

        ## [ list of dict ] - Documentations, keys of dict instances are: title, url.
        self._documents             = [{'title':'Web Site...', 'url':'https://www.safakoner.com'}]

        ## [ str ] - Python command to run the application.
        self._pythonCommand         = 'import mMayaCore.referenceLib;mMayaCore.referenceLib.Reference.removeSelected()'

        ## [ str ] - Menu path. Use / as separator to give a complete path.
        self._menuPath              = 'Reference'

        ## [ list of dict ] - Developers, keys of dict instances are userName, name, email, web.
        self._developers            = [mDeveloper.developers.sonerLib.INFO]

        mApplication.applicationInfoAbs.ApplicationInfo.__dict__['__init__'](self)

#
## @brief [ APPLICATION INFO CLASS ] - Class provides application information for the application.
class ReloadSelectedNodes(mApplication.applicationInfoAbs.ApplicationInfo):
    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self):

        ## [ str ] - Name of the application.
        self._name                  = 'Reload Selected Nodes'

        ## [ int ] - Major version.
        self._versionMajor          = 1

        ## [ int ] - Minor version.
        self._versionMinor          = 0

        ## [ int ] - Fix version.
        self._versionFix            = 0


        ## [ str ] - Description about the application.
        self._description           = 'Reload selected nodes.'

        ## [ str ] - Name of the icon file.
        self._iconFileName          = 'reference.png'

        ## [ list of enum ] - Parent applications which this application designed to work in @see mApplication.parentApplicationLib.Application
        self._parentApplications    = [mApplication.parentApplicationLib.Application.kMaya]

        ## [ list of str ] - Keywords.
        self._keywords              = ['node', 'reference', 'reload']

        ## [ list of dict ] - Documentations, keys of dict instances are: title, url.
        self._documents             = [{'title':'Web Site...', 'url':'https://www.safakoner.com'}]

        ## [ str ] - Python command to run the application.
        self._pythonCommand         = 'import mMayaCore.referenceLib;mMayaCore.referenceLib.Reference.reloadSelected()'

        ## [ str ] - Menu path. Use / as separator to give a complete path.
        self._menuPath              = 'Reference'

        ## [ list of dict ] - Developers, keys of dict instances are userName, name, email, web.
        self._developers            = [mDeveloper.developers.sonerLib.INFO]

        mApplication.applicationInfoAbs.ApplicationInfo.__dict__['__init__'](self)
