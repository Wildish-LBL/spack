##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Libffi(AutotoolsPackage):
    """The libffi library provides a portable, high level programming
    interface to various calling conventions. This allows a programmer
    to call any function specified by a call interface description at
    run time."""
    homepage = "https://sourceware.org/libffi/"

    version('3.2.1', '83b89587607e3eb65c70d361f13bab43',
            url="https://www.mirrorservice.org/sites/sourceware.org/pub/libffi/libffi-3.2.1.tar.gz")
    variant("shared", default=True, description="Enable shared libs")

    def configure_args(self):
        args = []
        if "+shared" in self.spec:
            args.append("--enable-shared")
        else:
            args.append("--disable-shared")
        
        if self.spec.satisfies("%intel") and self.spec.satisfies("os=cnl5"):
            args.append("--host=x86_64")

        return args
    # version('3.1', 'f5898b29bbfd70502831a212d9249d10',url =
    # "ftp://sourceware.org/pub/libffi/libffi-3.1.tar.gz") # Has a bug
    # $(lib64) instead of ${lib64} in libffi.pc
