# openstack_alter
> These are some modification maded to openstack to adapt the utility of DRA


- **..nova/api/openstack/compute/servers.py** <br>
add vm type store to mysql db

- **..nova/api/openstack/compute/schemas/servers.py** <br>
add request paramenter: app_type to openstack api

- **..nova/api/openstack/compute/db** <br>
db operation using sqlalchemy

- **..nova/scheduler/hades_scheduler.py** <br>
custom our own vms' creation scheduler
