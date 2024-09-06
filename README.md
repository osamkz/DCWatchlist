# MY FINAL PROJECT
This web-app acts like a Watchlist specific for DC Universe Movies. It is based on a list of the released movies related to DC Universe so far with their specific informations.  

- What does it do?  
  The aim for the user is to be able to scroll through the list of the movies of the universe, get access to the details and leave a review after finishing a movie. The user can also track the movies to watch by adding them to its watchlist. 

- What is the "new feature" which you have implemented that we haven't seen before?  
  Some new features implemented:
  - Populating a list of pages based on a file, with each page its specific details.
  - Adding comments that can be saved with a date on each movie page
  - Adding elements to a watch list and displayed on the homepage thanks to Local storage function

## Prerequisites
Did you add any additional modules that someone needs to install (for instance anything in Python that you `pip install-ed`)? No
List those here (if any).

## Project Checklist
- [X] It is available on GitHub.
- [X] It uses the Flask web framework.
- [X] It uses at least one module from the Python Standard Library other than the random module.
  Please provide the name of the module you are using in your app.
  - Module name: Datetime Module
- [X] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to let the class initialize the object's attributes (note that  `__init__()` doesn't count as a method). This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name for the class definition: courseapp.py
  - Line number(s) for the class definition: 51-60
  - Name of two properties: movie_len, movie_Timeline
  - Name of two methods: populate_moviz, movie_info
  - File name and line numbers where the methods are used: courseapp.py, 131-182
- [X] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [X] It uses modern JavaScript (for example, let and const rather than var).
- [X] It makes use of the reading and writing to the same file feature.
- [X] It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name: courseapp.js
  - Line number(s): 78-95
- [] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name:courseapp.py
  - Line number(s):162-178
- [X] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [X] It doesn't generate any error message even if the user enters a wrong input.
- [X] It is styled using your own CSS.
- [X] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  
- [X] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.