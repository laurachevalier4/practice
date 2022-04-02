"""
Problem: Given a string that represents items as asterisks (*) 
and compartment walls as pipes (|), a start index, and an 
end index, return the number of items in a closed compartment.

This solution assumes that asterisks are the only non-pipe character that
can appear. If there were other non-items in between compartment walls,
we would have to keep track of the item count rather than just open/close indices.

dict[start_index] = close_index  # serves as key to the next "open" pipe. 
If dict[start_index] is -1, we have no more closing pipes.
"""
def map_open_to_close(s):
    """Given a string of asterisks and pipes, returns the mapping of open pipe
	to close pipe, or start pipe to -1 if there is no close pipe."""
    mapping = {}
    start_index = 0
    string_length = len(s)
    while start_index < string_length:
        # If we found an open pipe, find the close pipe.
        if s[start_index] == "|":
            end_index = start_index+1
            # Loop until the end of the string or until we find the close pipe.
            while end_index < string_length and s[end_index] != "|":
		end_index += 1
            # Either we reached the end of the string or found a match.    
            if end_index >= string_length:
		mapping[start_index] = -1
                break
	    else:
                mapping[start_index] = end_index
		start_index = end_index
        # If this character isn't a pipe, check the next one.        
        else:
            start_index += 1
    return mapping
    
def solution(s, start, end):
    mapping = map_open_to_close(s)
    item_count = 0
    # We could make this more efficient by using an ordered dictionary
    # and only accessing the indices that we know are open pipes, since
    # we already know where these are from our map_open_to_close function.
    while start < end:
        # If there's an open pipe at this index, find the close (if
	# there is one) and calculate number of items.
	if mapping.get(start, None):
            close = mapping[start]
	    # Either no more close pipes, or we reached the end of
	    # our index range.
            if close == -1 or close >= end:
                break
	    # Otherwise, count number of items and reset start.
            else:
                item_count += (close-1 - start)
                start = close  # Start at the close pipe.
        # If no open pipe here, check the next index.
	else:
            start += 1
    return item_count
    
string = '|**|*|*'   
print(solution(string, 0, 5))
print(solution(string, 0, 6))
print(solution(string, 1, 7))
