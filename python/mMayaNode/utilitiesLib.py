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
## @file    mMayaNode/utilitiesLib.py @brief [ FILE ] - Operate on Maya nodes.
## @package mMayaNode.utilitiesLib    @brief [ FILE ] - Operate on Maya nodes.


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
from   maya          import cmds
import maya.OpenMaya as openMaya


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Display type of selected nodes.
#
#  @code
#
#import mMayaNode.utilitiesLib
#
#mMayaNode.utilitiesLib.displayNodeType()
#
# # persp  >  transform
# # top    >  transform
# # front  >  transform
#
#  @endcode
#
#  @exception N/A
#
#  @return None - None.
def displayNodeType():

    selection = cmds.ls(sl=1)

    if not selection:
        openMaya.MGlobal.displayWarning('Please select node(s).')
        return

    openMaya.MGlobal.displayWarning('')

    for i in selection:
        openMaya.MGlobal.displayInfo('{}  >  {}'.format(i.ljust(40), cmds.nodeType(i)))

#
## @brief Delete all unknown nodes in the scene.
#
#  @code
#
#import mMayaNode.utilitiesLib
#
#mMayaNode.utilitiesLib.deleteUnknownNodes()
#
# # 23 unknown node(s) have been deleted.
#
#  @endcode
#
#  @exception N/A
#
#  @return None - None.
def deleteUnknownNodes():

    nodes = cmds.ls(type='unknown')

    if nodes:
        cmds.delete(nodes)
        openMaya.MGlobal.displayInfo('{} unknown node(s) have been deleted.'.format(len(nodes)))
        return

    openMaya.MGlobal.displayInfo('No unknown node has been found.')

#
## @brief Delete selected node on the main channel box.
#
#  @code
#
#import mMayaNode.utilitiesLib
#
#mMayaNode.utilitiesLib.deleteOnChannelBox()
#
#  @endcode
#
#  @param confirmDeletion [ bool | False | in  ] - Whether a confirm dialog appears for deletion.
#
#  @exception N/A
#
#  @return None - None.
def deleteOnChannelBox(confirmDeletion=False):

    node = cmds.ls(sl=1, tr=1, s=1)

    if not node:
        openMaya.MGlobal.displayWarning('Please select a node on the channel box.')
        return

    if not confirmDeletion:
        cmds.select(node, d=1)
        cmds.delete()
        cmds.select(node)
        return

    confirm = cmds.confirmDialog(t='Delete', m='Do you want to delete selected node?', ma='center', b=['Yes','No'], db='Yes')
    if confirm == 'Yes':
        cmds.select(node, d=1)
        cmds.delete()
        cmds.select(node)