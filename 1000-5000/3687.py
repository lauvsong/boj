import sys
input = sys.stdin.readline

def getResult():
    minimum = getMinimum(n)
    maximum = getMaximum(n)

    print(minimum, maximum)

def getMinimum(n):
    dp = mins + [0]*92

    for i in range(9,n+1):
        dp[i] = dp[i-2] * 10 + 1

        for j in range(3,8):
            if j == 6: dp[i] = min(dp[i], dp[i-j] * 10)
            else: dp[i] = min(dp[i], dp[i-j] * 10 + mins[j])

    return dp[n]


def getMaximum(n):
    if n % 2 == 0: result = '1' * (n // 2)
    else: result = '7' + '1' * (n // 2 - 1)

    return result

testCaseCount = int(input())
mins = [0,0,1,7,4,2,6,8,10]

for _ in range(testCaseCount):
    n = int(input())
    getResult()


"""
성냥개비

n: 성냥개비의 개수


n개로 만들 수 있는 가장 작은수, 가장 큰수
- 양수
- 0으로 시작X


# 가장 큰 경우
그리디 조건
1. 자릿수가 클수록 크다.
   - 성냥개비가 적게 드는 숫자로 최대한 구성
        1) 짝수: 1을 나열하면 됨
        2) 홀수: 큰 자릿수에 7 하고 뒤에 싹다 1하면 되는거 아님..?
2. 큰 자릿수의 숫자가 클수록 크다.


# 가장 작은 경우
1. 자릿수가 최대한 작아야 한다.
    - 성냥개비가 많이 드는 숫자부터 뒤에 배치 -> (그리디 성립 X)
    
2. 큰 자릿수가 작을 수록 작다.


## Dynamic Programming
dp[i]: i개의 성냥개비를 썼을 때 나타낼 수 있는 최소의 숫자
j: 숫자의 성냥개비 개수
num: 숫자

케이스 1. 앞에 붙는 경우
케이스 2. 뒤에 붙는 경우

dp[i] = dp[i-2]*10 + 1

"""