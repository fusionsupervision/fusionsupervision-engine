#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016: Alignak team, see AUTHORS.txt file for contributors
#
# This file is part of Alignak.
#
# Alignak is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Alignak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Alignak.  If not, see <http://www.gnu.org/licenses/>.
#
#
# This file incorporates work covered by the following copyright and
# permission notice:
#
#  Copyright (C) 2009-2014:
#     Jean Gabes, naparuba@gmail.com
#     Grégory Starck, g.starck@gmail.com
#     Sebastien Coavoux, s.coavoux@free.fr

#  This file is part of Shinken.
#
#  Shinken is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Shinken is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Shinken.  If not, see <http://www.gnu.org/licenses/>.

#
# This file is used to test reading and processing of config files
#

from alignak_test import *


class TestMultipleNotHG(AlignakTest):

    def setUp(self):
        self.setup_with_file(['etc/alignak_multiple_not_hostgroups.cfg'])

    def test_dummy(self):

        for s in self.sched.services:
            print "SERVICES", s.get_full_name()
        
        svc = self.sched.services.find_srv_by_name_and_hostname("hst_in_BIG", "THE_SERVICE")
        self.assertIsNot(svc, None)

        svc = self.sched.services.find_srv_by_name_and_hostname("hst_in_IncludeLast", "THE_SERVICE")
        self.assertIsNot(svc, None)

        svc = self.sched.services.find_srv_by_name_and_hostname("hst_in_NotOne", "THE_SERVICE")
        self.assertIs(None, svc)

        svc = self.sched.services.find_srv_by_name_and_hostname("hst_in_NotTwo", "THE_SERVICE")
        self.assertIs(None, svc)


if __name__ == '__main__':
    unittest.main()