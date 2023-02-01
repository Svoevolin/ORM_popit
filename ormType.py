class ORMType:

    @staticmethod
    def INT():
        return f"INT"

    @staticmethod
    def SERIAL():
        return f"SERIAL"

    @staticmethod
    def CHAR():
        return f"CHAR"

    @staticmethod
    def VARCHAR(length):
        if isinstance(length, int):
            return f"VARCHAR({length})"
        else: raise Exception

    @staticmethod
    def NUMERIC(precision, scale):
        if isinstance(precision, int) and isinstance(scale, int):
            return f"NUMERIC({precision},{scale})"
        else: raise Exception

