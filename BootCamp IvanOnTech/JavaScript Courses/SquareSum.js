var array = [];
function squareSum(array) {
	let sum = 0;
	let i = 0;
	while (i <= array.length) {
		sum = sum + array[i] ** 2;
		i++;
	}
	return sum;
}
