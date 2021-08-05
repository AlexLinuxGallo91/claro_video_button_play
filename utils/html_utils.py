import re
import html
from constants import constants as const


class HtmlUtils:

    @staticmethod
    def generate_subject_email_by_list_play_button_errors(list_errors: list, region: str):
        subject = const.SUBJECT_MAIL_INCONSISTENCIA_PLAY_BUTTON
        list_nodes = []
        str_nodes = ''

        for node_data_json in list_nodes:
            if 'nodo' in node_data_json:
                list_nodes.append(node_data_json['nodo'])

        list_nodes = list(dict.fromkeys(list_nodes))
        str_nodes = ', '.join(list_nodes)

        return const.SUBJECT_MAIL_INCONSISTENCIA_PLAY_BUTTON.format(str_nodes, region)


    @staticmethod
    def replace_special_char_in_String_with_space(text):

        text_without_accents = ''

        for char in text:

            if char == 'á':
                text_without_accents = text_without_accents + 'a'
            elif char == 'Á':
                text_without_accents = text_without_accents + 'A'
            if char == 'é':
                text_without_accents = text_without_accents + 'e'
            elif char == 'É':
                text_without_accents = text_without_accents + 'E'
            if char == 'í':
                text_without_accents = text_without_accents + 'i'
            elif char == 'Í':
                text_without_accents = text_without_accents + 'I'
            if char == 'ó':
                text_without_accents = text_without_accents + 'o'
            elif char == 'Ó':
                text_without_accents = text_without_accents + 'O'
            if char == 'ú':
                text_without_accents = text_without_accents + 'u'
            elif char == 'Ú':
                text_without_accents = text_without_accents + 'U'
            elif char == 'ñ':
                text_without_accents = text_without_accents + 'n'
            elif char == 'Ñ':
                text_without_accents = text_without_accents + 'N'
            else:
                text_without_accents = text_without_accents + char

        return re.sub('[^a-zA-Z0-9 \n\.]', '', text_without_accents)

    @staticmethod
    def generate_table_headers_errors_push_buttons():
        header_html = ''

        for header in const.HTML_LISTA_HEADERS_PUSH_BUTTON:
            header_html += const.HTML_TABLE_TH.format(const.HTML_STYLE_HEADER, header)

        header_html = const.HTML_TABLE_TR.format('', header_html)

        return header_html

    @staticmethod
    def generate_html_table_errors_push_buttons(json_list_errors: list):
        html_body = ''
        html_headers = HtmlUtils.generate_table_headers_errors_push_buttons()

        for push_button_data in json_list_errors:
            movie_serie_name = push_button_data['movie_serie_name']
            expiration_date = push_button_data['expiration_date']
            validity = push_button_data['validity']
            group_id = push_button_data['group_id']
            push_btn_visible = push_button_data['push_btn_visible']
            message_error = push_button_data['message_error']
            nodo = push_button_data['nodo']

            validity = 'SI' if validity == 1 else 'NO'
            push_btn_visible = 'ACTIVO' if push_btn_visible == 1 else 'INACTIVO'

            # se revisa que el contenido del titulo de la serie o pelicula no contengan caracteres especiales
            movie_serie_name = HtmlUtils.replace_special_char_in_String_with_space(movie_serie_name)

            cadena_td_html = const.HTML_TABLE_TD.format(const.HTML_STYLE_BORDER_TABLE, nodo)
            cadena_td_html += const.HTML_TABLE_TD.format(const.HTML_STYLE_BORDER_TABLE, group_id)
            cadena_td_html += const.HTML_TABLE_TD.format(const.HTML_STYLE_BORDER_TABLE, movie_serie_name)
            cadena_td_html += const.HTML_TABLE_TD.format(const.HTML_STYLE_BORDER_TABLE, push_btn_visible)
            cadena_td_html += const.HTML_TABLE_TD.format(const.HTML_STYLE_BORDER_TABLE, validity)
            cadena_td_html += const.HTML_TABLE_TD.format(const.HTML_STYLE_BORDER_TABLE, message_error)
            cadena_td_html = const.HTML_TABLE_TR.format(const.HTML_STYLE_BORDER_TABLE, cadena_td_html)

            html_body += cadena_td_html

        html_body = html_headers + html_body
        html_body = const.HTML_TABLE.format(const.HTML_STYLE_BORDER_TABLE, html_body)
        html_body = const.HTML_MSG_NOTIFICACION_PLAY_BUTTON + html_body

        return html_body
