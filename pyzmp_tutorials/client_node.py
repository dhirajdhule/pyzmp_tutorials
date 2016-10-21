from __future__ import absolute_import
import pyzmp


class ClientNode(pyzmp.Node):
    def __init__(self, name):
        super(ClientNode, self).__init__(name)
        self.the_response= 89
        self.provides(self.response)

    def response(self):
             return self.the_response

    def shutdown(self):
        super(ClientNode, self).shutdown()