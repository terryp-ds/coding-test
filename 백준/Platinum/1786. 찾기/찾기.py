def compute_lps_array(pattern, len_pattern):
    lps = [0] * len_pattern
    length = 0
    i = 1

    while i < len_pattern:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length-1]

            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(pattern, text):
    len_pattern = len(pattern)
    len_text = len(text)

    lps = compute_lps_array(pattern, len_pattern)

    i,j = 0,0

    idx_array = []

    while i < len_text:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len_pattern:
            idx_array.append(i-j+1)
            j = lps[j-1]

        elif i < len_text and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]

            else:
                i += 1
        
    return idx_array
    

text = input()
pattern = input()

arr = kmp_search(pattern, text)
print(len(arr))
print(*arr, sep=' ')
