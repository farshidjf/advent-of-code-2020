#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using std::string;
using std::vector;

struct Policy {
    int first;
    int second;
    char letter;
    Policy(const string& str) {
        auto pos1 = str.find_first_of('-');
        first = stoi(str.substr(0, pos1));
        auto pos2 = str.find_first_of(' ');
        second = stoi(str.substr(pos1+1, pos2-pos1-1));
        letter = str[pos2+1];
    }
};

bool check_policy1 (const Policy& policy, const string& str) {
    auto count = std::count(begin(str), end(str), policy.letter);
    return ((policy.first <= count) && (count <= policy.second));
}

bool check_policy2 (const Policy& policy, const string& str) {
    return (str[policy.first-1] == policy.letter) != (str[policy.second-1] == policy.letter);
}

vector<string> read_input_from_file(const string& file_name) {
    vector<string> input;
    std::ifstream input_file(file_name);
    string temp;
    while(std::getline(input_file, temp))
        input.push_back(temp);
    return input;    
}

auto analyze = [] (const vector<string>& input, auto check_policy) {
    int count = 0;
    for (auto&& line: input) {
        auto pos = line.find_first_of(':');
        Policy policy(line.substr(0, pos));
        string password = line.substr(pos+2);
        if (check_policy(policy, password)) ++count;
    }
    return count;
};

int main() {
    string folder_name = "./Day2/";
    vector<string> file_names = {"small_input", "large_input"};
    for (auto&& file_name: file_names) {
        auto input = read_input_from_file(folder_name + file_name);
        std::cout << "Puzzle 1 - " << file_name << ": " << analyze(input, check_policy1) << std::endl;
        std::cout << "Puzzle 2 - " << file_name << ": " << analyze(input, check_policy2) << std::endl;
    }
    return 0;
}