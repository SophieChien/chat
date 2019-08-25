def read_file(filename):
	lines=[]
	with open(filename, 'r', encoding='utf-8-sig') as f: # -sig: 消除\ufeff
		for line in f:
			lines.append(line.strip())  # .strip(): 消除\n	
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:		
		if line == 'Sophie':
			person = 'Sophie'
			continue
		elif line == 'Cliff':
			person = 'Cliff'
			continue
		if person:
			new.append(person + ':' + line)
	return new
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():	
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)
main() #程式的進入點



		