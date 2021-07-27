import sys

class ClientGearmanUtils:

    @staticmethod
    def set_job_data_dict():

        #obtiene el argumento json
        if len(sys.argv) < 2:
            print('Favor de establecer el argumento JSON.')
            sys.exit(1)

        return sys.argv[1]
