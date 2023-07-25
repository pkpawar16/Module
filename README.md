# Problem Statement::


   Write an install able module in python with the following functionality:
   The module should be able to read .yaml, .cfg, .conf configuration file formats, read the configurations 
   and generate a flat dictionary out of it.
   Depending on the requirement, the module should be able to write the configurations in .env file, .json file 
   or it should also be able to set the configurations in the os environment.
   Please move the code to GitHub and share us Link.
   NOTE: Please follow the below instructions:
         1. The program should be developed in pure python, no frameworks should be used.
         2. The program can be developed with OOPs or a functional programming approach.
         3. The program must have unit test cases written with pytest and they need to have at least 85% code coverage.
         4. There needs to be a README file documenting the details about the program, installation, and running guidelines.


# Step-by-step process:

    STEP 1: git clone <https-url-copied-from-github>
    STEP 2: virtualenv venv
    STEP 3: .\venv\Scripts\activate
    STEP 4: pip install -r requirements.txt
    STEP 5: python config_parser.py

# Project Structure:
    
    Assigement (# project root)
     |--config_paresr.py (# configurations related files)
     |--README.md (#documetation)
     |--test_file.py (# testcases for all functions using pytest)
     |--venv
     |--requirements.txt (#dependency management)
   

Commands::

# To run the testcases use following commands:
    pytest test_file.py



     >> 