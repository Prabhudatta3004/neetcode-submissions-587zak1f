class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:

            alive = True

            while alive and ast<0 and stack and stack[-1] > 0:
                if abs(ast) < abs(stack[-1]):
                    alive = False
                elif abs(ast) > abs(stack[-1]):
                    stack.pop()
                else:
                    alive = False
                    stack.pop()
            if alive:
                stack.append(ast)
        return stack