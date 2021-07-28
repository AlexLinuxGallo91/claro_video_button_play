import random
from constants import constants as const


class JsonUtils:

    @staticmethod
    def verify_node_by_filter_and_node_id(node_id: int, filter_id: int):
        nodo_result = ''

        if node_id == const.CAT_NODE_ID_CATALAGO_PELICULAS:
            nodo_result = const.CAT_CATALAGO_PELICULAS

        elif node_id == const.CAT_NODE_ID_CATALAGO_SERIES:
            nodo_result = const.CAT_CATALAGO_SERIES

        elif node_id == const.CAT_NODE_ID_NOGGIN:
            nodo_result = const.CAT_NOGGIN

        elif node_id == const.CAT_NODE_ID_EDYE:
            nodo_result = const.CAT_EDYE

        elif node_id == const.CAT_NODE_ID_PICARDIA_NACIONAL:
            nodo_result = const.CAT_PICARDIA_NACIONAL

        elif filter_id == const.CAT_FILTER_ID_CATALAGO:
            nodo_result = const.CAT_CATALAGO

        elif filter_id == const.CAT_FILTER_ID_HBO_SERIES:
            nodo_result = const.CAT_HBO_SERIES

        elif filter_id == const.CAT_FILTER_ID_HBO_PELICULAS:
            nodo_result = const.CAT_HBO_PELICULAS

        elif filter_id == const.CAT_FILTER_ID_PARAMOUNT_SERIES:
            nodo_result = const.CAT_PARAMOUNT_SERIES

        elif filter_id == const.CAT_FILTER_ID_PARAMOUNT_PELICULAS:
            nodo_result = const.CAT_PARAMOUNT_PELICULAS

        elif filter_id == const.CAT_FILTER_ID_INDYCAR:
            nodo_result = const.CAT_INDYCAR

        elif filter_id == const.CAT_FILTER_ID_STINGRAY_QUELLO_TODOS_LOS_PROGRAMAS:
            nodo_result = const.CAT_STINGRAY_QUELLO_TODOS_LOS_PROGRAMAS

        elif filter_id == const.CAT_FILTER_ID_STINGRAY_KARAOKE_FIESTA_KARAOKE_1 or \
                filter_id == const.CAT_FILTER_ID_STINGRAY_KARAOKE_FIESTA_KARAOKE_2:
            nodo_result = const.CAT_STINGRAY_KARAOKE_FIESTA_KARAOKE

        elif filter_id == const.CAT_FILTER_ID_STINGRAY_KARAOKE_DISNEY:
            nodo_result = const.CAT_STINGRAY_KARAOKE_DISNEY

        elif filter_id == const.CAT_FILTER_ID_STINGRAY_KARAOKE_FESTIVOS:
            nodo_result = const.CAT_STINGRAY_KARAOKE_FESTIVOS

        elif filter_id == const.CAT_FILTER_ID_STINGRAY_KARAOKE_PORTUGUES:
            nodo_result = const.CAT_STINGRAY_KARAOKE_PORTUGUES

        elif filter_id == const.CAT_FILTER_ID_STINGRAY_KARAOKE_ROCK:
            nodo_result = const.CAT_STINGRAY_KARAOKE_ROCK

        elif filter_id == const.CAT_FILTER_ID_STINGRAY_KARAOKE_HIPHOP:
            nodo_result = const.CAT_STINGRAY_KARAOKE_HIPHOP

        elif filter_id == const.CAT_FILTER_ID_ATRES_PELÍCULAS:
            nodo_result = const.CAT_ATRES_PELÍCULAS

        elif filter_id == const.CAT_FILTER_ID_ATRES_PROGRAMAS:
            nodo_result = const.CAT_ATRES_PROGRAMAS

        elif filter_id == const.CAT_FILTER_ID_ATRES_SERIES:
            nodo_result = const.CAT_ATRES_SERIES

        return nodo_result

    @staticmethod
    def exist_errors_in_play_button_data(json_result: dict, debug_mode: bool = False):
        error_list = []

        if 'result' in json_result:

            print(type(json_result['result']))

            for data_json_serie in json_result['result']:

                json_data_expiration = {}
                json_data_expiration['movie_serie_name'] = data_json_serie['date_info_expiration']['NOMBRE_INTERNO']
                json_data_expiration['expiration_date'] = data_json_serie['date_info_expiration']['FECHA_HASTA']
                json_data_expiration['validity'] = data_json_serie['date_info_expiration']['VIGENCIA']
                json_data_expiration['group_id'] = data_json_serie['date_info_expiration']['group_id']
                json_data_expiration['push_btn_visible'] = int(data_json_serie['playButton']['visible'])
                json_data_expiration['nodo'] = data_json_serie['nodo']

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
