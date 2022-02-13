class TODOException(Exception):
    def __init__(self, func_name, additional_msg=""):
        super().__init__(f"{func_name} not implemented. Specs: {help(func_name)}.\n{additional_msg}")