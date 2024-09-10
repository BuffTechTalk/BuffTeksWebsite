import streamlit as st
from webpages import code_editor as ce



def pythonx_lesson1():
    st.title("Lesson 1: Introduction to Python")
    # Lesson1-Part1: what is programming
    st.header(":one: From Idea to Program")

    st.markdown(
        """
            The following chat outlines the basic logic of computer programming. We start with a task that we want the computer to help complete.

            - **Step 1**: The programmer **analyzes reuqirements** to identify the process to complete the task.
            - **Step 2**: The programmer **implements** the identified process in programming code as a computer program.
            - **Step 3**: The programmer **deploys** the program on the computer and let the complete complete the task and give expected outcomes.

            This is a simplified outline of coding (computer programming), and additional steps may be involved depending on the task's complexity and the program.
        """)
    st.image("./images/CodingProcess.png")

    # Lesson1-Part2: print out the words
    st.header(":two: First Python Program: Hello PythonX!")
    st.markdown("""Now, let's try our first program, which print out "Hello PythonX" on our computer screen with following code:""")
    st.code("""
        # Example 1: put following code in the editor and click APPLY to run
        print("Hello PythonX")
    """, line_numbers=True
    )

    # try sample code of hello pythonX
    ce.code_editor(height="100px",editor_label="lesson1-helloworld")

    st.markdown("""
        
        In the above code:

        ```python
        # Example 1: put following code in the editor and click APPLY to run
        ```
        - A sequence of words starting with the `#` symbol are comments in Python.
        > Comments are used to provide explanations or notes about the code. They are ignored by Python and do not affect the execution of the program. Comments help make the code more readable and understandable for other programmers or for future reference.

        ```python
        print("Hello PythonX!")
        ```
        - `print(input_value)` is the function used to display text or other data on the screen. Here, `"Hello PythonX!"` is the input value.
        > A function is a block of organized, reusable code that performs a specific task. Functions help to structure code, making it more readable, maintainable, and reusable. We can place a comment above or after a line of code.

        Let's see more examples:    
        """)
    st.code("""
        # Example 2: use print()function to print different kinds of values
        print(1234)  # This line prints the integer 1234
        print("abcdef")  # This line prints the string 'abcdef'
        print(3.141592653)  # This line prints the floating-point number 3.141592653, an approximation of Pi
        """, 
        line_numbers=True)
    ce.code_editor(height="100px",editor_label="lesson1-print")

    st.markdown("""
    
    - In Example 2, the `print()` function is used three times to output different values on three rows. When a program contains multiple lines of code.
    - The execution order is from the top to the bottom, processing each line sequentially.
    """)
    
    # Lesson1-Part3: mathematical operations
    st.header(":three: Do Math in Python")
    st.write("Mathematical operations in Python are similar to those learned in math class.")
    st.code("""
        # Example 3: Demonstrating basic arithmetic operations
        a = 10  # Assigns integer 10 to variable 'a'
        b = 3   # Assigns integer 3 to variable 'b'
        c = 2.5 # Assigns floating-point number 2.5 to variable 'c'

        print('Addition: ', a + b)       # Prints the sum of 'a' and 'b'
        print('Subtraction: ', a - b)    # Prints the result of subtracting 'b' from 'a'
        print('Multiplication: ', a * b) # Prints the product of 'a' and 'b'
        print('Multiplication: ', a * c) # Prints the product of 'a' and 'c', demonstrating integer-float multiplication
        print('Division: ', a / b)       # Prints the division of 'a' by 'b', result is a float
        print('Floor Division: ', a // b) # Prints the floor division of 'a' by 'b', removing digits after the decimal point
        print('Modulus: ', a % b)        # Prints the remainder of 'a' divided by 'b'
        """, line_numbers=True)
    ce.code_editor(height="250px",editor_label="lesson1-variables")
    st.markdown("""
        Example 3 teaches us how to do math in Python. First, we set up three variables, a, b, and c, like this:

        ```python
        a = 10
        b = 3
        c = 2.5
        ```

        These lines set up "containers" or **variables** that hold our numbers.

        > Think of a variable like a labeled box where you can store stuff. In programming, instead of physical things, we store data values. 
        
        > Just like we use a bottle to hold water or a shoebox for your shoes, variables help us keep our data organized and easy to use. 
        
        > In our Python program, a, b, and c are our boxes, holding the numbers 10, 3, and 2.5, making it easier for us to work with them in our math calculations.
        """)

    st.image("./images/lesson1-bottle.png")

    # Lesson1-Part4: value comparison
    st.header(":four: Comparisons in Python")
    st.write("We make comparisons everyday and use correct/wrong to check a comparison. E.g.: 10 is greater than 8, which is correct. How to represent this comparison in Python?")
    st.markdown("""
        In Python, we can use following symbols to make comparisons:

        | Symbol | Meaning               |
        |--------|-----------------------|
        | >      | Greater Than          |
        | <      | Less Than             |
        | >=     | Greater Than or Equal |
        | <=     | Less Than or Equal    |
        | ==     | Equal                 |
        | !=     | Not Equal             |
    
        We can compare two values directly, or compare the values of two variables.
        """)

    st.code("""
        number1 = 10
        number2 = 20
        print(10>20)
        print(number1>=number2)
        print(number1 == number2)
        print('Alice' != 'Bob')
    
        """, line_numbers=True)
    ce.code_editor(height="150px",editor_label="lesson1-comparevalue")
    st.write("""
        The ```True``` and ```False``` are ```bool``` (boolean) data type in Python. They represent **Correct** and **Wrong**, respectively. We can also create boolean variables like this:
        ```python
        is_adult = True
        is_student = False
        ```

        With the help of boolean values, we can make decisions in Python and ask Python program to do repetitive tasks.
        """)
    
    # Lesson1-Part5: decision making
    st.header(":five: Conditionals: Makes Decisions in Python")
    st.markdown("""
        Now we can make a Comparison with comparison operators in Python. Next, we will learn how to make decisions based on a comparison result.

        Python has several structures to make decisions, including if, if-else, elif statements.
        """)
    st.markdown("""
        ### ```if``` Statement
        ```if``` statement make a decision with one choice. The condition is a boolean value (True/False) which can be a comparison result.

        If the condition is ```True```, the *if-code block* will be excuted. If the condition is ```False```, the *if-code blcok* will be skipped, and run the code below if statemnt.

        ```python
        if condition:
            #if-code block
        ```

        For example, if we want to represent the following statements in Python, we can do that with ```if``` statement
        * You are an adult if you over 18 years old.
        * You can drive a car if you have a drive license.
        """)
    st.code("""
        # Example 1
        Age = 24;
        if Age >=18:
            print('You are an adult')

        # Example 2
        has_license = False
        if has_license == True:  # False == True-> Flase
            print('You can drive')
        print('False condition, skip the if statement')
        """, line_numbers=True)
    st.markdown("""Python uses indentation (**white space** or **tab** at the beginning of a line) to show the codeblock levels.""")
    ce.code_editor(height="200px",editor_label="lesson1-if-condition")

    st.markdown("""
        ### ```if-else``` Statement
        ```if-else``` statement: makes a decision from two choices. 
        If the condition is ```True```, the *if-code block* will be executed. If the condition is ```False```, the *else-code block* will be executed.

        ```python
        if condition:
            #if-code block
        else:
            #else-code block
        ```

        For example: we want to compare if ```a``` equals to ```b```.
        """)
    st.code("""
        a = 10
        b = 10
        # check if a equals to b
        if a==b:
            print('a==b')
        else: # a != b
            print("a!=b")

        # check if a doesn't equals to b
        if a!=b:
            print('a!=b')
        else:# a==b
            print('a==b')
        """, line_numbers=True)
    ce.code_editor(height="250px",editor_label="lesson1-if-else-condition")
   
    st.markdown("""
        ### ```if-elif``` Statement

        The ```elif``` statement allows you to check multiple conditions for TRUE and will execute the code block of the first ```True``` condition, then end the if-elif statement.
        If all conditions are False, the final ```else``` code block will be executed.

        ```python
        if condition1:
            #if-code block
        elif condition2:
            # elif block
        elif condition3:
            # elif block
        elif condition4:
            # elif block
        # the N-th condition
        elif conditionN:
            # elif block
        else:
            #else-code block
        ```
        For example, given a number x, to check if x is positive, zero, or negative:
        """)
    st.code("""
        x = 0
        if x>0:
            print('x is positive')
        elif x==0:
            print('x is zero')
        else: # x<0
            print('x is negative')
        """, line_numbers=True)
    ce.code_editor(height="150px",editor_label="lesson1-if-elif")


    st.markdown("""
        ### ```nested-if``` Statement
        include if statements within another if statement to provide more choices. 

        ```python
        if condition1:# outer-if condition
        # outer-if code blcok
        if condition2: #inner-if condition
            # inner-if code block
        else:
            # inner-else code block
        else: # outer-else 
        # outer-else code blcok
        if condition3:
            # inner-if code block
        else:
            # inner-else code block
        ```

        For example: find the largest value from n1,n2,n3
        """)
    st.code("""
        n1 = 10
        n2 = 20
        n3 = 30
        if n1>n2:
            if n1>n3:
                print("The largest num: n1")
            
            else:#n1<=n3
                print("The largest num: n3")

        else: #n2>=n1
            if n2>n3:
                print("The largest num: n2")
            
            else:#n3>=n2
                print("The largest num: n3")
        """, line_numbers=True)
    
    ce.code_editor(height="250px",editor_label="lesson1-if-elif-condition")

    # Lesson1-Part6: boolean operator
    st.header(":six: Boolean Logical Operators")
    st.markdown("""
        Boolean logical operators are used to make more complicated conditions for if statements that rely on more than one condition.
        Python's Boolean logical operators include: ```and```, ```or```, and ```not```.

        * The ```and``` operator takes two sub-conditions, and evaluates as **True** if, and only if, *both of its sub-conditions are True*. Otherwise, it evaluates to False.
        ```python
        print(2>1 and 2<3) # the output is: True
        ```

        * The ```or``` operator takes two sub-conditions. It evaluates to **True** if either (or both) of sub-conditions are True, and False if both sub-conditions are False
        ```python
        print(1>10 or 2<3) # the output is: True
        print(1>10 or 2>10) # the output is: False
        ```

        * The ```not``` operator is used to invert a condition. If a condition is True, the **not True** will be **False**. The **not False** will be **True**.
        ```python
        print(not 2>1) # the output is: False
        print(not 2>10) # the output is: True
        ```    
    """)
    ce.code_editor(height="150px",editor_label="lesson1-boolean-operator")

    st.markdown("""
    ### Precedence (Order) of Logical Operators

    When a complex condition consists of several sub-conditions chained with different logical operators, we should:
    1. check the sub-conditions in ```parentheses``` 
    2. check ```not```, ```and```, ```or``` sequentially.

    For example,
    ```python
    not True and (20<30) or not (10!=15)
    # (not True) and True or (not True)
    # (False and True) or False
    # False or False
    # False
    ```

    Try another example:
    ```python
    10>20 and 20<30 or not (1 != 5)
    ```
    To check the boolean value of above complex condition:
    1. ```(1!=5)``` is True
    2. ```not(1!=5)``` is False
    3. check ```10>20``` is False, ```20<30```is True, ```False and True``` is False 
    4. Finally, ```False or False``` is False

    Try to print the result in the following code editor:
    ```python
        print( 10>20 and 20<30 or not (1 != 5) )
    """)
    ce.code_editor(height="50px",editor_label="lesson1-logical-operator-order")

    # Lesson1-Part7: loop
    st.header(":seven: Loops")
    st.markdown("""
        Loops are used to repeat a block of code multiple times. Here are two types of loops: ```while loop``` and ```for loop```
        ### ```while``` loop
        
        Following is the basic structure of ```while``` loop:

        ```python
        start-value
        while stop-condition:
            code-block
            step-size
        ```
        Let's see a while loop example:
        
        ```python
        # print numbers between 0 and 5
        num = 0;
        while num<=5:
            print(num)
            num = num +1
        print("end")
        ```
        """)
    ce.code_editor(height="150px",editor_label="lesson1-while-loop")

    st.markdown("""
        ### ```for``` loop

        for loop often used to iterate over a given collection, such as lists or strings.

        ```python
        for item in collection:
            code-block
        ```
        """)
    st.code("""
        # This is a list of names. List is a collection of values
        name_list = ['Alice','Bob','Cathy','David']
        for name in name_list:
            print(name)
        """)
    ce.code_editor(height="100px",editor_label="lesson1-for-loop")

    st.markdown("""
        ### Loops with if Statement
        We often combine loops with if statements to select specific elements.
        """)
    st.code("""
        # Example 1: # print all numbers between 0 to 20 that are divisible by 3
        num = 0;
        while num<=20:
            if num%3==0:
                print(num)
            num = num +1

        # Example 2: print all names contains lower-case 'a' or 'b'
        name_list = ['Alice','Bob','Cathy','David']
        for name in name_list:
            if 'b' in name or 'a' in name:
                print(name)
        """, line_numbers=True)
    
    ce.code_editor(height="220px",editor_label="lesson1-loop-if")

    # Lesson1-Part8: Python Collections Data Type
    st.header(":eight: Python Collections Data Type")
    st.markdown("""
    ### ```List```
    A list is a collection of elements (numbers, words) within a pair of square brackets. It uses commas to separate elements.
    
    Each element in list has an index. And the index starts from 0.
    
    A certain item in the list can be accessed by using its index in square brackets.
    """)
    st.code("""
        name_list = ['Alice','Bob','Cathy','David']
        id_list = [111,222,333,444,555]
        mix_list = [1,'Alice',True,2.33]

        # print whole list
        print(mix_list)

        # print elements one by one
        for id in id_list:
            print(id)
        # print lenght
        print('The length of mix_list: ',len(mix_list))

        # access specific element via index
        print(name_list[0], name_list[2])

        # create an empty list
        empty_list = []
        # add element to the end of list with the append()
        empty_list.append('Math')
        empty_list.append('English')
        print(empty_list)
        """, line_numbers=True)
    st.markdown("More about List:https://www.w3schools.com/python/python_ref_list.asp")
    ce.code_editor(height="400px",editor_label="lesson1-list")
    
    
    st.markdown("""
    ### ```Dictionary```
    
    A dictionary is a collection of data stored in ```key:value``` pairs. The ```key``` should be unique (like student ID).
    """)

    st.code("""
        # a dictionary of id-name pairs
        id_name_dict = {
            111:'Alice',
            222:'Bob',
            333:'Cathy'
        }
    
        # access name "Alice" (value) via the id (key)
        print(id_name_dict[111])

        # iterate all pairs
        for id,name in id_name_dict.items():
            if id<300:
                print(f'ID: {id}, Name: {name}')
        """, line_numbers=True)
    ce.code_editor(height="250px",editor_label="lesson1-dictionary")

    st.header(":nine: Functions")
    st.markdown("""
        In Python, we create functions to reuse code. A ```function```, sometimes called a ```method```, is a reusable block of code that has a name, can take input arguments, and can return values.
        ```python
        def function_name(input_arguments):
            code-block
            return values
        ```


        *   ```def``` is the keyword to indicate a function
        *   ```input_arguments``` are the input values used in code block, and it is optional.
        *   ```return``` is the keyword used to send out the running results from code-block and it is also optional. It will end the function after returning a value to the function call.
        """)

    st.code("""
        # sample function without input arguments and return values
        def print_hello():
            print('Hello WT!')
        
        # type function name to call the function directly.
        print_hello()
        print_hello()
        print_hello()
    
    """, line_numbers=True)


    st.code("""
        # sample function with input arguments and return value
        def tree_sum(a,b,c):
            result = a+b+c
            return result
       
        # call function with given values and use another variable to hold return values
        sum1 = tree_sum(1,2,3)
        sum2 = tree_sum(4,5,6)

        print('sum1: ', sum1)
        print('sum2: ', sum2)
    
    """, line_numbers=True)

    st.code("""
        # sample function with multiple return values
        def sum_len(num_list):
            total = 0
            for num in num_list:
                total = total+num
            return total, len(num_list)
       
        num_list = [0,1,2,3,4,5,6,7,8,9]
        # t is a variable used to hold returned total
        # l is a variable used to hold returned length: len(num_list)
        t,l = sum_len(num_list)
        print(f'The length of list is: {l}; the sum of list is: {t}')
    
    """, line_numbers=True)
    ce.code_editor(height="400px",editor_label="lesson1-function")

    st.write("""
        This lesson provides a broad overview of the key components of the Python programming language. 
        
        If you'd like to learn more about Python in a structured way, I recommend [Sololearn](https://www.sololearn.com/en/learn/courses/python-introduction) platform, where I taught myself Python coding.
        
        Starting with the next lessons, we will explore how to use Python to build applications in various fields.
        
        Feel free to reach out to me if you have any questions about programming: <czhang@wtamu.edu> Or [Register](https://wtamuuw.az1.qualtrics.com/jfe/form/SV_2boQtKLCptO33HE) to join our Discord channel
        """)
