#include <bits/stdc++.h>

using namespace std;

int squarerootdemo[60][60], n, k, t;
bool rowsolutions[60][60], colsolutions[60][60], solutionpossible;

void solver(int rowsolution, int colsolution, int m) {
    if (rowsolution == n && colsolution == n + 1 && m == k && !solutionpossible) {
        solutionpossible = true;
        cout << "Case #" << t << ": " << "POSSIBLE\n";
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cout << squarerootdemo[i][j] << " ";
            }
            cout << "\n";
        }
        return;
    } else if (rowsolution > n) {
        return;
    } else if (colsolution > n) {
        solver(rowsolution + 1, 1, m);
    }
    for (int i = 1; i <= n && !solutionpossible; ++i) {
        if (!rowsolutions[rowsolution][i] && !colsolutions[colsolution][i]) {
            rowsolutions[rowsolution][i] = colsolutions[colsolution][i] = true;
            if (rowsolution == colsolution) {
                m += i;
            }
            squarerootdemo[rowsolution][colsolution] = i;

            solver(rowsolution, colsolution + 1, m);

            rowsolutions[rowsolution][i] = colsolutions[colsolution][i] = false;
            if (rowsolution == colsolution) {
                m -= i;
            }
            squarerootdemo[rowsolution][colsolution] = 0;
        }
    }
}

int main() {
    int T;
    scanf(" %d", &T);
    for (t = 1; t <= T; ++t) {
        scanf(" %d %d", &n, &k);
        solver(1, 1, 0);
        if (!solutionpossible) {
            cout << "Case #" << t << ": " << "IMPOSSIBLE\n";
        }
        solutionpossible = false;
    }
    return 0;
}