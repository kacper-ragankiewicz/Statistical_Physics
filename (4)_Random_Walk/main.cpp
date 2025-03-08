#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;

int main()
{
    srand((unsigned)time(NULL));
    vector<int> values;
    const int N = 1000;
    const int K = 1000;

    srand(time(0)); // Seed for random number generation

    auto start = chrono::high_resolution_clock::now();

    for (int i = 0; i <= K; i++)
    {
        int x = 0;
        for (int j = 0; j <= N; j++)
        {
            float u = (float)rand() / RAND_MAX;
            if (u < 0.5)
                x++;
            else
                x--;
            values.push_back(x);
        }
    }

    auto stop = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(stop - start);

    cout << "Execution time: " << duration.count() << " milliseconds." << endl;

    return 0;
}
