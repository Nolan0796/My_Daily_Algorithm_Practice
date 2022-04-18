import Foundation

/*
 * Complete the 'migratoryBirds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

func migratoryBirds(arr: [Int]) -> Int {
    var totals: [Int:Int] = [:]
    for i in 0..<Int(arr.count) {
        if totals[arr[i]] == nil {
            totals[arr[i]] = 1
        }
        else {
            totals[arr[i]]! += 1
        }
    }
    var max = 0
    for total in totals.values {
        if total > max {
            max = total
        }
    }
    var totalMax: [Int:Int] = [:]
    for (id, total) in totals {
        if total == max {
            totalMax[id] = total
        }
    }
    if totalMax.count > 1{
        var minID = 5
        for id in totalMax.keys {
            if id < minID {
                minID = id
            }
        }
        return minID
    }
    var maxID = 0
    for key in totalMax.keys {
        maxID = key
    }
    return maxID
}

print(migratoryBirds(arr: [1,4,4,4,5,3]))
print(migratoryBirds(arr: [1,2,3,4,5,4,3,2,1,3,4]))
