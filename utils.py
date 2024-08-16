#import regex and OCR library
import re
import pdfplumber

#define global variable for multiplying by unit values
MULTIPLIERS = {"million": 1000000, "billion": 1000000000}

#get all numbers from a page and apply unit defined in some tables using regex

def get_table_numbers(text, unit):
    numbers = re.findall('[1-9][0-9.,]+', text)
    numbers = parse_table_numbers(numbers, unit)
    return numbers

#applies unit value to relevant numbers 
def parse_table_numbers(numbers, unit):
    parsed_numbers = []
    for n in numbers:
        try:
            num = eval(n.replace(",",""))
            if type(num) is float:
                num = apply_unit_multiplier(num, unit)
                parsed_numbers.append(num)
            else:
                parsed_numbers.append(num)
        except:
            continue

    return parsed_numbers

#get individual numbers and units from text using regex
def get_text_numbers(text):
    numbers = re.findall('[0-9.,]+ [a-z|A-Z]illion', text)
    numbers = parse_text_numbers(numbers)
    return numbers

#converts numbers into numerical representation based on unit of original number
def parse_text_numbers(numbers):
    parsed_numbers = []
    for n in numbers:
        num, unit = n.split()
        parsed_num = apply_unit_multiplier(eval(num.replace(",","")), unit)
        parsed_numbers.append(parsed_num)
    
    return parsed_numbers
    
#gets the units from pages/tables where certain values are in a different unit
def get_units(text):
    units = re.findall('\\$ .*illions|[d,D]ollars in .*illions|\\$[A-Z]', text)
    unit = "none"
    for i in units:
        if "M" in i:
            unit = "million"
        elif "B" in i:
            unit = "billion"
    return unit
    
#applies the unit multiplier to base numbers
def apply_unit_multiplier(num, unit):
    if unit not in MULTIPLIERS.keys():
        return num
    else:
        multiplier = MULTIPLIERS.get(unit.lower())
        return num * multiplier

#extracts the largest number from the document using NLP guidance as explained in the bonus challenge of description
def extract_largest_adv(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    page_max = []
    for p in pdf.pages:
        
        text = p.extract_text(keep_blank_chars=True)
        unit = get_units(text)
        tab_numbers = get_table_numbers(text, unit)
        text_numbers = get_text_numbers(text)

        if tab_numbers != [] and text_numbers != []:
            max_num = max( max(tab_numbers), max(text_numbers) )
        elif tab_numbers != []:
            max_num = max(tab_numbers)
        elif text_numbers != []:
            max_num = max(text_numbers)
        else:
            max_num = -1

        if max_num > -1:
            page_max.append(max_num)
        
    return max(page_max)
        

#simple regex and processing to get all numbers from page with no care for units
def get_numbers_basic(text):
    numbers = re.findall('[1-9][0-9.,]+', text)
    clean_numbers = []
    for n in numbers:
        try:
            num = eval(n.replace(",", ""))
            clean_numbers.append(num)
        except:
            continue

    return clean_numbers

#extracts the largest number from pdf with no care for units
def extract_largest_basic(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    page_max = []
    for p in pdf.pages:
        
        text = p.extract_text(keep_blank_chars=True)
        numbers = get_numbers_basic(text)
        if numbers != []:
            page_max.append(max(numbers))

    return max(page_max)
