# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Xi Yu"
__date__ ="$2013-11-15 23:45:00$"
import sys

def eggDropping(egg,floor):
    if egg==floor:
        return floor
    if floor == 1 or floor== 0:
        return floor

    min = sys.maxint
    for x in range(1,floor):
        result = max(eggDropping(egg-1,x-1),eggDropping(egg,floor-x))
        if result < min:
            min = result
    return min+1


if __name__ == "__main__":
    print "How many eggs you want to waste?"
    egg = int(raw_input())
    print "How many floors you want to climb?"
    floor = int(raw_input())
    print eggDropping(egg,floor)
