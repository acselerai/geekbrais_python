class Road:
    MASS_OF_ASPHALT_FOR_ONE_SQ_METER = 25
    THICHNESS = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass_of_asphalt(self):
        return self._length * \
               self._width * \
               self.MASS_OF_ASPHALT_FOR_ONE_SQ_METER * \
               self.THICHNESS // \
               1000
