# openstack_alter
> These are some modification maded to openstack to adapt the utility of DRA


- ..nova/api/openstack/compute/servers.py
> add vm type store to mysql db

- ..nova/api/openstack/compute/db
> db operation using sqlalchemy

- ..nova/scheduler/hades_scheduler.py
> custom our own vms' creation scheduler
