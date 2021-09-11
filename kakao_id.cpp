#include <iostream>
#include <vector>
using namespace std;

string solution(string new_id) {
	string answer = new_id;

	//step 1
	for (int i = 0; i < answer.length(); i++) {
		char ch = answer[i];
		if ('A' <= ch && ch <= 'Z')
			answer[i] = ch - ('A' - 'a');
	}

	//step 2
	for (int i = 0; i < answer.length(); i++) {
		char ch = answer[i];
		if (('a' <= ch && ch <= 'z') || ('0' <= ch && ch <= '9') || ch == '-' || ch == '_' || ch == '.') {

		}
		else {
			answer.erase(i, 1);
			i--;
		}

	}

	//step 3
	for (int i = 0; i < answer.length(); i++) {
		char ch = answer[i];
		if (ch == '.') {
			for (int j = i + 1; answer[j] == '.'; j++) {
				answer.erase(j, 1);
				j--;
			}
			
		}

	}

	//step 4
	if (answer[0] == '.') answer.erase(0, 1);
	if (!answer.empty()) {
		if (answer[answer.length() - 1] == '.')
			answer.erase(answer.length() - 1, 1);
	}

	//step 5
	if (answer.empty()) answer = "a";

	//step 6
	if (answer.length() >= 16) answer.erase(15);
	if (answer[answer.length() - 1] == '.') answer.erase(answer.length() - 1, 1);

	//step 7
	if (answer.length() <= 2) {
		char last = answer[answer.length() - 1];
		while (answer.length() != 3)
			answer+=last;
	}
	
	return answer;
}

int main() {
	string str="=.=";
	printf("%s\n", solution(str).c_str());

}