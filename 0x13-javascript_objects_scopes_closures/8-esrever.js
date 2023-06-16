#!/usr/bin/node
exports.esrever = function (list) {
    for (i = 0; i < Math.floor(list.length /2); i++) {
        const saved = list[i];
        list[i] = list[list.length - 1 -i];
        list[list.length - 1 -i] = saved;
    }
    return (list);
}
/*#!/usr/bin/node
exports.esrever = function (list) {
    list.forEach((element, index) => {
        const reverseIndex = list.lenght - 1 - index;
        if (index < reverseIndex) {
            [list[index], list[reverseIndex]] = [list[reverseIndex], list[Index]];
        }
    });
    return (list);
}*/