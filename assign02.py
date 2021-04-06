import subprocess
import glob

def getGrade(score):
	grade = 0

	if score == 0:
		grade = 10
	elif score > 0 and score <= 35:
		grade = 30
	elif score > 35 and score <= 50:
		grade = 57
	elif score > 50 and score <= 60:
		grade = 67
	elif score > 60 and score <= 70:
		grade = 77
	elif score > 70 and score <= 80:
		grade = 87
	elif score > 80 and score <= 90:
		grade = 92
	elif score > 90 and score <= 95:
		grade = 97
	elif score > 95 and score < 100:
		grade = 99
	else:
		grade = 100

	return grade

scores = open("assign02-scores.txt", "a+")

testCase = ['PRINT hello', 'PRINT "hello world"', 'PRINT "hello" #this prints hello', 'PRINT ", world."', 'PRINT "12.5"', 'PRINT       "yes       "', 'PRINT "NO!"           #"prints no"', 'PRINT "I am       very           sleepy"', 'PRINTLN hello', 'PRINTLN "hello world"', 'PRINTLN "hello" #this prints hello', 'PRINTLN ", world."', 'PRINTLN "12.5"', 'PRINTLN       "yes       "', 'PRINTLN "NO!"           #"prints no"', 'PRINTLN "I am       very           sleepy"', '#Heyow', 'ADD 1 1','ADD 4 5', 'ADD 1.1 -1.1', 'ADD 2 2 2', 'ADD -10 +20', 'ADD 0 0', 'ADD -1 100000000000000000000000000000000000000', 'ADD -100000000000000000000000000000000000000 1', 'SUB 1 1', 'SUB 4 5', 'SUB 1.1 -1.1', 'SUB 2 2 2', 'SUB -10 +20', 'SUB 0 0', 'SUB -1 100000000000000000000000000000000000000', 'SUB -100000000000000000000000000000000000000 1', 'MUL 1 1', 'MUL 4 5', 'MUL 1.1 -1.1', 'MUL 2 2 2', 'MUL -10 +20', 'MUL 0 0', 'MUL -1 100000000000000000000000000000000000000', 'MUL -100000000000000000000000000000000000000 1', 'DIV 1 1', 'DIV 4 5', 'DIV 1.1 -1.1', 'DIV 2 2 2', 'DIV -10 +20', 'DIV 0 0', 'DIV -1 100000000000000000000000000000000000000', 'DIV -100000000000000000000000000000000000000 1', 'MOD 1 1', 'MOD 4 5', 'MOD 1.1 -1.1', 'MOD 2 2 2', 'MOD -10 +20', 'MOD 0 0', 'MOD -1 100000000000000000000000000000000000000', 'MOD -100000000000000000000000000000000000000 1']

noOfCases = len(testCase)

answerKey = ['Syntax is incorrect.\\n', 'hello world\\n', 'hello\\n', ', world.\\n', '12.5\\n', 'yes       \\n', 'NO!\\n', 'I am       very           sleepy\\n', 'Syntax is incorrect.\\n', 'hello world\\n\\n', 'hello\\n\\n', ', world.\\n\\n', '12.5\\n\\n', 'yes       \\n\\n', 'NO!\\n\\n', 'I am       very           sleepy\\n\\n', '\\n', '2\\n', '9\\n', 'Syntax is incorrect.\\n', 'Syntax is incorrect.\\n', '10\\n', '0\\n', '99999999999999999999999999999999999999\\n', '-99999999999999999999999999999999999999\\n', '0\\n', '-1\\n', 'Syntax is incorrect.\\n', 'Syntax is incorrect.\\n', '-30\\n', '0\\n', '-100000000000000000000000000000000000001\\n', '-100000000000000000000000000000000000001\\n', '1\\n', '20\\n', 'Syntax is incorrect.\\n', 'Syntax is incorrect.\\n', '-200\\n', '0\\n', '-100000000000000000000000000000000000000\\n', '-100000000000000000000000000000000000000\\n', '1\\n', '0\\n', 'Syntax is incorrect.\\n', 'Syntax is incorrect.\\n', '-1\\n', 'Error: Division by zero\\n', '-1\\n', '-100000000000000000000000000000000000000\\n', '0\\n', '4\\n', 'Syntax is incorrect.\\n', 'Syntax is incorrect.\\n', '10\\n', 'Error: Division by zero\\n', '99999999999999999999999999999999999999\\n', '0\\n']

print(len(answerKey))
path='assign02'
files = [f for f in glob.glob(path + "**/*02.py", recursive=False)]


for f in files:
	i = 0
	score = 0

	fnameIndex = f.find('/') + 1;
	firstIndex = f.find('-') + 1;
	secondIndex = f[firstIndex:].find('-') + firstIndex;
	fname = f[fnameIndex:firstIndex-1]

	outfile = "assign02-feedback/"+ f[firstIndex:secondIndex] + "-" + fname + ".txt"
	out = open(outfile, "w")

	for case in testCase:
		print(i, case)
		currCase = open("currCase", "w")
		currCase.write("BEGIN\n" + case + "\nEND")
		currCase.close()

		try:
			command = 'python3 ' + f + '< currCase | grep -v "Syntax correct\|INTERPOL\|Starting\|Ending\|Enter\|Exit\|Beginning\|Goodbye\|syntax checker\|Fitzgerald\|BEGIN\|END"'
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

			outstr = "Test  Case " + str(i+1) + ": " + case + "\nYour  Answer: " + strOutput + "\nRight Answer: " + answerKey[i] + "\n\n"
			out.write(outstr)

			ansKey = answerKey[i].lower()
			strOutput = strOutput.lower()

			if (strOutput.find(ansKey) > -1) or ( strOutput.find("none") > -1 and ansKey.find("incorrect") > -1 ) or (strOutput.find("incorrect") > -1 and ansKey.find("incorrect") > -1 ) or ( strOutput.find("error") > -1 and ansKey.find("error") > -1 ) or ( strOutput.find("error") > -1 and ansKey.find("incorrect") > -1 ) or ( strOutput.find("incorrect") > -1 and ansKey.find("error") > -1 ):
				score = score + 1
				#print(ansKey, strOutput)

			#print(outstr)
			#print(score)

		except subprocess.CalledProcessError:
			strOutput = '\\n'
			if answerKey[i] == strOutput:
				score = score + 1
				outstr = "Test  Case " + str(i+1) + ": " + case + "\nYour  Answer: " + strOutput + "\nRight Answer: " + answerKey[i] + "\n\n"
				out.write(outstr)

		except:
			out.write("Test  Case " + str(i+1) + ": " + case + "\n")
			out.write("Exception encountered.\n\n")

		i = i + 1
	

	out.write("Score:\t" + str(score) + " / " + str(noOfCases))	
	out.close()

	outstr = f[firstIndex:secondIndex] + ", " + fname + "\t" + str(getGrade(100*(score/noOfCases))) + "\n"
	scores.write(outstr)

scores.close()
