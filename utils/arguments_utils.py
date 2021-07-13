import sys
import json
from constants import constants


class ArgumentsUtils:

    @staticmethod
    def verify_argument():
        """
        Metodo que se encarga de validar los argumentos entrantes en la ejecucion principal del Script

        :return:
        """
        if not ArgumentsUtils.has_json_argument():
            print('Favor de establecer el argumento de entrada con los datos necesarios.')
            sys.exit(1)
        elif not ArgumentsUtils.is_a_valid_json_argument():
            print('El argumento establecido no se encuentra en formato JSON, favor de establecerlo correctamente.')
            sys.exit(1)
        elif not ArgumentsUtils.has_necessary_keys_json():
            print('Favor de establecer correctamente el argumento JSON')
            sys.exit(1)

    @staticmethod
    def has_json_argument():
        """
        Metodo que se encarga de validar el numero de argumentos en el script, verifica que al menos tenga un argumento

        :return:
        """
        arguments = sys.argv[1:]
        return len(arguments) > 0

    @staticmethod
    def is_a_valid_json_argument():
        """
        Metodo que se encarga de validar si el argumento entrante este en formato JSON

        :return:
        """
        result = True

        try:
            ArgumentsUtils.convert_arg_to_dict()
        except ValueError:
            result = False

        return result

    @staticmethod
    def convert_arg_to_dict():
        """
        Metodo que se encarga de convertir el argumento entrante del script en un objeto diccionario

        :return:
        """
        return json.loads(sys.argv[1:2][0])

    @staticmethod
    def has_necessary_keys_json():
        """
        Metodo el cual se encarga de verificar que en el argumento JSON tenga los keys necesarios, de lo contrario
        nos devuelve un booleano False, detiendo la ejecucion del Script

        :return:
        """
        result = True

        list_necessary_keys = [
            constants.ARG_NODO, constants.ARG_PASSWORD, constants.ARG_NODE_ID, constants.ARG_USER,
            constants.ARG_REGION, constants.ARG_FILTER_ID
        ]

        for key, value in ArgumentsUtils.convert_arg_to_dict().items():
            if key not in list_necessary_keys:
                print('Opcion {} no reconocido. '.format(key), end="")
                result = False

        return result

