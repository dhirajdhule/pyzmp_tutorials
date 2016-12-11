from __future__ import absolute_import
from __future__ import print_function

import pyzmp
import time

from pyzmp_tutorials import server_node, client_node

# with pyzmp.process_watcher_cm():
with server_node.ServerNode("srv"):
    question = pyzmp.discover("question")
    print(question.call())
    time.sleep(2)  # to give time to test user interruption

    with client_node.ClientNode("vrs"):
        response = pyzmp.discover("response")

        time.sleep(2)  # to give time to test user interruption
        print(response.call())

