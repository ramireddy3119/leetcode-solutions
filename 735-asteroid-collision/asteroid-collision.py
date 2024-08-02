class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                arr.append(asteroids[i])
            else:
                while arr and arr[-1] > 0 and arr[-1] < abs(asteroids[i]):
                    arr.pop()
                if arr and arr[-1] == abs(asteroids[i]):
                    arr.pop()
                elif len(arr)==0 or arr[-1] < 0:
                    arr.append(asteroids[i])
        return arr