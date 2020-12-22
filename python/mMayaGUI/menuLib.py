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
## @file    mMayaGUI/menuLib.py @brief [ FILE ] - Operate on menus in Maya.
## @package mMayaGUI.menuLib    @brief [ FILE ] - Operate on menus in Maya.


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
from   maya import cmds
from   maya import mel
from   maya import OpenMaya

import mApplication.applicationInfoAbs
import mApplication.parentApplicationLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Create a main menu.
#
#  @param path                 [ str  | None  | in ] - Path of the menu.
#  @param command              [ str  | None  | in ] - Command of the menu item.
#  @param icon                 [ str  | None  | in ] - Absolute path of an icon.
#  @param mainTearOff          [ bool | True  | in ] - Enable tear-off feature of the main menu.
#  @param mainAllowOptionBoxes [ bool | True  | in ] - Allow option boxes for main menu items.
#  @param mainDeleteFirst      [ bool | False | in ] - Delete main menu first.
#  @param tearOff              [ bool | True  | in ] - Enable tear-off feature of the sub menu(s).
#  @param allowOptionBoxes     [ bool | True  | in ] - Allow option boxes for sub menu items.
#  @param deleteFirst          [ bool | False | in ] - Delete sub menu(s) first.
#  @param addSeparator         [ bool | False | in ] - Add a separator before the menu item.
#
#  @exception N/A
#
#  @return str list - String list which contains the name of the created menus and menu item.
def createMenu(path,
               command,
               icon=None,
               mainTearOff=True,
               mainAllowOptionBoxes=True,
               mainDeleteFirst=False,
               tearOff=True,
               allowOptionBoxes=True,
               deleteFirst=False,
               addSeparator=False):

    PREFIX = 'Meco_'

    menuItemLabels = path.split('/')

    hierarchy     = ''
    menuItemNames = []

    for i in range(len(menuItemLabels)):

        if i == 0:
            hierarchy = '{}{}'.format(PREFIX, menuItemLabels[i])
        else:
            hierarchy += '_{}'.format(menuItemLabels[i])

        menuItemNames.append(hierarchy.replace(' ', ''))


    for i in range(len(menuItemLabels)):

        # Main menu attached to the main window
        if i == 0:

            if mainDeleteFirst:
                if cmds.menu(menuItemNames[i], q=1, ex=1):
                    cmds.deleteUI(menuItemNames[i])

            if not cmds.menu(menuItemNames[i], q=1, ex=1):
                mayaWindow = mel.eval('$temp1=$gMainWindow')
                cmds.menu(menuItemNames[i],
                          l=menuItemLabels[i],
                          p=mayaWindow,
                          to=mainTearOff,
                          aob=mainAllowOptionBoxes)

            continue


        if i > 0:

            if i == len(menuItemLabels)-1:
                # Menu item with command
                #sys.stdout.write('MENU ITEM')
                #sys.stdout.write(menuItemNames[i])

                if cmds.menuItem(menuItemNames[i], q=1, ex=1):
                    cmds.deleteUI(menuItemNames[i])

                if addSeparator:
                    cmds.menuItem(d=True, parent=menuItemNames[i-1])

                cmds.menuItem(menuItemNames[i],
                              l=menuItemLabels[i],
                              p=menuItemNames[i-1],
                              c=command,
                              i=icon)

            else:
                # Menu
                #sys.stdout.write(MENU')
                #sys.stdout.write(menuItemNames[i])

                if deleteFirst:
                    if cmds.menu(menuItemNames[i], q=1, ex=1):
                        cmds.deleteUI(menuItemNames[i])

                if not cmds.menu(menuItemNames[i], q=1, ex=1):
                    cmds.menuItem(menuItemNames[i], l=menuItemLabels[i], p=menuItemNames[i-1], aob=allowOptionBoxes, to=tearOff, sm=1)

    return menuItemNames


#
## @brief This function creates menus in Maya based on the application info classes available in PYTHONPATH.
#
#  Function do not initialize menus and returns `False` if Maya is not running in `OpenMaya.MGlobal.kInteractive` mode.
#
#  @see mApplication.applicationInfoAbs.ApplicationInfo
#
#  @exception N/A
#
#  @return bool - Result
def initializeMenus():

    if OpenMaya.MGlobal.mayaState() != OpenMaya.MGlobal.kInteractive:
        return False

    applicationList = mApplication.applicationInfoAbs.ApplicationInfo.list()
    if not applicationList:
        return False

    for app in applicationList:

        menuPath = app.fullMenuPath()
        if not menuPath:
            continue

        if not mApplication.parentApplicationLib.Application.kMaya in app.parentApplications() and not \
                mApplication.parentApplicationLib.Application.kAll in app.parentApplications():
            continue

        menuNames = createMenu(path=menuPath,
                               command=app.pythonCommand(),
                               icon=app.getIconFileAbsolutePath(),
                               addSeparator=app.menuSeparatorBefore(),
                               mainDeleteFirst=False)

    return True