import prometheus_client as prom
from logging_class import logg
import sys
class prometheus:

    #Creating gauge parameters and initialising them to zero
    def initialise_gauge_obj(data):
        print(data)
        gauge_obj_list=list()
        print(gauge_obj_list)
        for status in data.keys():
            print(data.keys())
            # if status not in status_list:
            print(status)
            print("woah")
            gauge_obj_list.append(prom.Gauge(status,'testing'))
            # status_list.append(status)
            print(len(gauge_obj_list))
        for gauge_obj in gauge_obj_list:
            gauge_obj.set(0.0)
        # print(gauge_obj_list)
        return gauge_obj_list

    #Setting the value of gauge parameters
    def set_gauge_obj(data, gauge_obj_list):

        for gauge_obj in gauge_obj_list:
            desc= gauge_obj.describe()[0].name

            if desc in data.keys():
                gauge_obj.set(data[desc])

        return gauge_obj_list
