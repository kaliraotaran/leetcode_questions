class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        starting_pixel = image[sr][sc] # getting that certian pixel at the column by row
        self.dfs(image, sr, sc, color, starting_pixel) 

        return image

    def dfs(self, image, sr,sc, newColor, starting_pixel):

        if sr<0 or sr > len(image)-1 or sc<0 or sc> len(image[0])-1 or image[sr][sc] == newColor or image[sr][sc] != starting_pixel:
            return  # just cheking any edge cases
        image[sr][sc] = newColor # assigning the new color
        # since we assign the new color to the pixels that are 1 above, below,
        #  right and left of starting pixel, we perform the same operation on them as well
        self.dfs(image, sr+1, sc, newColor, starting_pixel) 
        self.dfs(image, sr-1, sc, newColor, starting_pixel)
        self.dfs(image, sr, sc+1, newColor, starting_pixel)
        self.dfs(image, sr, sc-1, newColor, starting_pixel)
