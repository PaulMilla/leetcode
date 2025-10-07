/**
 * @param {number} N
 * @param {number[]} S
 * @return {number}
 */
function getMinProblemCount(N, S) {
    let maxNum = Math.max(...S);
    let minCount = Math.floor(maxNum / 2);

    const hasOdd = S.some(n => n % 2 == 1);

    return hasOdd ? minCount + 1 : minCount;
}

function main() {
    const test1 = () => {
        const N = 6;
        const S = [1, 2, 3, 4, 5, 6];

        const result = getMinProblemCount(N, S);
        const expected = 4;

        console.log(result);
        return result === expected;
    }

    test1();
}

main();