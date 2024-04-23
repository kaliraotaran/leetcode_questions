

'''
https://leetcode.com/problems/simplify-path/submissions/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        direcOrFile = []
        path = path.split('/')

        for elem in path:
            if direcOrFile and elem =='..':
                direcOrFile.pop()
            elif elem not in ['.', '..', '']:
                direcOrFile.append(elem)
        return '/'+'/'.join(direcOrFile)