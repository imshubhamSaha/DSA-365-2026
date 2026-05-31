#2126. Destroying Asteroids

from sortedcontainers import SortedSet
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n = len(asteroids)
        m = mass
        not_destroyed = SortedSet()

        for i in range(n) :
            ast = asteroids[i]
            if m >= ast :
                m += ast
            else :
                not_destroyed.add((ast, i)) 
        
        while not_destroyed:
            smallest_ast_mass, _ = not_destroyed.pop(0) 
            
            if m >= smallest_ast_mass:
                m += smallest_ast_mass
            else:
                return False  
        
        return True
----------------------------------


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n = len(asteroids)
        m = mass
        asteroids.sort()
        for i in range(n) :
            ast = asteroids[i]
            if m >= ast :
                m += ast
            else :
                return False 
                 
        return True
