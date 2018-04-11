from __future__ import absolute_import
from __future__ import print_function
import pyzmp
import time

from pyzmp_tutorials import server_node, client_node


def test_request_response():
    srv = None
    vrs = None
    try:

        # watcher = pyzmp.process_watcher()

        time.sleep(5)  # to give time to test user interruption

        srv = server_node.ServerNode("srv")
        srv.start()

        time.sleep(5)  # to give time to test user interruption

        vrs = client_node.ClientNode("vrs")
        vrs.start()

        question = pyzmp.discover("question")

        time.sleep(5)  # to give time to test user interruption

        response = pyzmp.discover("response")
        print(question.call())

        time.sleep(5)  # to give time to test user interruption

        print(response.call())

    except KeyboardInterrupt:
        print("Shutdown requested by user")

    finally:
        if srv:
            srv.shutdown()

        time.sleep(5)  # to give time to test user interruption

        if vrs:
            vrs.shutdown()

        time.sleep(5)  # to give time to test user interruption

        # if watcher:
        #     watcher.terminate()

# Just in case we run this directly
if __name__ == '__main__':
    import pytest
    pytest.main([
        '-s', __file__,
])
