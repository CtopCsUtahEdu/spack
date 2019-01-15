# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import glob


class Tetgen(Package):
    """TetGen is a program and library that can be used to generate
       tetrahedral meshes for given 3D polyhedral domains. TetGen
       generates exact constrained Delaunay tetrahedralizations,
       boundary conforming Delaunay meshes, and Voronoi paritions.
    """

    homepage = "http://wias-berlin.de/software/tetgen/"

    version('1.5.0', '3b9fd9cdec121e52527b0308f7aad5c1', url='http://www.tetgen.org/1.5/src/tetgen1.5.0.tar.gz')
    version('1.4.3', 'd6a4bcdde2ac804f7ec66c29dcb63c18', url='http://www.tetgen.org/files/tetgen1.4.3.tar.gz')

    variant('debug', default=False, description='Builds the library in debug mode.')
    variant('except', default=False, description='Replaces asserts with exceptions for better C++ compatibility.')

    patch('tetgen-1.5.0-free.patch', when='@1.5.0')

    def patch(self):
        cflags = '-g -O0' if '+debug' in self.spec else '-g0 -O3'

        mff = FileFilter('makefile')
        mff.filter(r'^(C(XX)?FLAGS\s*=)(.*)$', r'\1 {0}'.format(cflags))

        if '+except' in self.spec:
            hff = FileFilter('tetgen.h')
            hff.filter(r'(\b)(throw)(\b)(.*);', r'\1assert_throw(false);')
            hff.filter(r'^(#define\s*tetgenH\s*)$', r'\1{0}'.format("""\n
#include <stdexcept>

inline void assert_throw(bool assertion)
{
  if(!assertion)
    throw std::runtime_error("Tetgen encountered a problem (assert failed)!");
}\n"""))

            sff = FileFilter(*(glob.glob('*.cxx')))
            sff.filter(r'(\b)(assert)(\b)', r'\1assert_throw\3')

    def install(self, spec, prefix):
        make('tetgen', 'tetlib')

        mkdirp(prefix.bin)
        install('tetgen', prefix.bin)

        mkdirp(prefix.include)
        install('tetgen.h', prefix.include)

        mkdirp(prefix.lib)
        install('libtet.a', prefix.lib)
