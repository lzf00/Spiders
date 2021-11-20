# -*- codeing = utf-8 -*-
# @Time : 2021/1/4 15:48
# @Author : lzf
# @File : Marine_API.py
# @Software :PyCharm
from marinetrafficapi import MarineTrafficApi
api = MarineTrafficApi(api_key="81710166df546660b02cb7b295b7232cce80be61")

vessels = api.fleet_vessel_positions(min_latitude=38.20882,
                                     max_latitude=40.24562,
                                     min_longitude=-6.7749,
                                     max_longitude=-4.13721,
                                     time_span=10)

# list all possible params with:
MarineTrafficApi.print_params_for('fleet_vessel_positions')

for vessel in vessels.models:
    vessel.mmsi.value
    vessel.imo.value
    vessel.ship_id.value
    vessel.longitude.value
    vessel.latitude.value
    vessel.speed.value
    vessel.heading.value
    vessel.status.value
    vessel.course.value
    vessel.timestamp.value
    vessel.dsrc.value
    vessel.utc_seconds.value
    vessel.ship_name.value
    vessel.ship_type.value
    vessel.call_sign.value
    vessel.flag.value
    vessel.length.value
    vessel.width.value
    vessel.grt.value
    vessel.dwt.value
    vessel.draught.value
    vessel.year_built.value
    vessel.rot.value
    vessel.type_name.value
    vessel.ais_type_summary.value
    vessel.destination.value
    vessel.eta.value
    vessel.current_port.value
    vessel.last_port.value
    vessel.last_port_time.value
    vessel.current_port_id.value
    vessel.current_port_unlocode.value
    vessel.current_port_country.value
    vessel.last_port_id.value
    vessel.last_port_unlocode.value
    vessel.last_port_country.value
    vessel.next_port_id.value
    vessel.next_port_unlocode.value
    vessel.next_port_name.value
    vessel.next_port_country.value
    vessel.eta_calc.value
    vessel.eta_updated.value
    vessel.distance_to_go.value
    vessel.distance_travelled.value
    vessel.awg_speed.value
    vessel.max_speed.value

