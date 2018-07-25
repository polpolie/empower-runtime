#!/usr/bin/env python3
#
# Copyright (c) 2016 Roberto Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

"""Launch the EmPOWER runtime."""

from empower.main import main


if __name__ == "__main__":

    # Default modules
    ARGVS = ['restserver.restserver',
             'lvnfp.lvnfpserver',
             'lvapp.lvappserver',
             'vbsp.vbspserver',
             'ibnp.ibnpserver',

             'lvapp.lvap_stats.lvap_stats',
             'lvapp.bin_counter.bin_counter',
             'lvapp.txp_bin_counter.txp_bin_counter',
             'lvapp.trq_bin_counter.trq_bin_counter',
             'lvapp.cqm.ucqm',
             'lvapp.cqm.ncqm',
             'lvapp.wifi_stats.wifi_stats',
             'lvapp.rssi.rssi',
             'lvapp.summary.summary',
             'lvapp.igmp_report.igmp_report',

             'vbsp.rrc_measurements.rrc_measurements',
             'vbsp.mac_reports.mac_reports',

             'lvnfp.lvnf_get.lvnf_get',
             'lvnfp.lvnf_set.lvnf_set',
             'lvnfp.lvnf_stats.lvnf_stats']

    main(ARGVS)
