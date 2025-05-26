
"""
Created on Wed Aug 14 16:02:00 2024

@author: timofeevam
"""

def merge_intervals(intervals):
    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])
    print (intervals)
    
    # Initialize the list to hold merged intervals
    merged = []
    
    # Iterate through each interval in the sorted list
    for interval in intervals:
        # If merged is empty or the last interval in merged does not overlap with the current interval
        if len(merged) == 0 or merged[-1][1] < interval[0]:
            # Add the current interval to merged as a new non-overlapping interval
            merged.append(interval)
        else:
            # Merge the current interval with the last interval in merged
            # Update the end time of the last interval in merged to the maximum end time of the overlapping intervals
             merged[-1][1] = max(merged[-1][1], interval[1])
        print(merged)    
    
    # Return the list of merged intervals
    return merged


result = merge_intervals([[3,4], [1,5], [16, 18], [20, 24]])
print(result)