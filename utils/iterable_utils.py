
class IterableUtils:

    @staticmethod
    def chunker(list, size):
        return (list[pos:pos + size] for pos in range(0, len(list), size))