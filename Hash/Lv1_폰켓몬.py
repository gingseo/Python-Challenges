def my_solution(nums):
    N = len(nums) / 2

    sort = {}
    # sort = [0] * (max(nums) + 1)
    for i in nums:
        sort[i] = 1
    print(sort)

    cate = len(sort.keys())
    print(cate)

    if cate <= N:
        return cate
    else:
        return N

def solution_1(num):
    """
    니링 비슷한데, 중복을 제거할 때 나는 딕셔너리로 했는데 set으로 숫자만 zip했다.
    그리고 min을 써서 둘 중 비교를 쉽게 했다.
    """
    return min(len(num)/2, len(set(num)))

def solution(nums): # 해시를 사용한 코
    n_dict = dict()                   # Hash
    
    for n in nums:
        n_dict[n] = 1                 # 같은 종류의 폰켓몬의 중복이 제거된다.
    # n_dict의 크기(len(n_dict))를 계산하는 것은 len(n_dict.keys())와 동일
    if len(nums) // 2 <= len(n_dict): # 전체 종류의 수/2와 중복 제거된 종류의 수를 비교
        return len(nums) // 2         # 전체 종류의 수/2값이 작거나 같다면 즉시 반환
    
    return len(n_dict)                # 그렇기 않다면 중복 제거된 종류의 수를 반환

test_list = [3,3,3,2,2,2]
print(solution_1(test_list))