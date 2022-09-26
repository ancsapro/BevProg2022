# Raise an instance of the Exception class itself
 
raise Exception('Ummm... something is wrong')
 
 
 
# Raise an instance of the RuntimeError class
 
raise RuntimeError('Ummm... something is wrong')
 
 
 
# Raise a custom subclass of Exception that keeps the timestamp the exception was created
 
from datetime import datetime
 
 
 
class SuperError(Exception):
 
    def __init__(self, message):
 
        Exception.__init__(message)
 
        self.when = datetime.now()
 
 
 
 
 
raise SuperError('Ummm... something is wrong')