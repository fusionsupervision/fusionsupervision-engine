# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2019: FusionSupervision team, see AUTHORS.md file for contributors
#
# This file is part of FusionSupervision engine.
#
# FusionSupervision is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FusionSupervision is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with FusionSupervision engine.  If not, see <http://www.gnu.org/licenses/>.
#
#
# This file incorporates work covered by the following copyright and
# permission notice:
#
#  Copyright (C) 2015-2018: Alignak team, see AUTHORS.alignak.txt file for contributors
#
#  This file is part of Alignak.
#
#  Alignak is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Alignak is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Alignak.  If not, see <http://www.gnu.org/licenses/>.
#
#
#  This file incorporates work covered by the following copyright and
#  permission notice:
#
#   Copyright (C) 2009-2014:
#      Grégory Starck, g.starck@gmail.com
#
#   This file is part of Shinken.
#
#   Shinken is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Shinken is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with Shinken.  If not, see <http://www.gnu.org/licenses/>.

"""
This module provide PollerLink and PollerLinks classes used to manage link
between the modules Arbiter and Poller
"""

from fusionsupervision.objects.satellitelink import SatelliteLink, SatelliteLinks
from fusionsupervision.property import IntegerProp, StringProp, ListProp


class PollerLink(SatelliteLink):
    """
    Class to manage the link between Arbiter and Poller. With this, an arbiter
    can communicate with a poller
    """
    my_type = 'poller'
    # To_send: send or not to satellite conf
    properties = SatelliteLink.properties.copy()
    properties.update({
        'type':
            StringProp(default=u'poller', fill_brok=['full_status'], to_send=True),
        'poller_name':
            StringProp(default='', fill_brok=['full_status']),
        'port':
            IntegerProp(default=7771, fill_brok=['full_status'], to_send=True),
        # 'min_workers':
        #     IntegerProp(default=0, fill_brok=['full_status'], to_send=True),
        # 'max_workers':
        #     IntegerProp(default=30, fill_brok=['full_status'], to_send=True),
        # 'processes_by_worker':
        #     IntegerProp(default=256, fill_brok=['full_status'], to_send=True),
        # 'worker_polling_interval':
        #     IntegerProp(default=1, to_send=True),
        'poller_tags':
            ListProp(default=['None'], to_send=True),
    })


class PollerLinks(SatelliteLinks):
    """
    Class to manage list of PollerLink.
    PollerLinks is used to regroup all links between the Arbiter and different Pollers
    """
    name_property = "poller_name"
    inner_class = PollerLink
