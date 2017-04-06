import time
import sys

import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)

# stomp和activemq的通讯端口是61613， java是61616， java的客户端和Python的客户端可以互相 发布和订阅
conn = stomp.Connection([('ip',61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)

conn.subscribe(destination='/topic/moon', id=1, ack='auto')

conn.send(body='hello stomp ', destination='/topic/moon')

time.sleep(2)
conn.disconnect()
