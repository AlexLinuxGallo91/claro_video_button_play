from os.path import isdir
from os import mkdir, remove


class FileUtils:

    @staticmethod
    def create_folder(path_folder_to_create: str):
        result = True

        try:
            mkdir(path_folder_to_create)
        except OSError as e:
            result = False

        return result

    @staticmethod
    def check_folder_reports_exists(path_folder: str):
        folder_exists_result = True

        if not FileUtils.dir_exists(path_folder):
            folder_exists_result = FileUtils.create_folder(path_folder)

        return folder_exists_result

    @staticmethod
    def dir_exists(path_folder: str):
        return isdir(path_folder)

    @staticmethod
    def remove_file_from_path_str(path_file: str):
        remove(path_file)
