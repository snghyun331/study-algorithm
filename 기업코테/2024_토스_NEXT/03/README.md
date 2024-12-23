## 문제3

건물 관리자는 최근 며칠간 데이터 센터 CCTV 시스템에서 여러 대의 CCTV가 간헐적으로 녹화가 끊기는 문제를 발견했다. 모든 cctv가 동시에 작동하지 않은 특정 시간대에는 입주 건물 관리사무소로부터 해당 시간대의 cctv 녹화본을 요청하려고 한다. 모든 cctv에서 녹화가 누락된 시간대가 언제인지 확인하는 기능을 구현해라.

### 유의사항

- 시간 단위는 밀리초 단위로, 녹화 시작 및 종료 timestamp로 들어올 수 있는 값의 범위는 0이상 9,999,999,999,999 이하의 정수.
- 녹화파일 하나는 [녹화시작_timestamp, 녹화종료_timestamp] 튜플형태로 나타내야한다.
- cctv 한대의 녹화 파일 목록은 시간 오름차순으로 정렬된 튜플의 배열로 주어진다.
- 입력 : 여러 대의 cctv가 녹화한 녹화 파일 목록 배열의 배열을 받는다.
- 출력 : 누락된 시간 튜플의 배열을 리턴
- 전체 cctv의 녹화 시작 시간 이전과 이후 시간은 우락된 시간을 취급하지 않는다.

### 입력 예시

```javascript
const input = [
  [
    [1, 10],
    [15, 20],
    [25, 30],
  ],
  [[12, 21]],
];
```

### 출력 예시

```javascript
const output = [
  [10, 12],
  [21, 25],
];
```

### 풀이방법 요약

1. 병합 및 정렬: 모든 CCTV 녹화 구간을 하나의 배열로 병합한 후, 시작 시간 기준으로 정렬
2. 구간 병합: 각 구간을 비교하며 중복되는 구간을 병합. 만약 다음 구간의 시작 시간이 현재 구간의 종료 시간보다 크다면 구간을 병합하지 않고, 병합된 구간을 기록한 후 새 구간을 시작
3. 누락된 구간 찾기: 병합된 구간 사이에 틈이 있을 경우, 그 구간을 누락된 시간대로 기록
