# Pickling and Error Exception Handling
*Wyatt Parks 31May2023*

 In Python, there are two essential concepts that every programmer should understand: pickling and error exception handling. Pickling provides a convenient way to serialize and store objects, allowing for easy preservation and reconstruction of complex data structures. On the other hand, error exception handling equips developers with the ability to anticipate and handle errors, ensuring smooth execution of their code even in the face of unexpected events. Together, these topics form the foundation of Python programming, enabling efficient data management and robust error management, ultimately contributing to the reliability and effectiveness of Python applications.

Pickle is a module that can be imported to allow objects to be serialized and stored in a binary format. It can convert simple objects such as strings and integers. It can also convert more complex objects such as lists and dictionaries. The 'dump()' function allows for the conversion, and it accepts parameters for the object and the file. The 'load()' function converts data from a file back into readable data and accepts the file as a parameter.

Error exception handling is a method to catch and handle errors that occur while the code is running. Exception handling is done using try and except blocks, where the code is placed within the try block and any errors are passed to the exception block. There can be multiple exception blocks for a try block to catch multiple errors. Additionally, custom exceptions can be raised that wouldn't normally cause an error.

