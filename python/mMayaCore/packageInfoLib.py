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
## @package mMayaCore                   @brief [ PACKAGE   ] - Maya core functionalities.
## @dir     mMayaCore/python            @brief [ DIRECTORY ] - Python path.
## @dir     mMayaCore/python/mMayaCore  @brief [ DIRECTORY ] - Python package.
## @file    mMayaCore/packageInfoLib.py @brief [ FILE      ] - Package info module.
## @package mMayaCore.packageInfoLib    @brief [ MODULE    ] - Package info module.
## @package mMayaGUI                    @brief [ PACKAGE   ] - Maya GUI related modules.
## @dir     mMayaCore/python/mMayaGUI   @brief [ DIRECTORY ] - Python package.
## @package mMayaNode                   @brief [ PACKAGE   ] - Maya node related classes.
## @dir     mMayaCore/python/mMayaNode  @brief [ DIRECTORY ] - Python package.

#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
## [ str ] - Name of the package.
NAME                = 'mMayaCore'

## [ str ] - Version of the package.
VERSION             = '1.0.0'

## [ str ] - Description about the package.
DESCRIPTION         = 'Maya core functionalities.'

## [ list of str ] - Keywords to find this package.
KEYWORDS            = ['maya',
                       'core',
                       'namespace',
                       'optionVar',
                       'reference',
                       'menu',
                       'utilities',
                       'userSetup']

## [ list of str ] - Platforms which this package meant to be used on.
PLATFORMS           = ['Linux', 'Darwin', 'Windows']

## [ list of dict ] - Documentations about the package, keys of dict instances are: title, url.
DOCUMENTS           = []

## [ list of str ] - Applications which this package meant to be initialized for.
APPLICATIONS        = ['maya']

## [ list of str ] - Python versions supported by this package.
PYTHON_VERSIONS     = ['2', '3']

## [ bool ] - Whether this package is active (in use).
IS_ACTIVE           = True

## [ bool ] - Whether this package is external (third party).
IS_EXTERNAL         = False

## [ list of str ] - E-mail addresses of the developers.
DEVELOPERS          = ['safak@safakoner.com']

## [ list of str ] - Dependent packages.
DEPENDENT_PACKAGES  = ['mApplication',
                       'mCore',
                       'mDeveloper',
                       'mMecoPackage']

## [ list of str ] - Python packages contained by this package.
PYTHON_PACKAGES     = ['mMayaCore', 'mMayaGUI', 'mMayaNode']