from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            l = len(image[i])
            for j in range(len(image[i]) - 1, -1, -1):
                if image[i][j] == 0:
                    image[i].append(1)
                else:
                    image[i].append(0)

            image[i] = image[i][l : len(image[i])]

        return image


solution = Solution()
actual = solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
print(actual)
print(actual == [[1, 0, 0], [0, 1, 0], [1, 1, 1]])
