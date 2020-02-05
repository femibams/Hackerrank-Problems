# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    final_result = []
    for query in queries:
        count=0
        for i in range(len(strings)):
            if query == strings[i]:
                count+=1
        final_result.append(count)
    return final_result
