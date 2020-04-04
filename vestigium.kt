import java.util.*
import java.util.HashMap


fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)
    var kotlin = scan.nextLine().toInt()
    for (k in 1..kotlin) {
        var x = scan.nextLine().toInt()
        val s = Array(x, { IntArray(x) })
        var r = 0
        var c = 0
        var t = 0
        var flag = false
        var map = HashMap<Char, Int>()
        for (i in 0..x - 1) {
            s[i] = scan.nextLine().split(" ").map { it.trim().toInt() }.toIntArray()
        }

        for (i in 0..x - 1) {
            flag = false
            t+=s[i][i]

            for (m in 0..x - 2) {
                for (n in m+1..x-1) {
                if (s[i][m] == s[i][n])
                    flag = true
                 }
            }
            if (flag == true)
                r++
        }

        for (i in 0..x - 1) {
            flag = false

            for (m in 0..x - 2) {
                    for(n in m+1..x-1)
                    {
                        if (s[m][i] == s[n][i])
                            flag = true
                    }

            }
            if (flag == true)
                c++
        }
        println("Case #${k}: ${t} ${r} ${c}")
    }
}