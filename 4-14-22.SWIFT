import Foundation

/*
 * Complete the 'viralAdvertising' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */

func viralAdvertising(n: Int) -> Int {
    var recipients: Int = 5
    var cumalativeLikes: Int = 0
    var dailyLikes: Int
    for _ in 1...n {
        dailyLikes = recipients/2
        cumalativeLikes += dailyLikes
        recipients = dailyLikes*3
    }
    return cumalativeLikes
}

print(viralAdvertising(n: 1))
print(viralAdvertising(n: 2))
print(viralAdvertising(n: 3))
print(viralAdvertising(n: 4))
print(viralAdvertising(n: 5))

// Day Shared Liked Cumulative (Should return the following)
// 1      5     2       2
// 2      6     3       5
// 3      9     4       9
// 4     12     6      15
// 5     18     9      24