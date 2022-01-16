class Result:
    """
    Returns a pair - Detection's phase and result
    Example
    (white phase, found site)
    (black phase, found site)
    (re phase, found re)
    (ml pahse, propobility)
    """
    def __init__(self, phase, param):
        self.phase = phase
        self.param = param
