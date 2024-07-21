if __name__ == '__main__':
    n = int(input())  # Read the number of scores
    arr = list(map(int, input().split()))  
    
    # Convert list to a set to remove duplicates
    unique_scores = set(arr)
    
    # Convert the set back to a sorted list
    sorted_scores = sorted(unique_scores)

    print(sorted_scores[-2])
    
    #NOTE 
    """
    map takes two arguments (data type, itrable object)
    input().split() the input() method acceptes the inputs as a string so we need to slise(default delimiter is space for split()) it at every space we find.
    here The result is a map object that is an iterator of integers.
    so to be use it needs to be changed to a list.
    To eliminate the duplicate elements we should change the list to a set
    and then change it back to a sorted list since we cannot access elements of a set using index.
    """
