/**
 * @param {number} N
 * @param {number[]} D
 * @param {number} K
 * @return {number}
 */
function getMaximumEatenDishCount(N, D, K) {
    // Write your code here
    let eatHistory = [];
    let lastEatenIndicies = {};

    for (let i = 0; i < N; i++) {
        const dish = D[i];

        const lastEatenIdx = lastEatenIndicies[dish];
        // console.log(`processing i=`,i,'\tdish=', dish, '\t last eaten idx: ', lastEatenIdx);
        if (lastEatenIdx === undefined || eatHistory.length - lastEatenIdx > K) {
            lastEatenIndicies[dish] = eatHistory.length;
            eatHistory.push(dish);
            // console.log(`Eat history: `, JSON.stringify(eatHistory));
        }
    }

    return eatHistory.length;
}

function main() {
    const test1 = () => {
        const N = 6;
        const D = [1, 2, 3, 3, 2, 1];
        const K = 1;

        const result = getMaximumEatenDishCount(N, D, K);
        const expected = 5;

        console.log(result);
        return result === expected;
    }

    const test2 = () => {
        const N = 6;
        const D = [1, 2, 3, 3, 2, 1];
        const K = 2;

        const result = getMaximumEatenDishCount(N, D, K);
        const expected = 4;

        console.log(result);
        return result === expected;
    }

    const test3 = () => {
        const N = 7;
        const D = [1, 2, 1, 2, 1, 2, 1];
        const K = 2;

        const result = getMaximumEatenDishCount(N, D, K);
        const expected = 2;

        console.log(result);
        return result === expected;
    }

    test1();
    test2();
    test3();
}

main();