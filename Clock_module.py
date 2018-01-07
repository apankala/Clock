class Time:
    """Blueprint for a clock"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
        self.__military = "True"
        self.__AM_PM = "AM"

    def set_clock(self, hour, minute, second, military, AM_PM):
        """Sets the clock, including desideing how to display the time, IE Military Time"""
        if military == "True" or military == "False":
            self.__military = military
        else:
            print("Set the military value to True or False")
            exit()
        if military == "True":
            if hour >= 0 and hour < 24:
                self.__hour = hour
            else:
                print("Set an hour value between 0 and 23")
                exit()
        else:   #military = False
            if hour >= 1 and hour <= 12:
                self.__hour = hour
            else:
                print("Set an hour value between 1 and 12")
                exit()
        if minute >= 0 and minute < 60:
            self.__minute = minute
        else:
            print("Set a minute value between 0 and 59")
            exit()
        if second >= 0 and second < 60:
            self.__second = second
        else:
            print("Set a second value between 0 and 59")
        if military == "False":
            if AM_PM == "AM" or AM_PM == "PM":
                self.__AM_PM = AM_PM
            else:
                print("Set an AM_PM value that is either AM or PM")
                exit()
        else:
            self.__AM_PM = "AM"
            
    def print_clock(self):
        """Prints the time acording to Military Time status"""
        if self.__military == "True":
            print("The time is,", self.__hour,":", self.__minute,".", self.__second)
        else:
            print("The time is,", self.__hour,":", self.__minute,".", self.__second, self.__AM_PM)

    def set_military(self, military):
        """converts clock to and from Military Time"""
        if military == "True" or military == "False":
            if military == "True" and self.__military == "True":
                exit()
            if military == "False" and self.__military == "False":
                exit()
            if military == "True":
                self.__military = "True"
                if self.__hour == 12 and self.__AM_PM == "AM":
                        self.__hour == 0
                elif AM_PM == "PM":
                        self.__hour = self.__hour + 12
            if military == "False":  
                self.__military = "False"
                if self.__hour > 12:
                    self.__AM_PM = "PM"
                    self.__hour = self.__hour - 12
                    exit()
                elif self.__hour == 12:
                    self.__AM_PM = "PM"
                    exit()
                elif self.__hour == 0:
                    self.__hour == 12
                    self.__AM_PM = "AM"
                    exit()
                else:
                    self.__AM_PM = "AM"  
        else:
            print("Set the military value to True or False")

    def tick(self):
        """"Increases the time by one second"""
        if self.__military == "False":
            self.__second = self.__second +1
            if self.__second == 60:
                self.__second = 0
                self.__minute = self.__minute + 1
                if self.__minute == 60:
                    self.__minute = 0
                    self.__hour = self.__hour + 1
                    if self.__hour >= 12:
                        self._hour = 1
                        if self.__AM_PM == "AM":
                            self.__AM_PM = "PM"
                        else:
                            self.__AM_PM = "AM"
                    else:
                        print(self.__hour,":",self.__minute,".",self.__second, self.__AM_PM)
                else:
                    print(self.__hour,":",self.__minute,".",self.__second, self.__AM_PM)
            else:
                print(self.__hour,":",self.__minute,".",self.__second, self.__AM_PM)
            print(self.__hour,":",self.__minute,".",self.__second, self.__AM_PM)
        else:   #Military = True
            self.__second = self.__second +1
            if self.__second == 60:
                self.__second = 0
                self.__minute = self.__minute + 1
                if self.__minute == 60:
                    self.__minute = 0
                    self.__hour = self.__hour + 1
                    if self.__hour == 24:
                        self.__hour = 0
                    else:
                        print(self.__hour,":", self.__minute,".",self.__second)
                else:
                    print(self.__hour,":", self.__minute,".",self.__second)
            else:
                print(self.__hour,":", self.__minute,".",self.__second)
            print(self.__hour,":", self.__minute,".",self.__second)
        
            
                            
                        
                    
 
        
