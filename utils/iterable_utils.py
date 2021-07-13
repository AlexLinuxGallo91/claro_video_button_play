
class IterableUtils:

    @staticmethod
    def chunker(list, size):
        """
        Metodo el cual permite dividir en trozos/partes un array en grupos de cierto numero de elementos

        :param list:
        :param size:
        :return:
        """
        return (list[pos:pos + size] for pos in range(0, len(list), size))