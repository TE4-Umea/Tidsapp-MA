class Util:
    def __init__(self):
        """
        Initialises Util function and loads dotenv files variables into os and is accessed by os.getenv().
        :rtype: void
        """
        from dotenv import load_dotenv
        import os

        load_dotenv()
        pass

    @staticmethod
    def get_env(variable):
        """
        This Looks up If the :arg: variable exists in the dotenv file.
        Returns the value of the dotenv variable from the file, if the variable doesnt exist, methods returns a -
        empty string.
        :rtype: str
        """
        pass
