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
## @file    mMayaNode/exceptionLib.py @brief [ FILE   ] - Exceptions.
## @package mMayaNode.exceptionLib    @brief [ MODULE ] - Exceptions.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
#
#
# NODE
#
## @brief [ EXCEPTION CLASS ] - Node doesn't exist.
class NodeDoesNotExist(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Node is not unique.
class NodeIsNotUnique(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Node type is not correct.
class NodeTypeIsNotCorrect(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - No valid node.
class NoValidNode(Exception):
    pass

#
#
#
# PLUG
#
## @brief [ EXCEPTION CLASS ] - Plug doesn't exist.
class PlugDoesNotExist(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Plug is not writable.
class PlugIsNotWritable(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Plug is locked.
class PlugIsLocked(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Plug has incoming connection.
class PlugHasIncomingConnection(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Invalid data type.
class InvalidDataType(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Plug has minimum value.
class PlugHasMinimumValue(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Plug has maximum value.
class PlugHasMaximumValue(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Invalid value.
class InvalidValue(Exception):
    pass

#
## @brief [ EXCEPTION CLASS ] - Invalid plug.
class InvalidPlug(Exception):
    pass
