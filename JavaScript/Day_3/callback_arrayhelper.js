// 콜백 함수
// 다른 함수의 인자로 전달되는 함수
const calculator = function(a, b, mathFunction){
  return mathFunction(a, b)
}

const add = function(a, b){
return a + b
}

const sub = function(a, b){
return a - b
}



// add, sub 를 콜백 함수라고 부름
console.log(calculator(3, 5, add))
// add 함수를 화살표 함수로 바꾸기
console.log(calculator(3, 5, (a, b) => a + b))
console.log(calculator(3, 5, sub))

// Array Helper Method 란?
// - 배열 조작을 쉽게 만들어 주는 JS 내장 메서드
// - 얼마나 잘 쓰느냐에 따라 개발 속도가 엄청나게 차이난다

const lunchMenu = [
  { name: '김치찌개', price: 8000 },
  { name: '돼지국밥', price: 9000 },
  { name: '카레', price: 7500 },
  { name: '햄버거', price: 8500 },
  { name: '초밥', price: 12000 },
  { name: '김밥', price: 5000 }
];

// ----------------------------------------------------------------------------
// 문제1. 메뉴 맛있겠다 외치기
// 출력
// 김치찌개 맛있겠다!
// 돼지국밥 맛있겠다!
// 카레 맛있겠다!
// 햄버거 맛있겠다!
// 초밥 맛있겠다!
// 김밥 맛있겠다!

const delicious = lunchMenu.forEach((lunch) => console.log(`${lunch.name} 맛있겠다!`))
// 1. forEach
// - 주어진 배열의 각 요소에 대해 함수 실행
// - 새로운 배열 생성 X
// - Array.forEach((element, index, array) => {

// })



// ----------------------------------------------------------------------------
// 문제2. 내가 가진 돈은 15,000원 이다. 각 메뉴를 먹고 나서 남은 가격을 배열로 출력하시오.
// 출력
// [ 7000, 6000, 7500, 6500, 3000, 10000 ]


// 2. map
// - 주어진 배열의 각 요소에 대해 함수 실행
// - 새로운 배열 생성 O
// Array.map((element, index, array) => {
// })
let money = 15000

const leftmoney = lunchMenu.map((menuMoney) => money - menuMoney.price)
console.log(leftmoney)



// ----------------------------------------------------------------------------
// 문제3. 내가 가진 돈은 15,000원 이다. 각 메뉴에 먹고 나서 남은 가격을 추가한 새로운 배열을 출력하시오.
// 출력
// [
//   { name: '김치찌개', price: 8000, remainMoney: 7000 },
//   { name: '돼지국밥', price: 9000, remainMoney: 6000 },
//   { name: '카레', price: 7500, remainMoney: 7500 },
//   { name: '햄버거', price: 8500, remainMoney: 6500 },
//   { name: '초밥', price: 12000, remainMoney: 3000 },
//   { name: '김밥', price: 5000, remainMoney: 10000 }
// ]
// 3. filter
// - 조건에 만족하는 요소들만 새로운 배열로 반환
// Array.filter((element, index, array) => {
// })
const remains2 = lunchMenu.map((menu, index, array) => {
  // return `name: ${menu.name}, price: ${menu.price}, remainMoney: ${money - menu.price}`
  const remainMoney = money - menu.price
  return { ...menu, remainMoney }
})
console.log(remains2)


// ----------------------------------------------------------------------------
// 문제4. 가격이 8000원 이하인 메뉴만 걸러내시오.
// 출력
// [
//     { name: '김치찌개', price: 8000 },
//     { name: '카레', price: 7500 },
//     { name: '김밥', price: 5000 }
//   ]

// 4. find
// - 특정 조건에 만족하는 "첫 번째 값"을 찾고싶어
// - 값이 없다면 undefined 가 반환된다.
// Array.find((element, index, array) => {
// })

const under8000 = lunchMenu.filter((menu) => {
  return menu.price <= 8000;
})
console.log(under8000)


// ----------------------------------------------------------------------------
// 문제5. '초밥'을 파는 지 찾으시오.
// 출력
// 있다면 { name: '초밥', price: 12000 } 출력
// 없다면 undefined 출력

const findSushi = lunchMenu.find((menu) => {
  return menu.name === '초밥';
})
console.log(findSushi)
  

// ----------------------------------------------------------------------------
// 문제6. 내가 가진 돈으로 사먹지 못하는 메뉴가 있는 지 확인하시오.
// 있다면 "더 비싼 메뉴 있음!" 출력
// 없다면 "더 비싼 메뉴 없음!" 출력

// some : 조건충족 하나라도 있으면 true
// every : 모든 요소가 조건 만족하면 true
money = 10000
const canbuy = lunchMenu.some((menu) => {
  return menu.price > money
})


if (canbuy) console.log('더 비싼 메뉴 있음')
else console.log('더 비싼 메뉴 없음')

// 삼항 연산자로 조건문 쓰기
// 조건문 ? true일때 : false 일때
canbuy ? console.log('더 비싼 메뉴 있음!') : console.log('더 비싼 메뉴 없음!')


// if (canbuy === true) {
//   console.log('더 비싼 메뉴 있음!')
// } else {
//   console.log('더 비싼 메뉴 없음!')
// }



// ----------------------------------------------------------------------------
// 문제7. 모든 메뉴 가격 총합 구하기
// 출력
// 총 가격 : 50000
const sumPrice = lunchMenu.reduce((acc, menu) => {
  return acc + menu.price;
}, 0);
console.log(sumPrice)

// reduce 
// 각 요소에 주어진 함수를 실행하고, 하나의 결과값을 누적해서 반환
// Array.reduce((acc, element, index, array) => {
  // acc: 누적된 값
// }, start) // start : 시작값