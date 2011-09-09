# -*- coding: utf-8 -*-
#!/usr/bin/env python

import httplib
import socket

__author__ = 'Bruno Barbosa'


class ChecaCabecalho:
    def __init__(self, *args):
        self._url = args

    def get_url(self):
        return self._url

    def get_error(self, num):
        erros = {1:"Falha na conexão: O host conectado não respondeu!"}
        return erros[num]


    def get_cabecalho(self):

        links = self.get_url()

        for link in links:

            conn = httplib.HTTPConnection(link)
            try:
                conn.request("GET", "/")
            except socket.error:
                return self.get_error(1)

            result = conn.getresponse()

        return result.status, result.reason

