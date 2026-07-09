class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        stack = []

        for car in cars:
            time = (target-car[0]) / car[1]
            if not stack or stack[-1] < time:
                stack.append(time)


        return len(stack)
        