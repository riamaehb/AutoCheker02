import subprocess
import glob

def getGrade(score):
	grade = 0

	if score == 0:
		grade = 0
	elif score > 0 and score < 21:
		grade = 30
	elif score > 20 and score < 41:
		grade = 40
	elif score > 40 and score < 51:
		grade = 50
	elif score > 50 and score < 56:
		grade = 55
	elif score > 55 and score < 61:
		grade = 60
	elif score > 60 and score < 66:
		grade = 65
	elif score > 65 and score < 71:
		grade = 70
	elif score > 70 and score < 76:
		grade = 75
	elif score > 75 and score < 81:
		grade = 80
	elif score > 80 and score < 86:
		grade = 85
	elif score > 85 and score < 91:
		grade = 90
	elif score > 90 and score < 95:
		grade = 95
	elif score > 94 and score < 98:
		grade = 97
	elif score > 97 and score < 100:
		grade = 99
	else:
		grade = 100

	return grade

def main():

	scores = open("assign01-scores.txt", "a+")

	testCase = ['begin', 'PRINT', 'PRINT hello', 'PRINT "hello world"', 'PRINT 1234.5', 'PRINT "hello" #this prints hello', 'PRINT ", world."', 'PRINT "12.5"', 'PRINT "リア"', 'PRINT       "yes       "', 'PRINT "NO!"           #"prints no"', 'print "hello world"', 'PRINTLN', 'PRINTLN hello', 'PRINTLN "hello world"', 'PRINTLN 1234.5', 'PRINTLN "hello" #this prints hello', 'PRINTLN ", world."', 'PRINTLN "12.5"', 'PRINTLN "リア"', 'PRINTLN       "yes       "', 'PRINTLN "NO!"           #"prints no"', 'println "hello world"', 'ADD 1 2 3', 'ADD 1 2 a', 'ADD 1 2', 'ADD 12.5 2', 'ADD 12.4 4.4', 'ADD 12 2.2', 'ADD 0 0', 'ADD    1 2', 'ADD x y', 'add 12 m', 'SUB 1 2 3', 'SUB 1 2 a', 'SUB 1 2', 'SUB 12.5 2', 'SUB 12.4 4.4', 'SUB 12 2.2', 'SUB 0 0', 'SUB    1 2', 'SUB x y', 'SUB 12 m', 'sub 12 1', 'MUL 1 2 3', 'MUL 1 2 a', 'MUL 1 2', 'MUL 12.5 2', 'MUL 12.4 4.4', 'MUL 12 2.2', 'MUL 0 0', 'MUL    1 2', 'MUL x y', 'MUL 12 m', 'mul 3 4', 'DIV 1 2 3', 'DIV 1 2 a', 'DIV 1 2', 'DIV 12.5 2', 'DIV 12.4 4.4', 'DIV 12 2.2', 'DIV 0 0', 'DIV    1 2', 'DIV x y', 'DIV 12 m', 'div 5 6', 'MOD 1 2 3', 'MOD 1 2 a', 'MOD 1 2', 'MOD 12.5 2', 'MOD 12.4 4.4', 'MOD 12 2.2', 'MOD 0 0', 'MOD    1 2', 'MOD x y', 'MOD 12 m', 'mod 1 2', 'end']

	answerKey = ['incorrect', 'incorrect', 'incorrect', ' correct', 'incorrect', ' correct', ' correct', ' correct', 'incorrect', ' correct', ' correct', 'incorrect', 'incorrect', 'incorrect', ' correct', 'incorrect', ' correct', ' correct', ' correct', 'incorrect', ' correct', ' correct', 'incorrect', 'incorrect', 'incorrect', ' correct', 'incorrect', 'incorrect', 'incorrect', ' correct', ' correct', 'incorrect', 'incorrect', 'incorrect', 'incorrect', ' correct', 'incorrect', 'incorrect', 'incorrect', ' correct', ' correct', 'incorrect', 'incorrect', 'incorrect', 'incorrect', 'incorrect', ' correct', 'incorrect', 'incorrect', 'incorrect', ' correct', ' correct', 'incorrect', 'incorrect', 'incorrect', 'incorrect', 'incorrect', ' correct', 'incorrect', 'incorrect', 'incorrect', ' correct', ' correct', 'incorrect', 'incorrect', 'incorrect', 'incorrect', 'incorrect', ' correct', 'incorrect', 'incorrect', 'incorrect', ' correct', ' correct', 'incorrect', 'incorrect', 'incorrect', 'incorrect']

	noOfCases = len(testCase)

	path='assign01'
	files = [f for f in glob.glob(path + "**/*01.py", recursive=False)]


	for f in files:
		i = 0
		score = 0

		fnameIndex = f.find('/') + 1;
		firstIndex = f.find('-') + 1;
		secondIndex = f[firstIndex:].find('-') + firstIndex;
		fname = f[fnameIndex:firstIndex-1]

		outfile = "assign01-feedback/"+ f[firstIndex:secondIndex] + "-" + fname + ".txt"
		out = open(outfile, "w")

		for case in testCase:
			currCase = open("currCase", "w")
			currCase.write("BEGIN\n" + case + "\nEND")
			currCase.close()

			try:
				command = 'python3 ' + f + '< currCase | grep -v "INTERPOL\|Starting\|Ending\|Enter\|Exit\|Beginning\|Goodbye\|syntax checker\|Fitzgerald\|BEGIN\|END"'
				output = subprocess.check_output(command, shell=True)

				strOutput = str(output).replace("b'$", "", 1)
				strOutput = strOutput.replace('b"$', "", 1)
				strOutput = strOutput.replace("b'", "", 1)
				strOutput = strOutput.replace('b"', "", 1)
				strOutput = strOutput.replace("$ \\n", "", 1)
				strOutput = strOutput.replace("\\n\\n\\n$  ", "", 1)
				strOutput = strOutput.replace("\\n'", "\\n").lstrip()

				if strOutput.find("\\n") == 0:
					strOutput = strOutput[2:]

				outstr = "Test    Case: " + case + "\nYour  Answer: " + strOutput + "\nRight Answer: " + answerKey[i] + "\n\n"
				out.write(outstr)

				ansKey = answerKey[i].lower()
				strOutput = strOutput.lower()

				if (strOutput.find(ansKey) > -1) :
					score = score + 1

				#print(outstr)
				#print(score)

			except subprocess.CalledProcessError:
				strOutput = '\\n'
				if answerKey[i] == strOutput:
					score = score + 1
					outstr = "Test    Case: " + case + "\nYour  Answer: " + strOutput + "\nRight Answer: " + answerKey[i] + "\n\n"
					out.write(outstr)

			except:
				out.write("Test    Case: " + case + "\n")
				out.write("Exception encountered.\n\n")

			i = i + 1
			
		out.write("Score:\t" + str(score))
		out.close()

		grade = (score/(len(testCase))*100)

		outstr = f[firstIndex:secondIndex] + ", " + fname + "\t" + str(grade) + "\t" + str(getGrade(grade)) + "\n"
		scores.write(outstr)

	scores.close()

main()
