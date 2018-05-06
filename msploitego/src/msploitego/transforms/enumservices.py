from pprint import pprint

from common.msploitdb import MetasploitXML
from common.MaltegoTransform import *
import sys

__author__ = 'Marc Gurreri'
__copyright__ = 'Copyright 2018, msploitego Project'
__credits__ = []
__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'Marc Gurreri'
__email__ = 'me@me.com'
__status__ = 'Development'

def dotransform(args):
    entitytags = ["info", "name", "port", "proto", "state"]
    mt = MaltegoTransform()
    # mt.debug(pprint(args))
    mt.parseArguments(args)
    fn = mt.getVar("fromfile")
    ip = mt.getVar("address")
    for service in MetasploitXML(fn).gethost(ip).services:
        hostservice = mt.addEntity("maltego.Service", "{}/{}".format(service.name,service.port))
        hostservice.setValue = "{}/{}".format(service.name,service.port)
        hostservice.addAdditionalFields("fromfile", "Source File", True, fn)
        for etag in entitytags:
            if etag in service.getTags():
                hostservice.addAdditionalFields(etag, etag, True, service.getVal(etag))
    mt.returnOutput()
    mt.addUIMessage("completed!")

dotransform(sys.argv)
# args = ['enumservices.py',
#  '10.10.10.59',
#  'ipv4-address=10.10.10.59#ipaddress.internal=false#fromfile=/root/proj/oscp-maltego/oscp/src/oscp/transforms/common/msploitdb20180501.xml#name=TALLY#address=10.10.10.59#servicecount=48#osname=Windows 2016#state=alive']
# dotransform(args)
