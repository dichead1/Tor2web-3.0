import imp
import os
import sys
import types

from twisted.application import internet
from twisted.application import service
from twisted.plugin import IPlugin
from twisted.python import usage
from twisted.python import reflect
from zope.interface import implements

from tor2web.run import service_https, service_http

class Options(usage.Options):
    pass

class ServiceMaker(object):
    implements(service.IServiceMaker, IPlugin)
    tapname = "tor2web"
    description = "Tor2web 3.0 Cataclysm Edition"
    options = Options

    def makeService(self, options):
        srv = service.MultiService()
        s_https = service_https
        s_https.setServiceParent(srv)

        s_http = service_https
        s_http.setServiceParent(srv)

        return srv

serviceMaker = ServiceMaker()
