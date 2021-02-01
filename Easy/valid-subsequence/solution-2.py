def isValidSubsequence(arr, seq):
    seqIdx = 0
    for value in arr:
        if len(seq) == seqIdx:
            break
        if seq[seqIdx] == value:
            seqIdx += 1
    return len(seq) == seqIdx

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
