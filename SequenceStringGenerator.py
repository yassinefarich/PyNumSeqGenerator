__author__ = 'Yassine FARICH'
__version__ ='alpha 1.0'
__license__ = "GPL"
__email__ = "yassinefarich@gmail.com"


STRING_DATA ="Hello [1:2|3] Word [4:5|2] How are you [70:75|3] "

def test_sequence_generator() :
    import HSequencesGen.Generator as Generator
    generated_list = Generator.generate_sequence(STRING_DATA)
    print("Generated items : {}".format(len(generated_list)))
    for generated_item in generated_list :
        print (generated_item[0])

if __name__ == '__main__':
    test_sequence_generator()

