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
## @file    userSetup.py @brief [ FILE ] - User setup file for Autodesk Maya.
## @package userSetup    @brief [ FILE ] - User setup file for Autodesk Maya.


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
from    maya import utils

import  mMayaGUI.menuLib


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
#
## @brief Function initializes the menus for tools in Autodesk Maya.
#
#  @exception N/A
#
#  @return None - None.
def main():

    # Create menus for the available tools in Autodesk Maya
    utils.executeDeferred('mMayaGUI.menuLib.initializeMenus()')


if __name__ == '__main__':

    main()

