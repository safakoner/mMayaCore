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
## @file    mMayaCore/optionVarLib.py @brief [ FILE ] - Operate on optionVar in Maya.
## @package mMayaCore.optionVarLib    @brief [ FILE ] - Operate on optionVar in Maya.


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
from maya import cmds


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ CLASS ] - Class provides functionalities to operate on optionVar in Maya.
#
#  @code
#import sys
#import mMayaCore.optionVarLib
#
#optionVar = mMayaCore.optionVarLib.OptionVar('lastSelectedObject')
#
#sys.stdout.write(optionVar.exists())
# # False
#
#optionVar.setValue('cube1')
#
#sys.stdout.write(optionVar.exists())
# # True
#
#sys.stdout.write(optionVar.value())
# # cube1
#
#sys.stdout.write(optionVar.name())
# # lastSelectedObject
#
#  @endcode
class OptionVar(object):
    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param name [ str | None | in ] - Name of the variable.
    #
    #  @exception N/A
    #
    #  @return None
    def __init__(self, name):

        ## [ str ] - Name of the optionVar.
        self._name = name

    #
    # ------------------------------------------------------------------------------------------------
    # PROPERTY METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Name of the option variable.
    #
    #  @exception N/A
    #
    #  @return str  - Name of the option variable.
    #  @return None - If name is not set.
    def name(self):

        return self._name

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Check whether the option variable exists.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def exists(self):

        return cmds.optionVar(exists=self._name)

    #
    ## @brief Remove the option variable.
    #
    #  @exception N/A
    #
    #  @return None
    def remove(self):

        cmds.optionVar(remove=self._name)

    #
    ## @brief Set value of the option variable.
    #
    #  @param value [ int, float, str | None | in ] - Value to be set.
    #
    #  @exception N/A
    #
    #  @return None
    def setValue(self, value):

        if isinstance(value, str):
            cmds.optionVar(sv=(self._name, value))

        if isinstance(value, int):
            cmds.optionVar(iv=(self._name, value))

        if isinstance(value, float):
            cmds.optionVar(fv=(self._name, value))

    #
    ## @brief Get the value of the option variable.
    #
    #  @exception N/A
    #
    #  @return int, float, str - Value of the option variable.
    #  @return None            - If option variable doesn't exist.
    def value(self):

        if not self.exists():
            return None

        return cmds.optionVar(q=self._name)

    #
    # ------------------------------------------------------------------------------------------------
    # STATIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief List all option variables.
    #
    #  @exception N/A
    #
    #  @return str list - Option variables
    @staticmethod
    def list():

        return cmds.optionVar(list=True)
