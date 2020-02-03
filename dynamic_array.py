def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    result = []
    seq_list=[]
    for a in range(n):
        seq_list.append([])
    for i in range(len(queries)):
        query = queries[i]
        
        if query[0] == 1:
            seq = ((query[1] ^ last_answer)%n)
            seq_list[seq].append(query[2])
        elif query[0] == 2:
            seq = ((query[1] ^ last_answer)%n)
            size = len(seq_list[seq])
            
            num = query[2]%size

            last_answer = seq_list[seq][num]
            result.append(last_answer)
    return result
