def solution1(participant, completion):
    """ 효율성 테스트
    테스트 1 〉	통과 (30.47ms, 18MB)
    테스트 2 〉	통과 (57.01ms, 22.2MB)
    테스트 3 〉	통과 (67.59ms, 24.7MB)
    테스트 4 〉	통과 (71.31ms, 26.2MB)
    테스트 5 〉	통과 (71.62ms, 26.3MB)

    비슷하게 다음과 같이 할 수도 있음
    def solution(participant, completion):
        participant.sort()
        completion.sort()
        for p, c in zip(participant, completion):
            if p != c:
                return p
        return participant[-1]
    """
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[len(participant) -1]

def solution2(participant, completion):
    """ 효율성 테스트
    테스트 1 〉	통과 (22.40ms, 23.8MB)
    테스트 2 〉	통과 (32.85ms, 28.4MB)
    테스트 3 〉	통과 (36.79ms, 31.4MB)
    테스트 4 〉	통과 (44.71ms, 37.6MB)
    테스트 5 〉	통과 (44.03ms, 37.6MB)
    """
    # 1. 참가자의 hash 값을 구하고, 그걸 더해서 누적한다.
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # 2. 완주자들의 해시값을 구해서 누적한 값에서 뺀다.
    for comp in completion:
        sumHash -= hash(comp)

    return hashDict[sumHash]

from collections import Counter

def solution3(participant, completion):
    """ 효율성 테스트
    테스트 1 〉	통과 (28.85ms, 24.3MB)
    테스트 2 〉	통과 (40.97ms, 27.7MB)
    테스트 3 〉	통과 (52.74ms, 30MB)
    테스트 4 〉	통과 (77.58ms, 38.9MB)
    테스트 5 〉	통과 (75.12ms, 39MB)
    """
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

print(solution3(["leo", "kiki", "eden"], ["eden", "kiki"]))

# 결론: 해시가 가장 빨랐다.

# 다른사람의 코드

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer