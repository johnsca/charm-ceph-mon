# Copyright 2020 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from mock import patch

import charms_ceph.utils


class CharmCephUtilsTestCase(unittest.TestCase):

    @patch('charmhelpers.contrib.openstack.utils.lsb_release')
    def test_get_admin_caps(self, mock_lsb_release):
        mock_lsb_release.return_value = {'DISTRIB_CODENAME': 'focal'}
        gac = charms_ceph.utils.get_admin_caps
        self.assertIn('mgr', gac('distro'))
        self.assertIn('mgr', gac('cloud:bionic-train'))
        self.assertNotIn('mgr', gac('cloud:bionic-stein'))
        mock_lsb_release.return_value = {'DISTRIB_CODENAME': 'xenial'}
        self.assertNotIn('mgr', gac('distro'))
