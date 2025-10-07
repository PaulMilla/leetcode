/**
 * @param {number} N - length of string C
 * @param {string} C - string consisting of characters 'A', 'P', and 'B'
 * @param {number} X - minimum distance between 'A' and 'P'/'B'
 * @param {number} Y - maximum distance between 'A' and 'P'/'B'
 * @return {number}
 */
function getArtisticPhotographCount(N, C, X, Y) {
    let pCells = [];
    let pACells = [];
    let pABCells = [];

    let bCells = [];
    let bACells = [];
    let bAPCells = [];

    // Forward
    for (let i = 0; i < N; i++) {
        const cell = C[i];
        if (cell === 'P') {
            pCells.push(i);
            // console.log(`new P Cells: `, JSON.stringify(pCells));
        }
        else if (cell === 'A') {
            pCells.forEach(pIdx => {
                const dist = Math.abs(i - pIdx);
                if (X <= dist && dist <= Y) {
                    pACells.push([pIdx, i]);
                    // console.log(`new P-A cells:`, JSON.stringify(pACells));
                }
            });
        }
        else if (cell === 'B') {
            pACells.forEach(pAIdx => {
                const dist = Math.abs(i - pAIdx[1]);
                if (X <= dist && dist <= Y) {
                    pABCells.push([pAIdx[0], pAIdx[1], i]);
                    // console.log(`new P-A-B cells:`, JSON.stringify(pABCells));
                }
            });
        }
    }

    // Backwards
    for (let i = 0; i < N; i++) {
        const cell = C[i];
        if (cell === 'B') {
            bCells.push(i);
            // console.log(`new B Cells: `, JSON.stringify(bCells));
        }
        else if (cell === 'A') {
            bCells.forEach(bIdx => {
                const dist = Math.abs(i - bIdx);
                if (X <= dist && dist <= Y) {
                    bACells.push([bIdx, i]);
                    // console.log(`new B-A cells:`, JSON.stringify(bACells));
                }
            });
        }
        else if (cell === 'P') {
            bACells.forEach(bAIdx => {
                const dist = Math.abs(i - bAIdx[1]);
                if (X <= dist && dist <= Y) {
                    bAPCells.push([bAIdx[0], bAIdx[1], i]);
                    // console.log(`new B-A-P cells:`, JSON.stringify(bAPCells));
                }
            });
        }
    }

    // console.log('P-A-B Cells: ', JSON.stringify(pABCells));
    // console.log('B-A-P Cells: ', JSON.stringify(bAPCells));

    return pABCells.length + bAPCells.length;
}

function main() {
    const test1 = () => {
        const N = 5;
        const C = "APABA";
        const [X, Y] = [1, 2];

        const result = getArtisticPhotographCount(N, C, X, Y);
        const expected = 1;

        console.log(result);
        // assert(result === expected);
        return result === expected;
    }

    const test2 = () => {
        const N = 5;
        const C = "APABA";
        const [X, Y] = [2, 3];

        const result = getArtisticPhotographCount(N, C, X, Y);
        const expected = 0;

        console.log(result);
        // assert(result === expected);
        return result === expected;
    }

    const test3 = () => {
        const N = 8;
        const C = ".PBAAP.B";
        const [X, Y] = [1, 3];

        const result = getArtisticPhotographCount(N, C, X, Y);
        const expected = 3;

        console.log(result);
        // assert(result === expected);
        return result === expected;
    }

    test1();
    test2();
    test3();
}

main();