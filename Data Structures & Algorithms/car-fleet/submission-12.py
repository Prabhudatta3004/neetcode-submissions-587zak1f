class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        fleets = []
        
        for pos,speed in cars:
            time = (target-pos)/speed

            if not fleets:
                fleets.append(time)
            
            if fleets and time>fleets[-1]:
                fleets.append(time)
        return len(fleets)
