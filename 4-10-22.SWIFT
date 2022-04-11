import Foundation

/*
 * Complete the 'bonAppetit' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY bill
 *  2. INTEGER k
 *  3. INTEGER b
 */

func bonAppetit(bill: [Int], k: Int, b: Int) -> Void {
    var annasTotal: Float = 0
    for i in 0..<(bill.count) {
        if i == k {
            continue
        }
        else {
            annasTotal += Float(Double(bill[i])/2.0)
        }
    }
    
    if Int(annasTotal) == b {
        print("Bon Appetit")
    }
    else {
        print(b-Int(annasTotal))
    }
}

bonAppetit(bill: [3, 10, 2, 9], k: 1, b: 12)
bonAppetit(bill: [3, 10, 2, 9], k: 1, b: 7)