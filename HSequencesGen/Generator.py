__author__ = 'Yassine FARICH'
__version__ ='alpha 1.0'
__license__ = "GPL"
__email__ = "yassinefarich@gmail.com"

import re
#import logging
import copy
"""

    Sequence numbers generator module for python 3
    Example : for string = "Hello [1:2|3] Word [4:5|2] How are you [70:75|3] "
                the result will be :
                                Hello 001 Word 04 How are you 070
                                            ........
                                Hello 002 Word 05 How are you 073
                                Hello 002 Word 05 How are you 074
                                Hello 002 Word 05 How are you 075


"""

"""
The Source string generation datas regex :
 Example : My first [1:12|2] ...
                    [start:end|digits]
"""
LinkRegex = r'\[[0-9]+\:[0-9]+\|[0-9]]'
ExprRegex1 = r'([0-9]+\:)'
ExprRegex2 = r'(\:[0-9]+)'
ExprRegex3 = r'(\|[0-9])'

"""
Parse starting string to find where the number generation will
    be modified (where the string will be replaced )
    Example for " My [1:3|5] " the result will be "{1:3|5]

"""
def list_parse_global_expressions(link,regular_expr=LinkRegex):
    object_found=re.findall( regular_expr, link, re.M|re.I)
    return object_found

"""
Find more details about the generation

    @:return ( start_number,end_sequence_number,number_of_digits )

"""
def find_details_expression(elem,start_expression=ExprRegex1,middle_expression=ExprRegex2,last_expression=ExprRegex3):
    start = re.search(start_expression, elem, re.M|re.I).group()
    end = re.search(middle_expression, elem, re.M|re.I).group()
    size = re.search(last_expression , elem, re.M|re.I).group()
    return clean_data(start), clean_data(end), clean_data(size)

"""
Cleaning Data list before start generation

"""

def clean_list(list_expression):
    data_list=[];
    for expression_iter in list_expression :
        data = find_details_expression(expression_iter);
        if data[1] < data[0]:
            print ("Cleaning link data expression [a:b|c] 'a' must be less than 'b' ")
            data = data[1],data[0],data[2]
        data_list.append(data)
    return data_list;

def clean_data(str_data):
    accumulator = ''
    for var in str_data:
        if (var <= '9' and var >='0'):
            accumulator += var
    return int(accumulator)


"""
Replace source string with identifiers
to make yhe parsing easy

replace expression with identifier
"""

def replace_expression(strng,elements):
    index = 0 ;
    for var in elements :
        newstr = "[[$"+str(index)+"]]";
        strng=strng.replace(var,newstr,1)
        index += 1 ;
    return strng


"""
Replace source string with identifiers
to make yhe parsing easy

replace identifier with number
"""


def replace_expr_hiarch(string_repl,data,hiarch):
    new_string = data;
    old_string = "[[$"+str(hiarch)+"]]";
    strng = string_repl.replace(old_string,new_string,1);
    return strng


"""
Generate full sequence list

"""
def generate_result_list(data):
    num_liste=[]
    if len(data) == 1 :
        for nums in range(0,data[0]+1):
            num_liste.append(str(nums).zfill(data[2]))
    else :
        for nums in range(data[0],data[1]+1):
            num_liste.append(str(nums).zfill(data[2]))
    return num_liste


"""
Recursive generation tree

"""
def recursive_generation_tree(list_data,tree_level,sting_view,list_Accumulaor,data_Accumulator):
    tempo_data = list_data[tree_level]
    num_liste = generate_result_list(tempo_data)
    for vari in num_liste :
        CalcHiear = len(list_data) - tree_level - 1
        string_v = replace_expr_hiarch(sting_view,vari,CalcHiear)

        if len(list_Accumulaor) > CalcHiear :
           list_Accumulaor[CalcHiear] = vari
        else :
           list_Accumulaor.append(vari)

        if(tree_level > 0):
            recursive_generation_tree(list_data,tree_level-1,string_v,list_Accumulaor,data_Accumulator)
        else :
            data_Accumulator.append((string_v,copy.copy(list_Accumulaor)))

    return


"""
Main generation function
"""

def generate_sequence(global_link):

    list_expressions = list_parse_global_expressions(global_link)
    #logging.info("FOUND "+str(len(list_expressions))+" EXPRESSION ")
    newLink = replace_expression(global_link,list_expressions)
    data_list=clean_list(list_expressions)
    data_list.reverse()
    h=len(data_list)-1
    Data_Accumulator=[]
    list_Accumulaor = []
    #logging.info("### START RECURSIVE GENERATION _TREE ")
    recursive_generation_tree(data_list,h,newLink,list_Accumulaor,Data_Accumulator)
    #logging.info("### END RECURSIVE GENERATION _TREE ")
    return Data_Accumulator