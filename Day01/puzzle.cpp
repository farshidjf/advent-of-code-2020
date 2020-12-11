#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

long puzzle1(const vector<int>& input) {
    int n = input.size();
    for (int j, i = 0; i < n; ++i)
        for (j = i; j < n; ++j)
            if (input[i] + input[j] == 2020)
                return input[i] * input[j];
    return -1;
}

long puzzle2(const vector<int>& input) {
    int n = input.size();
    for (int k, j, i = 0; i < n; ++i)
        for (j = i; j < n; ++j)
            for (k = j; k < n; ++k)
                if (input[i] + input[j] + input[k] == 2020)
                    return input[i] * input[j] * input[k];
    return -1;
}

vector<int> read_input_from_file(const string& file_name) {
    ifstream input_file(file_name);
    vector<int> input;
    int temp;
    while (true) {
        input_file >> temp;
        if (input_file.eof()) break;
        input.push_back(temp);
    }
    input_file.close();
    return input;
}

int main() {
    string folder_name = "./Day1/";
    vector<string> file_names = {"small_input", "large_input"};
    for (auto&& file_name: file_names) {
        auto input = read_input_from_file(folder_name + file_name);
        cout << "Puzzle 1 - " << file_name << ": " << puzzle1(input) << endl;
        cout << "Puzzle 2 - " << file_name << ": " << puzzle2(input) << endl;
    } 
    return 0;
}