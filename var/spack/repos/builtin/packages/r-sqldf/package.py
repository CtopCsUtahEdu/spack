# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RSqldf(RPackage):
    """The sqldf() function is typically passed a single argument
    which is an SQL select statement where the table names are
    ordinary R data frame names. sqldf() transparently sets up a
    database, imports the data frames into that database, performs the
    SQL select or other statement and returns the result using a
    heuristic to determine which class to assign to each column of the
    returned data frame. The sqldf() or read.csv.sql() functions can
    also be used to read filtered files into R even if the original
    files are larger than R itself can handle. 'RSQLite', 'RH2',
    'RMySQL' and 'RPostgreSQL' backends are supported."""

    homepage = "https://cran.r-project.org/package=sqldf"
    url      = "https://cran.r-project.org/src/contrib/sqldf_0.4-11.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/sqldf"

    version('0.4-11', '85def6fe2418569370c24e53522d2c2d')

    depends_on('r-gsubfn', type=('build', 'run'))
    depends_on('r-proto', type=('build', 'run'))
    depends_on('r-rsqlite', type=('build', 'run'))
    depends_on('r-dbi', type=('build', 'run'))
    depends_on('r-chron', type=('build', 'run'))
