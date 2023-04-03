from itertools import zip_longest

from src.Utils import isStrEmpty, extractPathExtension


class ObfuscatorController:

    def __init__(self, view):
        self.view = view

    def obfuscateAction(self):
        filePaths = self.view.getFilePaths()
        references = self.view.getReferences()
        stringA = self.view.getStringA()
        stringB = self.view.getStringB()
        shouldMinifyCode = self.view.getShouldMinifyCode()

        if isStrEmpty(stringA) or isStrEmpty(stringB) or len(references) == 0:
            return

        self.obfuscateFiles(filePaths, references, stringA, stringB, shouldMinifyCode)

    def obfuscateFiles(self, filePaths: list, references: list, stringA: str, stringB: str, shouldMinifyCode: bool):

        #sort references
        references = sorted(references, reverse=True, key=lambda ref: len(ref))

        combinations = self.generateCombinations(len(references), stringA, stringB)

        for filePath in filePaths:
            self.obfuscateFile(filePath, combinations, references, shouldMinifyCode)

    def obfuscateFile(self, filePath: str, combinations: list, references: list, shouldMinifyCode: bool):

        referencesDictionary = self.buildReferencesDictionary(references, combinations)

        originalFile = open(filePath, 'r')
        fileContent = originalFile.read()
        originalFile.close()

        extension = extractPathExtension(filePath)
        obfuscatedFile = open(filePath.replace(extension, '') + '.obf' + extension, 'w')

        for reference in references:
            if fileContent.find(reference) != -1:

                fileContent = fileContent.replace(reference, referencesDictionary[reference])

                if shouldMinifyCode:
                    fileContent = fileContent.replace('\n', '')
                else:
                    fileContent = fileContent.replace('\n\n', '\n')

        obfuscatedFile.write(fileContent)
        obfuscatedFile.close()

    def buildReferencesDictionary(self, references: list, combinations: list) -> dict:
        dic = {}
        for reference, comb in zip_longest(references, combinations):

            if reference is None or combinations is None:
                break

            dic[reference] = comb
        return dic

    def generateCombinations(self, nReferences: int, stringA: str, stringB: str) -> list:
        exponent = self.calculateBinaryExponent(nReferences)
        combinations = []
        for i in range(0, 2 ** exponent):
            binaryString = bin(i)[2:].zfill(exponent)
            combString = binaryString.replace('0', stringA)
            combString = combString.replace('1', stringB)
            combinations.append(combString)
        return combinations

    def calculateBinaryExponent(self, nReferences: int) -> int:
        nCombs = 0
        exp = 0
        while nCombs < nReferences:
            exp += 1
            nCombs = 2 ** exp
        return exp
