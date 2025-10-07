/**
 * @param {number} N
 * @param {number} M
 * @param {number[]} C
 * @return {number}
 */
function getMinCodeEntryTime(N, M, C) {
    // Write your code here
    C.unshift(1);
    let totalTime = 0;

    for (let i = 0; i < C.length - 1; i++) {
        const current = C[i];
        const next = C[i + 1];

        if (current === next) {
            continue;
        }

        let clockwise = current - next;
        let counterclockwise = next - current;

        if (clockwise < 0) {
            clockwise += N;
        }
        if (counterclockwise < 0) {
            counterclockwise += N;
        }

        totalTime += Math.min(clockwise, counterclockwise);
    }

    return totalTime;
}

function main() {
    const test1 = () => {
        const N = 3;
        const M = 3;
        const C = [1, 2, 3];

        const result = getMinCodeEntryTime(N, M, C);
        const expected = 2;

        console.log(result);
        return result === expected;
    }

    const test2 = () => {
        const N = 10;
        const M = 4;
        const C = [9, 4, 4, 8];

        const result = getMinCodeEntryTime(N, M, C);
        const expected = 11;

        console.log(result);
        return result === expected;
    }

    test1();
    test2();
}

main();