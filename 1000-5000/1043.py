import sys
input = sys.stdin.readline

ans = 0
n,m = map(int, input().split())
knownCnt, *known = map(int, input().split())

known = set(known)
parties = []
lie = [1]*m

for _ in range(m):
    partyCnt, *party = map(int, input().split())
    parties.append(set(party))

for _ in range(m):
    for i, party in enumerate(parties):
        if party & known:
            known |= party
            lie[i] = 0

print(sum(lie))