def find_anagrams(word, candidates):
    t=word.lower()
    st=sorted(t)

    result=[]

    for candidate in candidates:
        lc=candidate.lower()

        if lc==t:
            continue 

        if sorted(lc)==st:
            result.append(candidate)

    return result
