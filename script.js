function findNextSquare(sq) {
    // Calculate the square root of the given number
    const root = Math.sqrt(sq);

    // Check if the square root is an integer
    if (Number.isInteger(root)) {
        // Calculate the next perfect square
        const nextSquare = Math.pow(root + 1, 2);
        return nextSquare;
    } else {
        // If the number is not a perfect square, return -1
        return -1;
    }
}
