import pickle
from itertools import zip_longest

from src.Utils import isStrEmpty, extractPathExtension


class ObfuscatorController:

    def __init__(self, view):
        self.view = view

    def obfuscateAction(self):

        self.view.enableObfuscateBtn(False)

        filePaths = self.view.getFilePaths()
        references = self.view.getReferences()
        stringA = self.view.getStringA()
        stringB = self.view.getStringB()
        shouldMinifyCode = self.view.shouldMinifyCode
        shouldSaveDecoder = self.view.shouldSaveDecoder
        path = None

        if isStrEmpty(stringA) or isStrEmpty(stringB) or len(references) == 0:
            self.view.enableObfuscateBtn(True)
            return

        if shouldSaveDecoder:
            path = self.view.requestFilePathToUsetToSaveDecoderFile()
            if path is None:
                return

        referencesDictionary = self.createReferencesDictionary(stringA, stringB, references)

        self.obfuscateFiles(filePaths, referencesDictionary, references, shouldMinifyCode)

        if shouldSaveDecoder:
            self.saveDecoderFile(path, referencesDictionary)  # type: ignore

        self.view.enableObfuscateBtn(True)

    def obfuscateFiles(self, filePaths: list, referencesDictionary: dict, references: list, shouldMinifyCode: bool):

        for filePath in filePaths:
            self.obfuscateFile(filePath, referencesDictionary, references, shouldMinifyCode)

    def obfuscateFile(self, filePath: str, referencesDictionary: dict, references: list, shouldMinifyCode: bool):
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

        obfuscatedFile.write(fileContent)
        obfuscatedFile.close()

    def createReferencesDictionary(self, stringA: str, stringB: str, references: list) -> dict:
        # sort references
        references = sorted(references, reverse=True, key=lambda ref: len(ref))
        combinations = self.generateCombinations(len(references), stringA, stringB)
        return self.buildReferencesDictionary(references, combinations)

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

    def saveDecoderFile(self, path: str, referencesDictionary: dict):

        binarySerialization = pickle.dumps(referencesDictionary)

        decoderFile = open(path, 'wb')
        decoderFile.write(binarySerialization)
        decoderFile.close()

    def deobfuscateAction(self):
        self.view.enableDeobfuscateBtn(False)

        filePaths = self.view.getFilePaths()
        decoderFilePath = self.view.getDecoderFilePath()

        references: dict = self.loadReferences(decoderFilePath)

        self.deobfuscateFiles(filePaths, references)

        self.view.enableDeobfuscateBtn(True)

    def loadReferences(self, decoderFilePath: str) -> dict:
        binarySerialization = open(decoderFilePath, 'rb').read()
        references: dict = pickle.loads(binarySerialization)
        return references

    def deobfuscateFiles(self, filePaths: list, referencesDictionary: dict):
        for filePath in filePaths:
            self.deobfuscateFile(filePath, referencesDictionary)

    def deobfuscateFile(self, filePath: str, references: dict):
        originalFile = open(filePath, 'r')
        fileContent = originalFile.read()
        originalFile.close()

        extension = extractPathExtension(filePath)
        obfuscatedFile = open(filePath.replace(extension, '') + '.deobf' + extension, 'w')

        for referenceKey in references.keys():
            if fileContent.find(references[referenceKey]) != -1:
                fileContent = fileContent.replace(references[referenceKey], referenceKey)

        obfuscatedFile.write(fileContent)
        obfuscatedFile.close()