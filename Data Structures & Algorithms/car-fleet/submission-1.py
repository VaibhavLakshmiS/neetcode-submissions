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
        time = 10-1/3 = 3

        stack 
        cars = [[7,1],[4,2],[1,2],[0,1]]
        time = 10-7/1 =3
        time = 6/2 =3
        time = 9/2 = 4.5 
        time = 10
        stack [3]
        """
        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse=True)
        print(cars)

        stack = []

        for position, speed in cars:
            time = (target - position) / speed

            if not stack: # when stack empty append
                stack.append(time)

            elif time > stack[-1]:
                stack.append(time)


        return len(stack)