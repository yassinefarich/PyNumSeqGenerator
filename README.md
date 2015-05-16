# Python String sequence number generator Module
Python's module for generating sequnence numbers . 

You can use the module to generate string list that include sequential numbers 

Example :
For the string line : 
> " .../hakoiridevilprincess/[1:2|2]/0/0/[10:12|2].html "   

Generated string list is : 

>.../hakoiridevilprincess/01/0/0/10.html  
>.../hakoiridevilprincess/01/0/0/11.html   
>.../hakoiridevilprincess/01/0/0/12.html   
>.../hakoiridevilprincess/02/0/0/10.html   
>.../hakoiridevilprincess/02/0/0/11.html   
>.../hakoiridevilprincess/02/0/0/12.html   

##Example of use
```python

STRING_DATA ="Hello [1:2|3] Word [4:5|2] How are you [70:75|3] "

def test_sequence_generator() :
    import HSequencesGen.Generator as Generator
    generated_list = Generator.generate_sequence(STRING_DATA)
    print("Generated items : {}".format(len(generated_list)))
    for generated_item in generated_list :
        print (generated_item[0])

if __name__ == '__main__':
    test_sequence_generator()
```
    
