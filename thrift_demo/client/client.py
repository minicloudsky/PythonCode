#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('__file__'), os.path.pardir)))

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from example.format_data import Client
from example.format_data import Data


__HOST = 'localhost'
__PORT = 9000


try:
    tsocket = TSocket.TSocket(__HOST, __PORT)
    transport = TTransport.TBufferedTransport(tsocket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Client(protocol)

    data = Data('hello,world!', 123)
    transport.open()
    print('client-requets')
    res = client.do_format(data)
    # print(client.do_format(data).text)
    print('server-answer', res)

    transport.close()
except Thrift.TException as ex:
    print(ex.message)