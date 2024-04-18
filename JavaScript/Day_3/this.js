// this
// - 특정 Object 를 가리키는 키워드

// Python(self) 에서는 인스턴스 자기자신을 가리킴
// JavaScript 의 this 는 호출 방법에 따라 this 가 가리키는 Object 가 다름

// 자바스크립트는 기본적으로 "전역 객체"를 가지고 있음
// 브라우저: Window / node.js : global

// console.log(global)     // 전역 객체(Node.js 의 표준 전역 객체)
// console.log(globalThis) // 전역 객체
    // (모든 Javascript 환경에서 표준화된 전역 객체에 접근하기 위한 표준 방법)

// nodejs 환경에서 js 파일은 하나의 모듈로 판단
// 즉, this 는 하나의 파일을 가리킴
// 모듈에서 아무것도 내보내고 있지 않기 때문에 {} 출력
// exports.add = function() {
//     console.log('test')
// }
// console.log(this)   // { add: [Function (anonymous)]}

// -----------------------------
// 1. 일반적인 함수에서의 this
const func = function() {
  console.log(this)   // this: 전역 객체(global)
  console.log(this === global)  // true
}
func()
// 2. 객체 내부 메서드에서의 this
const obj = {
  name:'test',
  func: function() {
    console.log(this)
  }, 
  arrowFunc: () => {
    // 화살표 함수는 한 단계 상위 스코프의 this를 참조
    console.log(this) // {}
  }
}
obj.func() // { name: 'test', func: [Function: func] }
// 메서드가 정의된 객체를 나타냄

obj.arrowFunc()
// 가급적 obj 안에는 arrowfunction 사용 지양.
// 단, callback function 쓸 때는 사용해야함

// callback function => arrow function
const obj2 = {
  name: '민채',
  greeting: function() { // 일반함수가 아니라 method 라서
    console.log(this) // obj2

    const arrowFunc = () => {
      console.log(this) // 상위 객체의 this를 가리키므로 obj2
    }

    arrowFunc() // {}

    const normalFunc = function() {
      console.log(this) // 일반함수라서 글로벌 (어디안에있는진 안중요)
    }
    normalFunc() 
  }
}

// 정리
// 1. 일반 함수의 this 는 무조건 전역 객체
// 2. 메서드의 function은 메서드가 정의된 객체
// 3. 화살표 함수의 this 는 렉시컬 스코프 (바로 한 단계위 객체가 가진 this)

const obj3 = {
  arr: [1, 2, 3],
  func: function() {
    this.arr.forEach((el) => {
      console.log(this)  // obj3
    })
  }
}