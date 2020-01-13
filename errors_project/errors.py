class RuntimeErrorWithCode(TypeError):
    """
    Exception with error code
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


#err = RuntimeErrorWithCode("Something bad happened.", 500)
#print(err.__doc__)
#raise RuntimeErrorWithCode("Something bad happened.", 500)
