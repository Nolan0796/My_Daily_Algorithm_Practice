import Foundation

/*
    The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.
    A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after  growth cycles?
 * Complete the 'utopianTree' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */

func utopianTree(n: Int) -> Int {
    var height = 0
    for i in 0...n {
        if i % 2 == 0 {
            height += 1
        }
        else {
            height *= 2
        }
    }
    return height
}

print(utopianTree(n: 5))
print(utopianTree(n: 30))

