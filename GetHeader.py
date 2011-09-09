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

    def set_url(self, link):
        self._url = link

    def get_error(self, num):
        erros = {1:"Falha na conexão: O host conectado não respondeu!"}
        return erros[num]

    def __remove_http(self):
        """
        Remove o HTTP:// antes do link para evitar erros na conexão
        """
        links = self.get_url()
        new_link = []
        for link in links:
            if "http://" in link:
                new_link.append(link[7:])
        self.set_url(new_link)

    
    #TODO: Criar método para dividir o link depois do '/', se houver, para passar em 'end_url' no get_cabecalho
                

    def get_cabecalho(self, end_url="/"):
        """
        Este método efetua uma conexão com os links passados, afim de obter seu código http
        """

        links = self.get_url()
        result = {}

        for link in links:

            # Faz a conexão em cada um dos links para buscar o cabeçalho
            conn = httplib.HTTPConnection(link)
            try:
                conn.request("GET", end_url)
            except socket.error:
                return self.get_error(1)

            cod_http = conn.getresponse()

            result[link] = cod_http.status, cod_http.reason

        return result

