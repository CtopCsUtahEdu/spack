# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyVirtualenvwrapper(PythonPackage):
    """virtualenvwrapper is a set of extensions to Ian Bicking's
    virtualenv tool. The extensions include wrappers for creating and
    deleting virtual environments and otherwise managing your development
    workflow, making it easier to work on more than one project at a time
    without introducing conflicts in their dependencies."""

    homepage = "https://bitbucket.org/virtualenvwrapper/virtualenvwrapper.git"
    url      = "https://pypi.io/packages/source/v/virtualenvwrapper/virtualenvwrapper-4.8.2.tar.gz"

    version('4.8.2', '8e3af0e0d42733f15c5e36df484a952e')

    depends_on('python@2.6:')
    depends_on('py-virtualenv', type=('build', 'run'))
    depends_on('py-virtualenv-clone', type=('build', 'run'))
    depends_on('py-stevedore', type=('build', 'run'))
    # not just build-time, requires pkg_resources
    depends_on('py-setuptools', type=('build', 'run'))
