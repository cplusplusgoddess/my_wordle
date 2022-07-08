# **my_wordle**

###Description
A python script using the wordle-utils PyPi package
***
###Requirements
<li>python3 (version 3.5 or greater)
<li>pip
<p>Additionally the setup.sh will install the following (and their dependencies) within your virtualenv: 
<li>wordle-utils 0.0.3</li>

###Installation
___
**Python Packages:** You’ll need to install python and a couple of packages manually. The setup script will handle the rest.
<br>**Steps:**
<ol><li>Install python3<li>Install pip3<li><code>bash ./setup.sh</code></ol>

### Running 
___
<code>% python3 my_wordle.py
 < _options_ >:<br>
     -**h**, --help <br>
     -**p**, --playmyself       Ill choose a random word and try and guess. (DEFAULT) <br>
     -**a**, --answer _ANSWER_  You give me the word to guess, and I will solve <br>
     -**i**, --interactive      I'll provide the guesses, you provide the results for 5 letters _ = BLACK, ? = YELLOW, ! = GREEN <br>
</code>

