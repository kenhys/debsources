# Copyright (C) 2015  The Debsources developers <qa-debsources@lists.alioth.debian.org>.
# See the AUTHORS file at the top-level directory of this distribution and at
# https://anonscm.debian.org/gitweb/?p=qa/debsources.git;a=blob;f=AUTHORS;hb=HEAD
#
# This file is part of Debsources. Debsources is free software: you can
# redistribute it and/or modify it under the terms of the GNU Affero General
# Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.  For more information
# see the COPYING file at the top-level directory of this distribution and at
# https://anonscm.debian.org/gitweb/?p=qa/debsources.git;a=blob;f=COPYING;hb=HEAD

from __future__ import absolute_import

from flask import Blueprint

# naming rule: bp_{dirname}
bp_patches = Blueprint('patches',
                       __name__,
                       template_folder='templates',
                       static_url_path='/static/patches',
                       static_folder='static')

from . import routes  # NOQA
