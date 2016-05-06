# coding: utf-8
__author__ = 'cshuo'


from .entity import Vm

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine, 
    Table, 
    Column, 
    Integer, 
    String, 
    MetaData, 
    ForeignKey
)


sqlURL = 'mysql://dra:cshuo@20.0.1.11:3306/machineDB'
engine = create_engine(sqlURL)

DBSession = sessionmaker(bind=engine)


def create_vm_table():
    metaData= MetaData()
    vmTable = Table('vm', metaData,
            Column('ids', String(40), primary_key=True),
            Column('name', String(32)),
            Column('vm_type', String(32)),
            )
    metaData.create_all(engine)


class DbUtil(object):
    def __init__(self):
        self.engine = engine

    def add_vm(self, ids, name, vm_type):
        session = DBSession()
        new_vm = Vm(ids=ids, name=name, vm_type=vm_type)
	try:
            session.add(new_vm)
            session.commit()
  	except:
	    session.close()
	    return False
        session.close()
        return True

    def rm_vm(self, vm_name):
        """
        return True for delete vm successfully, or return False
        """
        session = DBSession()
        try:
            vm_inst = session.query(Vm).filter(Vm.name==vm_name).one()
        except:
            session.close()
            return False
        session.delete(vm_inst)
        session.close()
        return True

    def query_vm(self, vm_ids):
        """
        return dict of vm info, None for None
        """
        session = DBSession()
        try:
            vm_inst = session.query(Vm).filter(Vm.ids==vm_ids).one()
        except:
            session.close()
            return None
        vm_info = {}
        vm_info['ids'] = vm_inst.ids
        vm_info['name'] = vm_inst.name
        vm_info['type'] = vm_inst.vm_type
        session.close()
        return vm_info

    def list_all(self):
	"""
	"""
	session = DBSession()
	try:
	    vms = session.query(Vm).all()
	except:
	    vms = []
	session.close()
	return vms


if __name__ == '__main__':
    create_vm_table()
    db = DbUtil()
    for i in db.list_all():
	print i.name
    # Vm.__table__.drop(engine)
    if db.add_vm('1212-1212-2121', 'test1', 'normal'):
	print "add ok"
    print db.query_vm('1212-1212-2121')
