class ORMConstraint:

    @staticmethod
    def PRIMARYKEY():
        return f"PRIMARY KEY"

    @staticmethod
    def NOTNULL():
        return f"NOT NULL"

    @staticmethod
    def UNIQUE():
        return f"UNIQUE"
