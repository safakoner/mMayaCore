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
## @file    mMayaCore/nameSpaceLib.py @brief [ FILE ] - Operate on namespaces in Maya.
## @package mMayaCore.nameSpaceLib    @brief [ FILE ] - Operate on namespaces in Maya.


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
import mCore.nameSpaceLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ CLASS ] - Class to operate on namespaces in Maya.
class NameSpace(mCore.nameSpaceLib.NameSpace):
    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param nameSpace [ str | None | in  ] - NameSpace.
    #
    #  @exception N/A
    #
    #  @return None
    def __init__(self, nameSpace=None):

        mCore.nameSpaceLib.NameSpace.__dict__['__init__'](self, nameSpace)

