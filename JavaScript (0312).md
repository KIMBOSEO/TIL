# JavaScript (03/12)

## javascript 배경

html이 뼈대고 자바가 움직이게 해준다



브라우저에서 할 수 있는 일

- 전역 개체 window
  - DOM 조작
  - BOM 조작
    - navigator, screen, location, frames, history, XHR
  - JavaScript
    - Object, Array, Function



Dom

- Document에 있는 타이틀을 바꾸고, 타이틀에 새로운 값을 넣고 출력 가능

BOM

- window에 너비 값을 알아 낼 수 있다

여기까지는 브라우저 조정만 가능! 따라서, 언어라고 안쳐줌



JavaScript

V8엔진-> frontend의 개발을 도왔다면, nodeJS -> backend까지 개발

이로인해 JavaScript가 폭발적으로 사용량이 늘어났다.



## javascript 기초

#### 변수 선언

- 변수 선언은 `var` 키워드를 활용해야 함.
-  ES6 기준으로 아래와 같은 키워드가 등장함.
  - const
  - let

#### 데이터 타입 분류(type of)

- 원시 타입(primitive) - 변경 불가능한 값(immutable)
  - boolean - true, false
  - null
  - undefined
  - number
  - strung
  - symbol (ES6)
- 객체 타입(object)
  - object: 일반 객체, function, array, date, RegExp

#### Number

- 모든 숫자는 number 타입
- 8진수(0), 16진수(0x)로 표현 가능
- 추가적으로 Infinity, -infinity, Nan(not a number)도 number 타입



#### String - 템플릿 문자열(ES6)

- 템플릿 문자열
  - 편하게 문자열 내에 변수를 사용 가능
  - 여러 라인으로 이뤄진 문자열 사용 가능



#### null vs undefined

- null
  - 의도적으로 변수에 값이 없다는 것을 명시
  - typeof 출력시 object로 출력되는 것은 설계상의 실수
- undefined
  - 선언 이후 할당하지 않은 변수에 지정된 값
  - 자바스크립트 엔진이 할당 이전에 초기화된 값
  - 직접 값으로 할당해서 사용하는 것 금지

#### 객체

- 자바스크립트는 원시 타입을 제외하고는 모두 객체이다.
- 자바스크립트의 객체는 키와 값으로 구성된 속성의 집합이며, 프로퍼티 값이 함수일 경우 구분을 위해 메소드라고 부른다.

#### 변수 유효 범위(scope)

- 자바스크립트는 함수 레벨 스코프를 가진다.
- 따라서 함수 내에서 선언된 변수는 지역 변수이며,
- 나머지는 전역 변수로 활용된다
- 변수 선언시 키워드를 쓰지 않으면, 암묵적 전역으로 설정된다.
  - 주의: 변수가 아닌 전역객체(window)의 프로퍼티로 생성
  - 따라서, delete로 지워지는 값

## javascript 문법

- 연산자
- 조건문
- 반복문



#### #밈  == vs ===  

- 동등 연산자(==)
  - 값 비교 및 예상치 않은 변환
- 일치 연산잔(===)
  - 엄경한 같음. 형 비교