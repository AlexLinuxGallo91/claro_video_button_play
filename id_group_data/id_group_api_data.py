#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################################################################################
# Nombre: Gerardo Treviño Montelongo
# Clase: idgrupAPI.py
# Fecha: 11/06/2021
# Correo: gerardo.trevino@triara.com
# Version 1.00
# Sistema: Linux
#
#
# Referencias:
#   https://j2logo.com/python/tutorial/tipo-range-python/
#
#############################################################################################################################

# import requests module.
import requests
import json
import concurrent.futures as futures

# Variables
numPartes = 200

class IdGroupApi:

    # -------------------------
    # Funcion principal.
    # -------------------------
    def main(self, node_id, filter_id):
        # Datos iniciales de l aurl
        idgrups = self.jsonidgrup(self.getParams(node_id, filter_id))
        # dict_json = json.dumps(idgrups, indent = 4)
        # print(dict_json)
        return idgrups


    # ----------------------------------------------
    # Parametros para enviar a la url del igrups ---
    # ----------------------------------------------
    def getParams(self, node_id, filter_id):
        # Parametros para el request.
        params = {
            # ----------------------------
            'filter_id' : filter_id, # 9482 31069
            'node_id' : node_id, #None
            # ----------------------------
            'quantity' : '1',
            'from' : '0',
            'order_way' : 'ASC',
            'order_id' : '0',
            'level_id' : 'GPS',
            'region' : 'mexico',
            'device_id' : 'web',
            'device_category' : 'web',
            'device_model' : 'web',
            'device_type' : 'web',
            'device_so' : 'Chrome',
            'format' : 'json',
            'device_manufacturer' : 'generic',
            'authpn' : 'webclient',
            'authpt' : 'tfg1h3j4k6fd7',
            'api_version' : 'v5.93',
            'HKS' : '3ogr7na3ck7ousjtkjieo5i6n2'
        }
        return params


    # -----------------------------------
    #  Ejecuta el get para el idgrups ---
    # -----------------------------------
    def jsonidgrup(self, jsonParams):
        #  URL para consultar.
        url = 'https://mfwkweb-api.clarovideo.net/services/content/list'
        # Consultar get request.
        response = requests.get(url, params=jsonParams)
        # Se extrae el total de registros del response.
        responseJson = response.json()
        totalIdgrups = responseJson['response']['total']
        # Consultar get request.
        jsonParams['quantity'] = totalIdgrups

        # Valida el numero de veces que va a ejecutar la consulta
        if (totalIdgrups <= numPartes):
            # Si el total de idgrups es menos a 200 se corre una vez.
            idgrups = self.getIdgrups(url, jsonParams, 0)
            idgrupsKeys = list(dict.fromkeys(idgrups))
        else:
            # Si los registros son mayores a 200 se realiza un bucle
            # Se genera el listado con los rangos inicia en 0 e incrementa en 200 hasta totalIdgrups
            rankNums = sorted(list(range(1, totalIdgrups, numPartes)))
            idgrups = self.proccesGetIdgrups(url, jsonParams, rankNums)
            idgrupsKeys = list(dict.fromkeys(idgrups))

        # Generar el json final
        data = {
            'idgrups' : idgrupsKeys,
            'totalAPI' : totalIdgrups,
            'totalScript' : len(idgrupsKeys),
            # 'duplicados' : len([x for x in idgrups if idgrups.count(x) >= 2])
        }
        return data


    # -------------------------------------------------
    # Se ejecuta el prceso para extraer los idgrups ---
    # -------------------------------------------------
    def getIdgrups(self, url, jsonParams, fromPart):
        jsonParams['from'] = (fromPart - 1)
        # print(jsonParams)
        response = requests.get(url, params=jsonParams)
        # Validar que el codigo de respuesta sea 200.
        if (response.ok):
            idgrups = []
            # Se extrae el idgrups del response.
            responseJson = response.json()
            idgroups = responseJson['response']['groups']
            if (idgroups != None):
                # print(responseJson)
                for idgroup in idgroups:
                    # JSON con los registros necesarios.
                    idgrups.append(int(idgroup['id']))

        return idgrups


    # ---------------------------------------------------------------
    # Paralelización de la revision de las imagenes con las URL`s ---
    # ---------------------------------------------------------------
    def proccesGetIdgrups(self, url, jsonParams, rankNums):
        idgrups = []
        jsonParams['quantity'] = numPartes
        # Podemos usar una declaración with para asegurarnos de que los hilos se limpien rápidamente.
        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            # Inicie las operaciones de carga y marque cada futuro con su URL
            for num in rankNums:
                future = executor.submit(self.getIdgrups, url, jsonParams, num)
                # Json con el resultado
                idgrups = idgrups + future.result()
            # Regresamos el arraglo con todos los idgrups
            return idgrups



# -------------------------
# Inicia proceso.
# -------------------------
if __name__ == '__main__':
    id_group_api = IdGroupApi()
    id_group_api.main()
