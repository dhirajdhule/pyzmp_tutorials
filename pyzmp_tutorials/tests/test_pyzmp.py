from __future__ import absolute_import
import pyzmp

from pyzmp_tutorials import server_node, client_node


srv = server_node.ServerNode("srv")
srv.start()


vrs = client_node.ClientNode("vrs")
vrs.start()

question = pyzmp.discover("question")
response = pyzmp.discover("response")
print question.call()
print response.call()



srv.shutdown()
vrs.shutdown()