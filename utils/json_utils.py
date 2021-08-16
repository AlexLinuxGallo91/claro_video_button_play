import random
from constants import constants as const


class JsonUtils:

    @staticmethod
    def is_valid_type_format(json_data_dict:dict):
        result = True

        format_obtained = json_data_dict['date_info_expiration']['FORMATO']
        if not format_obtained in const.LIST_FILTER_ACTIVE_TYPES:
            result = False

        return result

    @staticmethod
    def exist_errors_in_play_button_data(json_result: dict, debug_mode: bool = False):
        error_list = []

        # debug
        nodo = ''

        if 'result' in json_result:

            if len(json_result['result']) < 1:
                print('no se encontraron id_groups en este nodo.')

            for data_json_serie in json_result['result']:

                # verifica que si este dentro de los tipos de formatos validos, en caso contrario, se omite la serie/
                # pelicula
                if not JsonUtils.is_valid_type_format(data_json_serie) and not debug_mode:
                    continue

                json_data_expiration = {}
                json_data_expiration['movie_serie_name'] = data_json_serie['date_info_expiration']['NOMBRE_INTERNO']
                json_data_expiration['expiration_date'] = data_json_serie['date_info_expiration']['FECHA_HASTA']
                json_data_expiration['validity'] = data_json_serie['date_info_expiration']['VIGENCIA']
                json_data_expiration['group_id'] = data_json_serie['date_info_expiration']['group_id']
                json_data_expiration['push_btn_visible'] = int(data_json_serie['playButton']['visible'])
                json_data_expiration['nodo'] = data_json_serie['nodo']
                nodo = json_data_expiration['nodo']

                if debug_mode and len(error_list) <= 5:
                    list_random_values = [0, 1]
                    dummy_bool_visibility = random.choice(list_random_values)
                    dummy_bool_validity = random.choice(list_random_values)

                    json_data_expiration['validity'] = dummy_bool_validity
                    json_data_expiration['push_btn_visible'] = dummy_bool_visibility

                    if dummy_bool_validity < 1:
                        json_data_expiration['expiration_date'] = '13-05-2000'

                # filtros de validaciones
                if json_data_expiration['push_btn_visible'] == 0 and json_data_expiration['validity'] == 1:
                    json_data_expiration['message_error'] = 'Deberia tener boton activo'
                    error_list.append(json_data_expiration)

                elif json_data_expiration['push_btn_visible'] == 1 and json_data_expiration['validity'] == 0:
                    json_data_expiration['message_error'] = 'El contenido no deberia estar publicado / Deberia ' \
                                                            'tener boton inactivo'
                    error_list.append(json_data_expiration)

                elif json_data_expiration['push_btn_visible'] == 0 and json_data_expiration['validity'] == 0:
                    json_data_expiration['message_error'] = 'El contenido no deberia estar publicado'
                    error_list.append(json_data_expiration)

            # debug
            print('numero de elementos encontrados en el nodo {}: {}'.format(nodo, len(json_result['result'])))

        return error_list
