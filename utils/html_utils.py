from constants import constants as const
import html

class HtmlUtils:

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
            movie_serie_name = html.escape(push_button_data['movie_serie_name'])
            expiration_date = html.escape(push_button_data['expiration_date'])
            validity = html.escape(push_button_data['validity'])
            group_id = html.escape(push_button_data['group_id'])
            push_btn_visible = html.escape(push_button_data['push_btn_visible'])
            message_error = html.escape(push_button_data['message_error'])
            nodo = html.escape(push_button_data['nodo'])

            validity = 'SI' if validity == 1 else 'NO'
            push_btn_visible = 'ACTIVO' if push_btn_visible == 1 else 'INACTIVO'

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
