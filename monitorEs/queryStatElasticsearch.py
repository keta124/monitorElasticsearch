'''
Created on Sep 12, 2017

@author: CrazyDiamond
'''
from elasticsearch import Elasticsearch
import json
import time
def queryStatEs():
    try:
        time_now =int(time.time())*1000
        es = Elasticsearch([{'host': '192.168.142.101', 'port': 9200}])
        result = es.nodes.stats()
        node_id = result["nodes"].keys()
        if len(node_id)>1:
            for node in node_id:
                data ={}
                info = result["nodes"][node]
                data["host"] = info["host"]
                data["name"] =info["name"]
                # os
                os = info["os"]
                data["cpu_percent"]= os["cpu_percent"]
                data["mem_total"] = int(os["mem"]["total_in_bytes"]/1073741824)
                data["mem_free"] = os["mem"]["free_percent"]
                # jvm
                jvm = info["jvm"]["mem"]
                data["heap_used"] = jvm["heap_used_percent"]
                data["pool_young"] = int(100* jvm["pools"]["young"]["used_in_bytes"]/jvm["pools"]["young"]["max_in_bytes"])
                data["pool_survivor"] = int(100* jvm["pools"]["survivor"]["used_in_bytes"]/jvm["pools"]["survivor"]["max_in_bytes"])
                data["pool_old"] = int(100* jvm["pools"]["old"]["used_in_bytes"]/jvm["pools"]["old"]["max_in_bytes"])
                #
                data["timestamp"]=time_now
                # json
                print(json.dumps(data))
    except:
        pass

if __name__ == '__main__':
    queryStatEs()