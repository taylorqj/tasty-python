class Config():
    def __init__(self):
        ''' Base configurations for API. This is used for testing only '''
        ''' If this were to be deployed we would add environment variables '''
        ''' to dynamically switch host, port, etc '''
        self.debug = False
        self.db_uri = 'sqlite:///tastypython.db'
