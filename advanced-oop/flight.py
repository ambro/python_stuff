from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        segments = [self.segments[0].departure]
        for segment in self.segments:
            segments.append(segment.destination)
        return ' -> '.join(segments)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, value):
        # self.segments[0].departure = value
        dest = self.segments[0].destination
        self.segments[0] = Segment(value, dest)


flight = Flight([Segment('GLA', 'LHR'), Segment('LHR', 'CAN'), Segment('CAN', 'BOS')])
print(flight.departure_point)
flight.departure_point = 'EDI'
print(flight.departure_point)
print(flight)