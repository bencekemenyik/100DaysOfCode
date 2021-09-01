from datetime import datetime, timedelta


class FlightData:
    def __init__(self, fly_to, stop_overs=0):
        self.fly_from = "LON"
        self.fly_to = fly_to
        now = datetime.now()
        tomorrow = (now + timedelta(1)).strftime("%d/%m/%Y")
        six_months_later = (now + timedelta(180)).strftime("%d/%m/%Y")
        self.date_from = tomorrow
        self.date_to = six_months_later
        self.flight_type = "round"
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.curr = "GBP"
        self.max_stopovers = stop_overs
        self.limit = 1
        self.price = 0
        self.departure_city_name = ""
        self.departure_airport_iata_code = ""
        self.arrival_city_name = ""
        self.arrival_airport_iata_code = ""
        self.outbound_date = ""
        self.inbound_date = ""
        self.via_city = ""

    def get_datas(self):
        return f"Only £{self.price} to fly from {self.departure_city_name}-{self.departure_airport_iata_code} to {self.arrival_city_name}-{self.arrival_airport_iata_code}, from {self.outbound_date} to {self.inbound_date}"

    def get_google_link(self):
        # flt=STN.SXF.2020-08-25*SXF.STN.2020-09-08
        return f"https://www.google.co.uk/flights?hl=en#flt={self.departure_airport_iata_code}.{self.arrival_airport_iata_code}.{self.outbound_date}*{self.arrival_airport_iata_code}.{self.departure_airport_iata_code}.{self.inbound_date}"
