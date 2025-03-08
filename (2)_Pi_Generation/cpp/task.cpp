#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cout << "Usage: " << argv[0] << " <value_of_l>" << endl;
        return 1;
    }

    int l = atoi(argv[1]);

    double pi, x, y;
    int idumm = -1;
    int lk = 0;

    srand(time(0)); // Seed for random number generation

    // Measure the start time
    auto start = high_resolution_clock::now();

    // Check if the file exists
    ifstream fileCheck("data/pi_values.dat");
    bool fileExists = fileCheck.good();
    fileCheck.close();

    ofstream outFile("data/pi_values.dat", fileExists ? ios::trunc : ios::app); // Open the file with truncation if it exists

    if (!outFile.is_open())
    {
        cout << "Unable to open the file for saving pi." << endl;
        return 1; // Exit the program if the file can't be opened
    }

    for (int i = 1; i <= l; ++i)
    {
        x = rand() / (double)RAND_MAX;
        y = rand() / (double)RAND_MAX;

        if (x * x + y * y <= 1.0)
        {
            lk++;
        }

        pi = lk * 4.0 / i; // Calculate pi at each iteration

        outFile << pi << endl; // Save pi to the file
    }

    outFile.close(); // Close the file after the loop

    // Measure the end time
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);

    cout << "The values of pi have been written to 'pi_values.dat'." << endl;
    cout << "Execution time: " << duration.count() << " milliseconds." << endl;

    return 0;
}
