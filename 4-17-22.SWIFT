import Foundation

/*
 * Complete the 'pageCount' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER p
 */

func pageCount(n: Int, p: Int) -> Int {
    var minimum = p/2
    if ((n-p)/2) < minimum {
        if p == n {
            minimum = 0
        }
        else if (n%2 != 0 && p+1 == n) {
            minimum = 0
        }
        else if (n%2 == 0 && n-p == 1) {
            minimum = 1
        }
        else { 
            minimum = ((n-p)/2)
        }
    }
    return minimum
}

print(pageCount(n:6, p:2))
print(pageCount(n:5, p:4))