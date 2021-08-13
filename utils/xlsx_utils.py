import xlsxwriter
import constants.constants as const


class XlsxUtils:

    @staticmethod
    def create_xlsx_file_from_list_errors(list_errors: list, path: str):
        workbook = xlsxwriter.Workbook(path)
        worksheet = workbook.add_worksheet('play button inconsistencies')
        row = 0
        col = 0

        header_cell_format = workbook.add_format(
            {'bold': True, 'bg_color': 'FCE93E', 'align': 'center', 'valign': 'vcenter', 'border': 1}
        )

        play_button_cell_format = workbook.add_format(
            {'bold': True, 'bg_color': 'FFE6B3', 'align': 'center', 'valign': 'vcenter', 'border': 3}
        )

        for header in const.HTML_LISTA_HEADERS_PUSH_BUTTON:
            worksheet.write(row, col, header, header_cell_format)
            col += 1

        col = 0
        row += 1

        len_char_movie_serie_name = 0
        len_char_validity = 0
        len_char_group_id = 0
        len_char_push_btn_visible = 0
        len_char_message_error = 0
        len_char_nodo = 0

        for play_button_data in list_errors:
            movie_serie_name = play_button_data['movie_serie_name']
            validity = play_button_data['validity']
            group_id = play_button_data['group_id']
            push_btn_visible = play_button_data['push_btn_visible']
            message_error = play_button_data['message_error']
            nodo = play_button_data['nodo']

            validity = 'SI' if validity == 1 else 'NO'
            push_btn_visible = 'ACTIVO' if push_btn_visible == 1 else 'INACTIVO'

            len_char_movie_serie_name = len(movie_serie_name) if len(movie_serie_name) > len_char_movie_serie_name \
                else len_char_movie_serie_name

            len_char_validity = len(validity) if len(validity) > len_char_validity else len_char_validity

            len_char_group_id = len(str(group_id)) if len(str(group_id)) > len_char_group_id else len_char_group_id

            len_char_push_btn_visible = len(push_btn_visible) if len(push_btn_visible) > len_char_push_btn_visible \
                else len_char_push_btn_visible

            len_char_message_error = len(message_error) if len(message_error) > len_char_message_error \
                else len_char_message_error

            len_char_nodo = len(nodo) if len(nodo) > len_char_nodo else len_char_nodo

            worksheet.write(row, col, nodo, play_button_cell_format)
            col += 1
            worksheet.write(row, col, group_id, play_button_cell_format)
            col += 1
            worksheet.write(row, col, movie_serie_name, play_button_cell_format)
            col += 1
            worksheet.write(row, col, push_btn_visible, play_button_cell_format)
            col += 1
            worksheet.write(row, col, validity, play_button_cell_format)
            col += 1
            worksheet.write(row, col, message_error, play_button_cell_format)
            col += 1

            col = 0
            row += 1

        # establece el ancho de cada columna del excel
        worksheet.set_column(0, 0, len_char_nodo)
        worksheet.set_column(1, 1, len_char_group_id)
        worksheet.set_column(2, 2, len_char_movie_serie_name)
        worksheet.set_column(3, 3, len_char_push_btn_visible)
        worksheet.set_column(4, 4, len_char_validity)
        worksheet.set_column(5, 5, len_char_message_error)

        workbook.close()
