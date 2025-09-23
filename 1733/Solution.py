from typing import List

class Solution:
    def canCommunicate(self, languages1: List[int], languages2: List[int]) -> bool:
        if any(lang in languages2 for lang in languages1):
            return True
        return False

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        people_to_teach = set()
        lang_teachings = {}

        # Find all friends who can't communicate
        for person1,person2 in friendships:
            person1_languages = languages[person1-1]
            person2_languages = languages[person2-1]
            if not self.canCommunicate(person1_languages, person2_languages):
                people_to_teach.add(person1)
                people_to_teach.add(person2)

        # Try teaching each language
        for lang in range(1, n+1):
            for person in people_to_teach:
                if lang not in languages[person-1]:
                    lang_teachings.setdefault(lang, set()).add(person)

        # Get lang with min number of teachings
        if lang_teachings:
            min_teachings = min(lang_teachings.values(), key=len)
            min_len = len(min_teachings)
            return min_len
        else:
            return 0
        


class Tester(Solution):
    def __init__(self, solution):
        self.solution = solution

    def test1(self):
        n = 2
        languages = [[1],[2],[1,2]]
        friendships = [[1,2],[1,3],[2,3]]
        answer = self.solution.minimumTeachings(n, languages, friendships)
        assert answer == 1

    def test2(self):
        n = 3
        languages = [[2],[1,3],[1,2],[3]]
        friendships = [[1,4],[1,2],[3,4],[2,3]]
        answer = self.solution.minimumTeachings(n, languages, friendships)
        assert answer == 2
    
    def test3(self):
        #Input:
        # A(1,4) -> B(2)
        # B(2) -> C(3)
        # C(3) -> D(1,4)
        # D(1,4) -> E(4)
        # A(1,4) -> E(4)
        n = 4
        languages = [[1,4],[2],[3],[1,4],[4]]
        friendships = [[1,2],[2,3],[3,4],[4,5],[1,5]]
        answer = self.solution.minimumTeachings(n, languages, friendships)

        #Output: 2 - Teach B and C language 4
        assert answer == 2


    def test4(self):
        #Key:
        # A B C D E F G H I J  K  L  M  N  O  P  Q
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
        n = 2
        languages = [
            [2] #A
            ,[1] #B
            ,[2,1] #C
            ,[1] #D
            ,[1,2] #E
            ,[1] #F
            ,[2] #G
            ,[1] #H
            ,[1] #I
            ,[2] #J
            ,[1,2] #K
            ,[1,2] #L
            ,[1,2] #M
            ,[2,1] #N
            ,[1] #O
            ,[2] #P
            ,[1,2]] #Q
        friendships = [
            [15,16] #O(1) -> P(2)
            ,[4,13] #D(1) -> M(1,2)
            ,[3,16] #C(2,1) -> P(2)
            ,[5,14] #E(1,2) -> N(2,1)
            ,[1,7] #A(2) -> G(2)
            ,[2,11] #B(1) -> K(1,2)
            ,[3,15] #C(2,1) -> O(1)
            ,[4,16] #D(1) -> P(2)
            ,[7,9] #G(2) -> I(1)
            ,[6,13] #F(1) -> M(1,2)
            ,[6,16] #F(1) -> P(2)
            ,[4,10] #D(1) -> J(2)
            ,[6,9] #F(1) -> I(1)
            ,[5,6] #E(1,2) -> F(1)
            ,[7,12] #G(2) -> L(1,2)
            ,[6,12] #F(1) -> L(1,2)
            ,[3,7] #C(2,1) -> G(2)
            ,[4,7] #D(1) -> G(2)
            ,[8,10]] #H(1) -> J(2)
        # Output: 3 - Teach D, F, H language 2
        answer = self.solution.minimumTeachings(n, languages, friendships)
        assert answer == 3
    def test5(self):
        n = 11
        languages = [[3,11,5,10,1,4,9,7,2,8,6],[5,10,6,4,8,7],[6,11,7,9],[11,10,4],[6,2,8,4,3],[9,2,8,4,6,1,5,7,3,10],[7,5,11,1,3,4],[3,4,11,10,6,2,1,7,5,8,9],[8,6,10,2,3,1,11,5],[5,11,6,4,2]]
        friendships = [[7,9],[3,7],[3,4],[2,9],[1,8],[5,9],[8,9],[6,9],[3,5],[4,5],[4,9],[3,6],[1,7],[1,3],[2,8],[2,6],[5,7],[4,6],[5,8],[5,6],[2,7],[4,8],[3,8],[6,8],[2,5],[1,4],[1,9],[1,6],[6,7]]
        answer = self.solution.minimumTeachings(n, languages, friendships)
        assert answer == 0


if __name__ == "__main__":
    tester = Tester(Solution())
    tester.test1()
    tester.test2()
    tester.test3()
    tester.test4()
    tester.test5()
