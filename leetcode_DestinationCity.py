class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        endCities = []
        for i in range(len(paths)):
            endCities.append(paths[i][1])
        for i in range(len(paths)):
            if(paths[i][0] in endCities):
                endCities.remove(paths[i][0])
        return endCities.pop()
            