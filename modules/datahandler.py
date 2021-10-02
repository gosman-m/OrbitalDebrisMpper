import ephem


class Object:
    def __init__(self, index, name, line1, line2):
        self.index = index
        self.name = name
        self.line1 = line1
        self.line2 = line2


class DataHandler:
    def __init__(self):
        self.debris_list = []
        self.load_data()

    def load_data(self):
        active = False
        index = 1
        name = ''
        line1 = ''
        line2 = ''

        with open('data/debris-tle.txt') as data_file:
            for data_line in data_file:
                if active != True:
                    name = data_line
                    active = True
                elif data_line[0] == '1':
                    line1 = data_line
                elif data_line[0] == '2':
                    line2 = data_line
                    
                    self.debris_list.append(Object(index, name, line1, line2))

                    active = False
                    index += 1
                    name = ''
                    line1 = ''
                    line2 = ''

    def get_location(self, sat, date = []):
        location = ephem.readtle(sat.name, sat.line1, sat.line2)

        if date != []:
            year = date[0]
            m = date[1]
            day = date[2]
            hour = date[3]
            minute = date[4]
            sec = date[5]

            location.compute(year, m, day, hour, minute, sec)
        
        else:
            location.compute()

        return location.sublat/ephem.degree, location.sublong/ephem.degree

    def convert(self, lat, lon):
        x = (1280/2*lat)/180
        x = 1280 - x
        y = (720/2*lat)/90
        y = 720 - y

        return x, y
