import sys
import json
from constants import constants


class ArgumentsUtils:

    @staticmethod
    def verify_argument():

        if not ArgumentsUtils.has_json_argument():
            sys.exit(1)
        elif not ArgumentsUtils.is_a_valid_json_argument():
            sys.exit(1)

        json_arg = ArgumentsUtils.convert_arg_to_dict()

        ArgumentsUtils.has_necessary_keys_json(json_arg)

    @staticmethod
    def has_json_argument():
        arguments = sys.argv[1:]
        return len(arguments) > 0

    @staticmethod
    def is_a_valid_json_argument():
        result = True
        json_argument = sys.argv[1:2][0]

        try:
            json.loads(json_argument)
        except ValueError:
            result = False

        return result

    @staticmethod
    def convert_arg_to_dict():
        return json.load(sys.argv[1:2][0])

    @staticmethod
    def has_necessary_keys_json(json: dict):
        list_necessary_keys = [
            constants.ARG_NODO, constants.ARG_PASSWORD, constants.ARG_NODE_ID, constants.ARG_CORREO,
            constants.ARG_REGION, constants.ARG_FILTER_ID
        ]

        for key, value in json.items():
            print("{}-{}".format(key, value))

