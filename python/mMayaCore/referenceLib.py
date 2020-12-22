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
## @file    mMayaCore/referenceLib.py @brief [ FILE ] - Operate on referenced nodes in Maya.
## @package mMayaCore.referenceLib    @brief [ FILE ] - Operate on referenced nodes in Maya.


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
import  os

from   maya import cmds
from   maya import OpenMaya

import mMayaCore.nameSpaceLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ CLASS ] - Class to operate on referenced nodes in Maya.
#
#  @code
#import sys
#import mMayaCore.referenceLib
#
#reference = mMayaCore.referenceLib.Reference(node='someMayaFile:pCube1')
#
#sys.stdout.write(reference.exists())
# # True
#
#sys.stdout.write(reference.setNode(node='someMayaFile:pCube1'))
# # True
#
#sys.stdout.write(reference.node())
# # someMayaFile:pCube1
#
#sys.stdout.write(reference.reload())
# # True
#
#sys.stdout.write(reference.duplicate())
# # /pathToFile/someMayaFile.ma{2}
#
#sys.stdout.write(reference.remove())
# # True
#
#sys.stdout.write(mMayaCore.referenceLib.Reference.create(mayaFile='/pathToFile/someMayaFile.ma'))
# # /pathToFile/someMayaFile.ma
#
#mMayaCore.referenceLib.Reference.duplicateSelected()
#
#mMayaCore.referenceLib.Reference.removeSelected()
#
#mMayaCore.referenceLib.Reference.reloadSelected()
#
#sys.stdout.write(mMayaCore.referenceLib.Reference.isNodeReferenced(node='someMayaFile:pCube1'))
# # True
#
#sys.stdout.write(mMayaCore.referenceLib.Reference.isNodeReferenced(node='persp'))
# # False
#
#  @endcode
#
class Reference(mMayaCore.nameSpaceLib.NameSpace):
    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param node [ str | None | in  ] - Name of the node.
    #
    #  @exception N/A
    #
    #  @return None.
    def __init__(self, node=None):

        mMayaCore.nameSpaceLib.NameSpace.__dict__['__init__'](self, nameSpace=node)

        ## [ str ] - Name of the referenced node.
        self._node = None

        if node:
            self.setNode(node=node)

    #
    # ------------------------------------------------------------------------------------------------
    # PROPERTY METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Node.
    #
    #  @exception N/A
    #
    #  @return str  - Name of the node.
    #  @return None - If node is not set.
    def node(self):

        return self._node

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Check whether the node exists.
    #
    #  Checks whether node is None.
    #  Checks whether the node exists.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def exists(self):

        if not self._node:
            return False

        return cmds.objExists(self._node)

    #
    ## @brief Set node.
    #
    #  Returns False if the node is not a referenced node.
    #
    #  @param node [ str | None | in  ] - Name of the node.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def setNode(self, node):

        if not Reference.isNodeReferenced(node=node):
            return False

        self._node = node
        self.setNameSpace(nameSpace=node)

        return True

    #
    ## @brief Reload the referenced node.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def reload(self):

        if not self.exists():
            return False

        referencedNode = cmds.referenceQuery(self._node, referenceNode=1)
        cmds.file(lr=referencedNode)

        return True

    #
    ## @brief Duplicate given referenced node.
    #
    #  @exception N/A
    #
    #  @return str  - Resolved name of the referenced file.
    #  @return None - If not is not set.
    def duplicate(self):

        if not self.exists():
            return None

        filePath  = cmds.referenceQuery(self._node, f=1, withoutCopyNumber=1)
        nameSpace = os.path.basename(filePath).split('.')[0]

        referenced = Reference.create(filePath, nameSpace)

        return referenced

    #
    ## @brief Remove the given referenced node.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def remove(self):

        if not self.exists():
            return False

        referencedFile = cmds.referenceQuery(self._node, f=1)
        cmds.file(referencedFile, rr=1)

        self._node = None

        return True

    #
    # ------------------------------------------------------------------------------------------------
    # STATIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Check whether the given node is a referenced node.
    #
    #  @param node [ str | None | in  ] - Name of the node.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    @staticmethod
    def isNodeReferenced(node):

        if not cmds.objExists(node):
            return False

        if not cmds.referenceQuery(node, inr=1):
            return False

        return True

    #
    ## @brief Create reference from given file.
    #
    #  If nameSpace argument left out, file name will be the name space for the referenced nodes.
    #
    #  @param mayaFile  [ str | None | in  ] - Name of the file, Maya ASCII or Maya Binary.
    #  @param nameSpace [ str | None | in  ] - Namespace of the referenced nodes.
    #
    #  @exception N/A
    #
    #  @return str  - Resolved name of the referenced file.
    #  @return None - If maya file doesn't exist.
    @staticmethod
    def create(mayaFile, nameSpace=None):

        if not os.path.isfile(mayaFile):
            return None

        fileType = 'mayaAscii'
        if os.path.splitext(mayaFile)[1][1:] == 'mb':
            fileType = 'mayaBinary'

        if not nameSpace:
            nameSpace = os.path.basename(mayaFile).split('.')[0]

        return cmds.file(mayaFile, r=1, type=fileType, namespace=nameSpace, options='v=0;cmds=17')

    #
    ## @brief Duplicate selected referenced nodes.
    #
    #  @exception N/A
    #
    #  @return None
    @staticmethod
    def duplicateSelected():

        selection = cmds.ls(sl=1)
        if not selection:
            OpenMaya.MGlobal.displayWarning('Please select referenced node(s).')
            return

        _reference = Reference()

        for i in selection:
            if not _reference.setNode(node=i):
                OpenMaya.MGlobal.displayWarning('Node is not referenced: {}'.format(i))
            else:
                _reference.duplicate()

    #
    ## @brief Remove selected referenced nodes.
    #
    #  Method actually removes the referenced file which will be retrieved from the referenced nodes.
    #
    #  @exception N/A
    #
    #  @return None
    @staticmethod
    def removeSelected():

        selection = cmds.ls(sl=1)
        if not selection:
            OpenMaya.MGlobal.displayWarning('Please select referenced node(s).')
            return

        confirm = cmds.confirmDialog(title='Remove Referenced Nodes',
                                     message='Do you want to remove selected referenced node(s)?',
                                     button=['Yes','No'],
                                     defaultButton='No',
                                     cancelButton='No',#
                                     dismissString='No' )

        if confirm == 'Yes':

            _reference = Reference()

            for i in selection:
                if not _reference.setNode(node=i):
                    OpenMaya.MGlobal.displayWarning('Referenced node could not be set: {}'.format(i))
                else:
                    _reference.remove()

    #
    ## @brief Reload selected referenced nodes.
    #
    #  Method actually reloads the referenced file which will be retrieved from the referenced nodes.
    #
    #  @exception N/A
    #
    #  @return None
    @staticmethod
    def reloadSelected():

        selection = cmds.ls(sl=1)
        if not selection:
            OpenMaya.MGlobal.displayWarning('Please select referenced node(s).')
            return False

        _reference = Reference()

        for i in selection:
            if not _reference.setNode(node=i):
                OpenMaya.MGlobal.displayWarning('Referenced node could not be set: {}'.format(i))
            else:
                _reference.reload()
