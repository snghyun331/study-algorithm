# **동적계획법(Dynamic Programming)**

- 문제를 쪼개서 작은 문제의 답을 구하고, 그걸로 더 큰 문제의 답을 구하는 것을 반복
- Top-down(재귀, Memoization)
  - Memoization(한번 구한 답들은 저장해두기 - 중복연산방지)
    - 필요있는 부분 문제들만
- Bottim-up(반복문, Tabulation)
  - Tabulation(답을 미리 다 구해두기)
    - 필요없는 부분 문제들까지

## **피보나치**

F(0) = 0  
F(1) = 1  
F(n) = F(n-2) + F(n-1)

## **이항계수**

bino(n,0) = 1  
bino(n.n) = 1  
bino(n,r) = bino(n-1, r-1) + bino(n-1, r)
