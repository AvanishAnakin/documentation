"""Automated class Generation"""
import os

from dataclasses import dataclass


@dataclass
class ClassGenerator():
    '''
    This class is used to generate a class file.

    Sample Image

    .. image:: ../../images/1.png
        :width: 1000
        :alt: Alternative text
    '''

    name: str
    # Name of the file and class to be generated
    members: list()
    getters = list()
    setters = list()
    constructor: str
    constructor_args: list()

    def __init__(self, name: str, members: list(), constructor_args: list()):
        '''Initializes the class generator.

        Some detailed description
        
        Args:
            name (int): The name of the class.
            members (List[str]): A list of members to be added to the class.
            constructor_args: (List[str]): A list of arguments to be passed to the constructor.

        Returns:
            None: Does not return anything.

        Examples:
            >>> from classgen import ClassGenerator
            >>> student = ClassGenerator('student', ['name', 'standard', 'dob'])
            <ClassGenerator at 0x107352eb0>
        '''
        self.name = name
        self.members = members
        self.constructor_args = constructor_args
        # Create the getters and setters
        for member in members:
            self.getters.append('get_' + member[0] + member[1:])
            self.setters.append('set_' + member[0] + member[1:])
        # Add the constructor

    def generate_class_docstring(self):
        '''Initializes the class generator.

        Some detailed description
        
        Args:
            name (int): The name of the class.
            members (List[str]): A list of members to be added to the class.
            constructor_args: (List[str]): A list of arguments to be passed to the constructor.

        Returns:
            None: Does not return anything.

        Examples:
            >>> cg = ClassGenerator('stduent', ['m1', 'm2', 'm3'], ['m1', 'm2', 'm3'])
            >>> cg
            <ClassGenerator at 0x107352eb0>
            >>> cg.generate_class_docstring()
            "Some Very Long String with tabs and newlines"


        '''
        '''Generate the class docstring.

        Generates the class docstrings based on class attribute values.
        
        Args:
            None: This method does not accept any argument.

        Returns:
            str: Returns the complete docstring of the class.

        Examples:

        >>> `cg = ClassGenerator('stduent', ['m1', 'm2', 'm3'], ['m1', 'm2', 'm3'])`
        >>> `cg`
        <ClassGenerator at 0x107352eb0>
        >>> `cg.generate_class_docstring()`
        "\t"""\n\tThis class is used to represent a stduent.\n\t\n\tAttributes:\n\t\tm1: The m1 of the stduent.\n\t\tm2: The m2 of the stduent.\n\t\tm3: The m3 of the stduent.\n\t\n\tMethods:\n\t\tget_m1(self): Gets the m1 of the stduent.\n\t\tget_m2(self): Gets the m2 of the stduent.\n\t\tget_m3(self): Gets the m3 of the stduent.\n\t\tset_m1(self, m1): Sets the m1 of the stduent.\n\t\tset_m2(self, m2): Sets the m2 of the stduent.\n\t\tset_m3(self, m3): Sets the m3 of the stduent.\n\t"""\n\n"
        '''
        docstring = str()
        docstring += ('\t\"\"\"\n')
        docstring += ('\tThis class is used to represent a ' + self.name + '.\n')
        docstring += ('\t\n')
        docstring += ('\tAttributes:\n')
        for member in self.members:
            docstring += ('\t\t' + member + ': The ' + member + ' of the ' + self.name + '.\n')
        docstring += ('\t\n')
        
        # Write details of methods
        docstring += ('\tMethods:\n')
        for getter in self.getters:
            docstring += ('\t\t' + getter + '(self): Gets the ' + getter[4:] + ' of the ' + self.name + '.\n')
        for setter in self.setters:
            docstring += ('\t\t' + setter + '(self, ' + setter[4:] + ')' +  ': Sets the ' + setter[4:] + ' of the ' + self.name + '.\n')        
        docstring += ('\t\"\"\"\n')
        docstring += ('\n')
        return docstring

    def generate_members(self):
        '''
        Generate the members docstring.
        '''
        docstring = str()
        # Create the members
        for member in self.members:
            docstring += ('\t_' + member + ': ' + 'None\n')
        docstring += "\t\n"
        return docstring

    def generate_constructor_docstring(self):
        '''
        Generate the constructor docstring.
        '''
        docstring = str()
        # Create the docstring
        docstring += ('\t\t\"\"\"\n')
        docstring += ('\t\tInitializes a ' + self.name + ' object.\n')
        docstring += ('\t\t\n')
        docstring += ('\t\tParams:\n')
        for arg in self.constructor_args:
            docstring += ('\t\t\t' + arg + ': The ' + arg + ' of the ' + self.name + '.\n')
        docstring += ('\t\t\"\"\"\n')
        return docstring

    def generate_constructor(self):
        # Write the constructor
        docstring = str()
        docstring += ('\tdef __init__(self')
        for arg in self.constructor_args:
            docstring += (', ' + arg)
        docstring += ('):\n')
        docstring += (self.generate_constructor_docstring())
        # Write the constructor body
        for member in self.members:
            docstring += ('\t\tself._' + member + ' = ' + member + '\n')
        docstring += ('\t\n')
        return docstring
    
    def generate_getter_docstring(self, member):
        '''
        Generate the getter methods' docstrings.
        '''
        docstring = str()
        # Create the docstring
        docstring += ('\t\t\"\"\"\n')
        docstring += ('\t\tGets the ' + member[4:] + ' of the ' + self.name + '.\n')
        docstring += ('\t\t\n')
        docstring += ('\t\tReturns:\n')
        docstring += ('\t\t\t' + member + ': The ' + member[4:] + ' of the ' + self.name + '.\n')
        docstring += ('\t\t\"\"\"\n')
        return docstring

    def generate_getter(self):
        """Write the getters and setters"""
        docstring = str()
        for getter in self.getters:
            docstring += ('\tdef ' + getter + '(self):\n')
            docstring += (self.generate_getter_docstring(getter))
            docstring += ('\t\treturn self.' + getter[3:] + '\n')
            docstring += ('\n')
        return docstring
    
    def generate_setter_docstring(self, member):
        '''
        Generate the setter methods' docstrings.
        '''
        docstring = str()
        # Create the docstring
        docstring += ('\t\t\"\"\"\n')
        docstring += ('\t\tSets the ' + member[4:] + ' of the ' + self.name + '.\n')
        docstring += ("\t\t\n")
        docstring += ('\t\tParams:\n')
        docstring += ('\t\t\t' + member[4:] + ': The ' + member[4:] + ' of the ' + self.name + '.\n')
        docstring += ('\t\t\"\"\"\n')
        return docstring

    def generate_setter(self):
        docstring = str()
        for setter in self.setters:
            docstring += ('\tdef ' + setter + '(self, ' + setter[4:] + '):\n')
            docstring += (self.generate_setter_docstring(setter))
            docstring += ('\t\tself.' + setter[3:] + ' = ' + setter[4:] + '\n')
            docstring += ('\n')
            continue
        return docstring

    def generate(self, path: str="./name.py"):
        '''
        generate
        Generates the class file along with docstrings.
        
        Args:
            path: The path to the class file.

        Returns:
            None: Does not return anything. Only saves the value to the class attribute.
        '''
        # Name resolution of the file
        if path == "./name.py":
            path = "./" + self.name + ".py"
        # If file exists, delete the file
        if os.path.exists(path):
            os.remove(path)
        # Create the file
        file = open(path, 'w')
        # Write the class header
        file.write(f'#(class) {self.name}\n')
        file.write('class ' + self.name + ':\n')
        file.write(self.generate_class_docstring())                
        file.write(self.generate_members())
        file.write(self.generate_constructor())
        file.write(self.generate_getter())
        file.write(self.generate_setter())        
        # Close the file
        file.close()
        return None