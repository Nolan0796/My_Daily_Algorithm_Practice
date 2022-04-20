import Foundation

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

func countingValleys(steps: Int, path: String) -> Int {
    var elevation = 0
    var valleyCount = 0
    for i in 0..<steps {
        let index = path.index(path.startIndex, offsetBy: i)
        if String(path[index]) == "U" {
            if elevation < 0 {
                elevation += 1
                if elevation == 0 {
                    valleyCount += 1
                }
            }
            else {
                elevation += 1
            }
        }
        else {
            elevation -= 1
        }
    }
    return valleyCount
}

print(countingValleys(steps: 8, path: "UDDDUDUU"))
print(countingValleys(steps: 12, path: "DDUUDDUDUUUD"))

