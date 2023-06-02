# 1396. Design Underground System
# https://leetcode.com/problems/design-underground-system/description/

class UndergroundSystem:

    def __init__(self):
        self.checkin_map = {}  # id -> [start station, time]
        self.route_stats_total = {}  # (start,stop) -> total
        self.route_stats_count = {}  # (start,stop) -> count

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        start_station = stationName
        start_time = t
        self.checkin_map[id] = [start_station, start_time]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        last_station = stationName
        end_time = t

        [start_station, start_time] = self.checkin_map[id]
        route = (start_station, last_station)
        if route not in self.route_stats_total:
            self.route_stats_total[route] = 0
        if route not in self.route_stats_count:
            self.route_stats_count[route] = 0

        self.route_stats_total[route] += (end_time - start_time)
        self.route_stats_count[route] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        route = (startStation, endStation)
        return self.route_stats_total[route] / self.route_stats_count[route]
