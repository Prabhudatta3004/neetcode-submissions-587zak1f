class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position,speed),reverse = True)

        stack = []

        for pos,speed in sorted_cars:
            time = (target-pos)/speed

            if not stack:
                stack.append(time)
            if stack and stack[-1] < time:
                stack.append(time)
        return len(stack)