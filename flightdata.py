class FlightData:
    def __init__(self, price, origin_city, origin_city2, origin_port, origin_port2, des_city, des_city2, des_port, des_port2,out_date, out_tm, out_date2, out_tm2, stp_ovrs=0):
        self.fprice = price
        self.forigin_city = origin_city
        self.forigin_city2 = origin_city2
        self.forigin_port = origin_port
        self.forigin_port2 = origin_port2
        self.fdes_city = des_city
        self.fdes_city2 = des_city2
        self.fdes_port = des_port
        self.fdes_port2 = des_port2
        self.fout_date = out_date
        self.fout_tm = out_tm
        self.fout_date2 = out_date2
        self.fout_tm2 = out_tm2
        self.fstp_ovrs = stp_ovrs
