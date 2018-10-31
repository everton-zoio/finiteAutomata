# Linha 1: alfabeto de entrada
# Linha 2: simbolo que representa epsilon (padrão: E)
# Lista 3: conjunto de estados
# Linha 4: estado inicial
# Linha 5: conjunto de estados de aceitacao
# Linhas 6 em diante: transicoes, uma por linha, no formato estado atual, simbolo atual da palavra e novo estado

from xml.etree import ElementTree as ET
import csv
import sys

class Transition(object):
	def __init__(self):
		self.currentState = None
		self.currentWordSymbol = None
		self.newState = None

	def __lt__(self, other):
		if self.currentState != other.currentState:
			return self.currentState < other.currentState
		if self.currentWordSymbol != other.currentWordSymbol:
			return self.currentWordSymbol < other.currentWordSymbol
		if self.newState != other.newState:
			return self.newState < other.newState 

class Jflap2Utfpr(object):
	def __init__(self):
		self.state_id_to_name = {}
		self.inputAlphabet = set()
		self.states = set()
		self.initialStates = set()
		self.acceptingStates = set()
		self.transitions = []
		self.blankSymbol = "E"

	def convert(self, inputFile, outputFile, blankSymbol = "E", inputAlphabet = None, states = None):
		self.blankSymbol = blankSymbol
		if inputAlphabet is not None:
			self.inputAlphabet = inputAlphabet
		if states is not None:
			self.states = states

		xmldoc = ET.parse(inputFile)
		root = xmldoc.getroot()
		tm = root.find('automaton')

		for s in tm.findall('state'):
			state_id = s.attrib['id']
			state_name = s.attrib['name']
			self.state_id_to_name[state_id] = state_name
			self.states.add(state_name)
			if s.find('initial') is not None:
				self.initialStates.add(state_name)
			if s.find('final') is not None:
				self.acceptingStates.add(state_name)

		# Discover input alphabet:
		if inputAlphabet is None:
			for t in tm.findall('transition'):
				if t.find('read').text is not None:
					self.inputAlphabet.add(t.find('read').text)

		# Use a symbol to represent epsilon that is not used by the input or stack alphabets
		fullAlphabet = set()
		fullAlphabet.union(self.inputAlphabet)
		for s in fullAlphabet:
			if s == blankSymbol:
				oldBlankSymbol = blankSymbol
				for c in ascii_uppercase:
					if c not in fullAlphabet:
						blankSymbol = c
						break
				print("Simbolo escolhida para representar branco (" + oldBlankSymbol + ") foi utilizado para outros fins no automato. Simbolo para branco foi substituido por " + blankSymbol + ".")
		self.blankSymbol = blankSymbol
		
		for t in tm.findall('transition'):
			transition = Transition()
			self.transitions.append(transition)
			transition.currentState = self.state_id_to_name[t.find('from').text]
			if t.find('read').text is not None:
				transition.currentWordSymbol = t.find('read').text
			else:
				transition.currentWordSymbol = self.blankSymbol
			transition.newState = self.state_id_to_name[t.find('to').text]
			
		self.transitions.sort()
		
		with open(outputFile, 'w') as csvfile:
			writer = csv.writer(csvfile, delimiter = ' ', escapechar = None, quotechar = None, quoting = csv.QUOTE_NONE, skipinitialspace = True)
			writer.writerow(set2list(self.inputAlphabet))
			writer.writerow(self.blankSymbol)
			writer.writerow(set2list(self.states))
			writer.writerow(set2list(self.initialStates))
			writer.writerow(set2list(self.acceptingStates))
			for t in self.transitions:
				writer.writerow([t.currentState, t.currentWordSymbol, t.newState])


def set2list(dataset):
	sortedList = list(dataset)
	sortedList.sort()
	return sortedList
	

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Parametros insuficientes. Informe o nome de arquivo de entrada e o nome do arquivo de saida")
		sys.exit(1)
	converter = Jflap2Utfpr()
	converter.convert(sys.argv[1], sys.argv[2], "E")

