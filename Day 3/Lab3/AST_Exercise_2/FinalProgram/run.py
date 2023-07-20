import sys, os
from utils import *

TARGET = "../CompiledLanguage"


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif len(argv) < 3:
        if os.path.isdir(TARGET) and not TARGET in sys.path:
            sys.path.append(TARGET)

        from Exercise2Lexer import Exercise2Lexer
        from Exercise2Parser import Exercise2Parser

        inputFile = argv[0]

        if len(argv) == 1:
            outputFile = "result.txt"
        else:
            outputFile = argv[1]

        checkAST(Exercise2Lexer, Exercise2Parser, inputFile, outputFile)

    else:
        printUsage()


def printUsage():
    print("python run.py TESTCASE_FILE [OUTPUT_FILE]")


if __name__ == "__main__":
    main(sys.argv[1:])
