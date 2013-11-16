class ActionFailedError(Exception):
    """
    Raised when a ROS action fails for some reason.
    """
    pass

class ControllerManagerError(Exception):
    '''
    Raised when the controller manager is unable to change controllers in the way we want.
    
    **Attributes:**
    
        **msg (str):** User-readable description of what happened.
    '''

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
