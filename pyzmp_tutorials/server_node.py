from __future__ import absolute_import
import pyzmp


class ServerNode(pyzmp.Node):
    def __init__(self, name):
        super(ServerNode, self).__init__(name)
        self.the_answer= 42
        self.provides(self.question)

    def question(self):
             return self.the_answer

    def shutdown(self):
        super(ServerNode, self).shutdown()
