class JsonUtils:

    @staticmethod
    def exist_errors_in_play_button_data(json_result: dict, debug_mode: bool = False):
        error_list = []

        for json_result in json_result['response']:
            for data_json_serie in json_result['result']:
                movie_serie_name = data_json_serie['date_info_expiration']['NOMBRE_INTERNO']
                expiration_date = data_json_serie['date_info_expiration']['FECHA_HASTA']
                validity = data_json_serie['date_info_expiration']['VIGENCIA']
                push_btn_visible = data_json_serie['playButton']['visible']

                print('movie_serie_name: {} - {}'.format(type(movie_serie_name), movie_serie_name))
                print('expiration_date: {} - {}'.format(type(expiration_date), expiration_date))
                print('validity: {} - {}'.format(type(validity), validity))
                print('push_btn_visible: {} - {}'.format(type(push_btn_visible), push_btn_visible))

                if debug_mode:
                    pass
