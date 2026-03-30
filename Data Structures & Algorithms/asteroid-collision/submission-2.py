class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True
            while alive and asteroid<0 and stack and stack[-1]>0:
                if abs(stack[-1]) > abs(asteroid):
                    alive = False
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack