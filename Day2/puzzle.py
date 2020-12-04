"""
Puzzle 1:
They have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

How many passwords are valid according to their policies?

Puzzle 2:
Each policy describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

How many passwords are valid according to the new interpretation of the policies?
"""

def parse_line(line):
    (policy, password) = line.split(': ')
    (policy_range, policy_letter) = policy.split(' ')
    (policy_min, policy_max) = policy_range.split('-')
    return (int(policy_min), int(policy_max), policy_letter, password)

# for puzzle 1
def is_valid1(line):
    policy_min, policy_max, policy_letter, password = parse_line(line)
    count = password.count(policy_letter)
    return policy_min <= count <= policy_max

# for puzzle 2
def is_valid2(line):
    policy_min, policy_max, policy_letter, password = parse_line(line)
    count = 0
    if (password[policy_min-1] == policy_letter) ^ (password[policy_max-1] == policy_letter):
        return True
    return False


def evaluate_file(file_content, is_valid):
    return len([1 for line in file_content.splitlines() if is_valid(line)])

if __name__ == "__main__":
  with open('./Day2/small_input') as small_file:
    content = small_file.read();
    num_valid1 = evaluate_file(content, is_valid1)
    num_valid2 = evaluate_file(content, is_valid2)
    print("Puzzle 1 - small input: ", num_valid1)
    print("Puzzle 2 - small input: ", num_valid2)
    
  with open('./Day2/large_input') as large_file:
    content = large_file.read();
    num_valid1 = evaluate_file(content, is_valid1)
    num_valid2 = evaluate_file(content, is_valid2)
    print("Puzzle 1 - large input: ", num_valid1)
    print("Puzzle 1 - large input: ", num_valid2)
