import Foundation

/*
 * Complete the 'sockMerchant' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY ar
 */

func sockMerchant(n: Int, ar: [Int]) -> Int {
    var colorOptions: [Int:Int] = [:]
    for i in 0..<n {
        if colorOptions[ar[i]] == nil {
            colorOptions[ar[i]] = 1
        }
        else if colorOptions[ar[i]] != nil {
            colorOptions[ar[i]]! += 1
        }
    }
    var totalPairs = 0
    for color in colorOptions.values {
        totalPairs += color/2
    }
    return totalPairs
}

print(sockMerchant(n: 9, ar: [10,20,20,10,10,30,50,10,20]))
print(sockMerchant(n: 11, ar: [1,2,2,3,3,3,3,5,5,5,6]))
