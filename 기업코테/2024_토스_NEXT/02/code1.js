function getFileTypeFromBase64(base64Encoded) {
  // Base64 인코딩된 문자열을 바이너리 데이터로 디코딩 -> 16진수 문자열로 변환
  const binaryString = Buffer.from(base64Encoded, "base64").toString("hex").toUpperCase();

  // 매직 넘버와 파일 타입을 매핑
  const magicNumbers = {
    25504446: "pdf",
    "89504E47": "png",
    FFD8FF: "jpg",
    "504B0304": "zip",
    47494638: "gif",
    "424D": "bmp",
  };

  // 첫 4~8바이트의 매직 넘버 추출
  const firstBytes = binaryString.slice(0, 8);

  // 매직 넘버 비교
  for (const [magicNumber, fileType] of Object.entries(magicNumbers)) {
    if (firstBytes.startsWith(magicNumber)) {
      return fileType;
    }
  }

  // 매칭되는 매직 넘버가 없으면 unknown 반환
  return "unknown";
}

/* 테스트 */
const base64EncodedPDF = "JVBERi0xLjMKJcTl8uXrp/Og0MTGCjI0NTAwMQo=";
console.log(getFileTypeFromBase64(base64EncodedPDF)); // pdf

const base64EncodedPNG = "iVBORw0KGgoAAAANSUhEUgAAAAUA";
console.log(getFileTypeFromBase64(base64EncodedPNG)); // png

const base64EncodedJPG = "/9j/4AAQSkZJRgABAQEAAAAAAAD";
console.log(getFileTypeFromBase64(base64EncodedJPG)); // jpg

const base64EncodedUnknown = "AAECAwQFBgcICQoLDA0ODw==";
console.log(getFileTypeFromBase64(base64EncodedUnknown)); // unknown
