class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        moves = 0
        for i in range(len(seats)):
            if seats[i] > students[i]:
                while seats[i] > students[i]:
                    students[i]+=1
                    moves+=1
            elif seats[i] < students[i]:
                while seats[i] < students[i]:
                    students[i]-=1
                    moves+=1
            else:
                continue
        return moves