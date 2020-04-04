
import java.util.*

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)
    var kotlin = scan.nextLine().toInt()

    for (k in 1..kotlin) {
        var n = scan.nextLine().toInt()
        val t = Array(n, { IntArray(2) })
        val pos = IntArray(n)

        var ca = 0
        var cb = 0
        var ja = 0
        var jb = 0
        var answer = ""
        var flag=true

        for (i in 0..n - 1) {
            answer += "a"
        }
        var ans = StringBuilder(answer)
        var c = 0
        var j = 0
        var used = 0

        for (i in 0..n - 1) {
            t[i] = scan.nextLine().split(" ").map { it.trim().toInt() }.toIntArray()
            pos[i] = i
        }

        for (i in 0..n - 1) {
            for (j in 0..n - 2) {
                    if (t[j][0] > t[j + 1][0]) {
                        var temp = t[j][0]
                        t[j][0] = t[j + 1][0]
                        t[j + 1][0] = temp

                        temp = t[j][1]
                        t[j][1] = t[j + 1][1]
                        t[j + 1][1] = temp

                        temp = pos[j]
                        pos[j] = pos[j + 1]
                        pos[j + 1] = temp

                }
            }
        }

        for (i in 0..n - 1) {

            var x = t[i][0]
            var y = t[i][1]

            if(cb<=x && cb!=0)
            {
                ca=0
                cb=0
                used--
            }
            if(jb<=x && jb!=0)
            {
                ja=0
                jb=0
                used--
            }

            if(used<2)
            {
                if ((ca == 0 && cb == 0)) {
                    ca = x
                    cb = y
                    ans[pos[i]] = 'C'

                } else if ((ja == 0 && jb == 0)) {
                    ja = x
                    jb = y
                    ans[pos[i]] = 'J'
                }
                used++
            }
            else {
                flag=false
                break
            }

        }
        if(flag==false)
            println("Case #${k}: IMPOSSIBLE")
        else
            println("Case #${k}: ${ans}")
    }
}