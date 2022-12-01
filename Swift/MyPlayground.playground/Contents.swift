let arr = Array<Int>(0...10000)

for i in (2..<arr.count) {
    var prime = true
    for j in (2..<i) {
        if i % j == .zero {
            prime = false
        }
    }
    if prime {
        print(i)
    }
}


