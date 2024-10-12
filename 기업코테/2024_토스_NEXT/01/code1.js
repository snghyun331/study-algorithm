function hasConsoleLog(fn) {
  const fnString = fn.toString(); // 함수의 내용을 문자열로 반환

  return /console\.log\s*\(.*\)/.test(fnString); // 정규식을 이용해 console.log 호출 여부를 검사
}

/* 테스트 */

// hasConsoleLog 인자에 들어갈 함수 만들기
function test1() {
  console.log("Hello world");
}

function test2() {
  return "No console log";
}

console.log(hasConsoleLog(test1)); // true
console.log(hasConsoleLog(test2)); // false
