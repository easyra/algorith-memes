//import arr1 from '../example-arrays';
const arr1 = [2, 6, 3, 9, 6, 1, 6, 8, 0, 4, 7, 5];

console.log(arr1);

function selectionSort1(arr) {
  const unsortedArr = [...arr];
  const sortedArr = [];
  while (sortedArr.length < arr.length) {
    let smallestNumIndex = 0;
    for (let i = 0; i < arr.length; i++) {
      if (unsortedArr[i] < unsortedArr[smallestNumIndex]) {
        smallestNumIndex = i;
      }
    }
    sortedArr.push(unsortedArr[smallestNumIndex]);
    unsortedArr.splice(smallestNumIndex, 1);
  }
  return sortedArr;
}

console.log(selectionSort1(arr1));
