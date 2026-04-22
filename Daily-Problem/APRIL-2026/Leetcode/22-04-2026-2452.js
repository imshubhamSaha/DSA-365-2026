//2452. Words Within Two Edits of Dictionary
/**
 * @param {string[]} queries
 * @param {string[]} dictionary
 * @return {string[]}
 */
var twoEditWords = function(queries, dictionary) {
    const q = queries.length;
    const n = dictionary.length;
    const included_words = [];

    for (let i = 0; i < q; i++) {
        const word = queries[i];
        for (let j = 0; j < n; j++) {
            if (word === dictionary[j]) {
                included_words.push(word);
                break;
            }
            let idx = 0;
            let difference = 0;
            while (idx < word.length) {
                if (word[idx] != dictionary[j][idx])
                    difference += 1;
                if (difference > 2)
                    break;
                idx += 1;
            }
            if (difference <= 2) {
                included_words.push(word);
                break;
            }
        }
    }

    return included_words;
};
