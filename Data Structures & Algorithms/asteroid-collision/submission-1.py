class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if abs(asteroid) > abs(stack[-1]):   # current asteroid destroys top of stack
                    stack.pop()
                elif abs(asteroid) == abs(stack[-1]): # both destroy each other
                    stack.pop()
                    alive = False
                else:  # stack top is bigger, asteroid destroyed
                    alive = False
            if alive:
                stack.append(asteroid)
        
        return stack
