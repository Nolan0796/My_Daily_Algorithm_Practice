import Foundation

/*
 *  Complete the getMoneySpent function below.
    returns int: the maximum that can be spent, or -1 if it is not possible to buy both items
 */
func getMoneySpent(keyboards: [Int], drives: [Int], b: Int) -> Int {
    var maxTotal = -1
    if keyboards.count > drives.count {
        for i in 0..<keyboards.count {
            for j in 0..<drives.count {
                if keyboards[i] + drives[j] > maxTotal && keyboards[i] + drives[j] <= b {
                    maxTotal = keyboards[i] + drives[j]
                }
            }
        }
    }
    if keyboards.count < drives.count {
        for i in 0..<drives.count {
            for j in 0..<keyboards.count {
                if keyboards[j] + drives[i] > maxTotal && keyboards[j] + drives[i] <= b {
                    maxTotal = keyboards[j] + drives[i]
                }
            }
        }
    }
    return maxTotal
}

print(getMoneySpent(keyboards: [5,3,4], drives: [2,1], b: 7))
print(getMoneySpent(keyboards: [33,40,35,50], drives: [10,15,18], b: 35))
