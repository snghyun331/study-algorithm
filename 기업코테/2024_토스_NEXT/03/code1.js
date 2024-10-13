/* 각 CCTV의 녹화 구간이 주어졌을 때 그 구간을 통합하고 누락된 시간대를 확인한다.(연속되지 않는 구간찾기)*/

function findMissingRecordingTimes(cctvRecords) {
  /* 1. 모든 녹화 구간을 하나의 배열로 병합하고, 시작 시간 기준으로 정렬 */
  const mergedRecords = [];
  for (const records of cctvRecords) {
    mergedRecords.push(...records);
  }
  mergedRecords.sort((a, b) => a[0] - b[0]); // 시작 시간을 기준으로 정렬

  /* 2. 구간 병합 (중복 및 겹치는 구간을 병합) */
  const combinedIntervals = [];
  let currentStart = mergedRecords[0][0];
  let currentEnd = mergedRecords[0][1];

  for (let i = 1; i < mergedRecords.length; i++) {
    const [nextStart, nextEnd] = mergedRecords[i];

    if (nextStart <= currentEnd) {
      currentEnd = Math.max(currentEnd, nextEnd); // 현재 구간이 다음 구간과 겹치는 경우, 종료 시간을 갱신
    } else {
      combinedIntervals.push([currentStart, currentEnd]); // 겹치지 않는 경우, 현재 구간을 추가하고 새 구간 시작
      currentStart = nextStart;
      currentEnd = nextEnd;
    }
  }

  combinedIntervals.push([currentStart, currentEnd]); // 마지막 구간 추가

  /* 3. 누락된 시간대 찾기  */
  const missingTimes = [];

  for (let i = 1; i < combinedIntervals.length; i++) {
    const prevEnd = combinedIntervals[i - 1][1];
    const nextStart = combinedIntervals[i][0];

    if (prevEnd < nextStart) {
      missingTimes.push([prevEnd, nextStart]); // 두 구간 사이에 틈이 있는 경우
    }
  }

  return missingTimes;
}

/* 테스트 */
const input = [
  [
    [1, 10],
    [15, 20],
    [25, 30],
  ],
  [[12, 21]],
];

const output = findMissingRecordingTimes(input);
console.log(output); // [[10, 12], [21, 25]]
