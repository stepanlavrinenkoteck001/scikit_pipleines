class carTransmission:  #class with methods and attributes
    def __init__(self, current_gear, transmission_oil_age):
        self.current_gear = current_gear  # attributes
        self.transmission_oil_age = transmission_oil_age  #attributes

    def check_brake_on(self):
        # engage that brake is pressed here
        return self
    
    def engage_clutch(self):
        # engage clutch here
        return self
    
    def release_clutch(self):
        # release clutch here
        return self    

    def shift_forward(self, next_gear):  #method
        self = self.check_brake_on().engage_clutch()
        self.current_gear = next_gear
        return self
    
    def check_maintenance_needed(self):  #method
        if self.transmission_oil_age > 6000:
            print('Oil is 6000km old. Need to change it')
        return self


if __name__ == '__main__':
    # usage
    # initialize class
    mytransmission = carTransmission(1)
    mytransmission.shift_forward(3).check_maintenance_needed()