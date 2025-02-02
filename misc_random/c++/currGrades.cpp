#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

int main() {
	float scores[5];
	int loop = 0;
	float line;
	ifstream gradeFile(".grades.txt");

	if (gradeFile.is_open()) {
		while (!gradeFile.eof()) {
			getline(gradeFile, line);
			scores[loop] = line;
			loop++;
		}
		gradeFile.close();
	}
	else {
		std::cout << "Cannot access grades file." << std::endl;
		exit(EXIT_SUCCESS);
	}

	int subject;
	std::cout << "Select subject. Press:" << std::endl;
	std::cout << "1 - CS 225" << std::endl << "2 - CS 233" << std::endl << "3 - ECON 203" << std::endl << "4 - PHYS 325" << std::endl
		<< "5 - STAT 410" << std::endl << "6 - View Grades" << "Enter here: " << std::flush;
	std::cin >> subject;
	std::cout << "Select assignment. Press:" << std::endl;

	switch(subject) {
		case 1:
			CS225(&scores[0]);
			break;
		case 2:
			CS233(&scores[1]);
			break;
		case 3:
			ECON203(&scores[2]);
			break;
		case 4:
			PHYS325(&scores[3]);
			break;
		case 5:
			STAT410(&scores[4]);
			break;
		case 6:
			std::string outs[5] = {"CS 225: ", "CS 233: ", "ECON 203: ", "PHYS 325: ", "STAT 410: "};
			for (int i = 0; i < scores.size(); i++) { std::cout << out[i] << scores[i] << std::endl; }
			break;
		default:
			std::cout << "Invalid" << std::endl;
			main();
	}
	std::cout << "Total score updated" << std::endl;
	char restart;
	std::cout << "Again?[Y/N] : " << std::flush;
	std::cin >> restart;

	if (restart == 'Y' || restart == 'y') { main(); }
	else if (restart == 'N' || restart == 'n') { exit(EXIT_SUCCESS); }
	else {
		std::cout << "Fine. Be a dick." << std::flush;
		exit(EXIT_SUCCESS);
	}
}

void CS225(float *score) {
	int assignment;
	int addScore;
	std::cout << "1 - MP" << std::endl << "2 - Lab" << std::endl << "3 - Exams" << std::endl << "4 - Extra Credit" << "Enter here:" << std::flush;
	std::cin >> assignment;
	std::cout << "Enter score: " << std::flush;
	std::cin >> addScore;

	switch(assignment) {
		case 1:
			char mp_intro;
			std::cout << "mp_intro?[Y/N] : " << std::flush;
			std::cin >> mp_intro;
			if (mp_intro == 'Y' || mp_intro == 'y') { *score - (20 - addScore); }
			else { *score - (45 - addScore);}
			break;
		case 2:
			*score - (10 - addScore);
			break;
		case 3:
			char exam0;
			char finalExam;
			std::cout << "Exam 0?[Y/N] : " << std::flush;
			std::cin >> exam0;
			if (exam0 == 'Y' || exam0 == 'y') { *score - (40 - addScore); }
			else {
				std::cout << "Final Exam?[Y/N] : " << std:flush;
				std::cin >> finalExam;
				if (finalExam == 'Y' || finalExam == 'y') { *score - (150 - addScore); }
				else { *score - (70 - addScore); }
			}
			break;
		case 4:
			*score + addScore;
	}
}

void CS233(int *score) {
	int assignment;
	int addScore;
	std::cout << "1 - Lab" << std::endl << "2 - HW" << std:endl << "3 - Exams" << std::endl << "4 - Attendance" << "5 - Extra Credit" << "Enter here:" 
		<< std::flush;
	std::cin >> assignment;
	std::cout << "Enter score: " << std::flush;
	std::cin >> addScore;

	switch(assignment) {
		case 1:
			*score - (50/3 - addScore);
			break;
		case 2:
			// "UNDER CONSTUCTION"
			break;
		case 3:
			
	}
}




