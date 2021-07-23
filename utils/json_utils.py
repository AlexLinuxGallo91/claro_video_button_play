import random

class JsonUtils:

    @staticmethod
    def exist_errors_in_play_button_data(json_result: dict, debug_mode: bool = False):
        error_list = []

        for json_result in json_result['response']:
            for data_json_serie in json_result['result']:

                v = data_json_serie['date_info_expiration']

                print(v)

                json_data_expiration = []
                json_data_expiration['movie_serie_name'] = data_json_serie['date_info_expiration']['NOMBRE_INTERNO']
                json_data_expiration['expiration_date'] = data_json_serie['date_info_expiration']['FECHA_HASTA']
                json_data_expiration['validity'] = data_json_serie['date_info_expiration']['VIGENCIA']
                json_data_expiration['group_id'] = data_json_serie['date_info_expiration']['group_id']
                json_data_expiration['push_btn_visible'] = int(data_json_serie['playButton']['visible'])

                if debug_mode:
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

        return error_list
