import json
import os
from pathlib import Path

data_file = str(Path(__file__).parent.absolute()) + "/../jason/sample.json"

with open(data_file,'r') as json_file:
    data = json.load(json_file)

cmd = 'virt-install --name={0} --disk path={1} --graphics spice --vcpu={2} --ram={3} --location={4} --network bridge=virbr0'.format(data['components']['ISO'],data['components']['Disk_path'],data['components']['CPUs'],data['components']['Memory'],data['components']['Location'])


os.system(cmd)
