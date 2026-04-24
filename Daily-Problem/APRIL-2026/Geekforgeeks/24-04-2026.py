#Buildings with Sunlight

class Solution:
    def visibleBuildings(self, arr):
        n = len(arr)
        sunlight_vis_build =0
        last_max_building = arr[0]
        
        for build in arr :
            if build >= last_max_building :
                last_max_building = build
                sunlight_vis_build += 1
                
        return sunlight_vis_build
