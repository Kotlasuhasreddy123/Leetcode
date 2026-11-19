type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    const filter: number[] = [];
    for (let i = 0; i < arr.length; i++){
        if (fn(arr[i], i)){
            filter.push(arr[i]);
        }
    }
    return filter;
};