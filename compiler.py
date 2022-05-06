### author_name, student_no = 'Amir Afsari', 96105575
### student_no = 'Hamed Khanaki', 96105712

from scanner import Scanner 
from parser import Parser
from parse_table import parse_table


scanner = Scanner("./input.txt")
parser = Parser(scanner, parse_table)

parser.parse()
