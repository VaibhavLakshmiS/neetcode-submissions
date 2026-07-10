class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        tar = 10
        position =[1,4]
        speed=[3,2]

        cars = [[1,3],[4,2]]
        after sort 
        cars[[4,2][1,3]]

        time = 10-4/2 = 3
        time = 10-1/3 = 7

        stack 
        

        """
        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse=True)
        print(cars)

        stack = []

        for position, speed in cars:
            time = (target - position) / speed

            if not stack:
                stack.append(time)

            elif time > stack[-1]:
                stack.append(time)


        return len(stack)