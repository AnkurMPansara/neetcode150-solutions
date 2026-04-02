class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = 0
        stack = []
        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        stack.sort(key=lambda x: x[0])
        prev_time_taken = 0
        while stack:
            car_pos, car_speed = stack.pop()
            time_taken = (target-car_pos)/car_speed
            if time_taken > prev_time_taken:
                car_fleets += 1
                prev_time_taken = time_taken
        return car_fleets