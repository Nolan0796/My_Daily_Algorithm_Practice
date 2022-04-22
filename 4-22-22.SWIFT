import Foundation

/*
 * Complete the 'hurdleRace' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY height
 */

func hurdleRace(k: Int, height: [Int]) -> Int {
    let highestHurdle = height.max()!
    if (highestHurdle - k) > 0 {
        return highestHurdle - k
    }
    else {
        return 0
    }

}

print(hurdleRace(k: 4, height: [1,6,3,5,2]))
print(hurdleRace(k: 7, height: [2,5,4,5,2]))
