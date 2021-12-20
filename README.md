Constituency TreeBanks
============

When one talks about the “success” of a Natural Language Processing solution, they often refer to its ability to analyse the semantic and syntactic structure of a given sentence. Such a solution is expected to be able to understand both the linear and hierarchical order of the words in a sentence, unveil embedded structures, illustrate syntactical relationships and have a firm grasp of the argument structure. In order to meet the expectations, cutting edge Natural Language Processing systems like parsers, POS taggers or machine translation systems make use of syntactically or semantically annotated treebanks. Such treebanks offer a deep look through the surface and into the logical form of sentences.

Annotated treebanks can be categorised as constituency treebanks and dependency treebanks. Constituency treebanks offers clarity through resolving structural ambiguities, and successfully illustrates the syntagmatic relations like adjunct, complement, predicate, internal argument, external argument and such. 

The very first comprehensive annotated treebank, the Penn Treebank, was created for the English language and offers 40,000 annotated sentences. Following the Penn Treebank, numerous treebanks annotated for constituency structures were developed in different languages including French, German, Finnish, Hungarian, Chinese and Arabic.

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/ParseTree-Cy), [Java](https://github.com/starlangsoftware/ParseTree), [C++](https://github.com/starlangsoftware/ParseTree-CPP), [Swift](https://github.com/starlangsoftware/ParseTree-Swift), [Js](https://github.com/starlangsoftware/ParseTree-Js), or [C#](https://github.com/starlangsoftware/ParseTree-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-ParseTree
	
## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called ParseTree will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/ParseTree-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `ParseTree-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [TreeBank](#treebank)
+ [ParseTree](#parsetree)

## TreeBank

To load a TreeBank composed of saved ParseTrees from a folder:

	TreeBank(self, folder: str = None)

To load trees with a specified pattern from a folder of trees: 

	TreeBank(self, folder: str = None, pattern: str = None)
		
the line above is used. For example,

	a = TreeBank("/mypath");

the line below is used to load trees under the folder "mypath" which is under the current folder. If only the trees with ".train" extension under the same folder are to be loaded:

	a = TreeBank("/mypath", ".train");

the line below is used. 

To iterate over the trees after the TreeBank is loaded:

	for i in range(a.size()):
		p = a.get(i);
	
a block of code like this can be useful.

## ParseTree

To load a saved ParseTree:

	ParseTree(fileName: str)
	
is used. Usually it is more useful to load a TreeBank as explained above than loading the ParseTree one by one.

To find the node number of a ParseTree:

	nodeCount() -> int
	
leaf number of a ParseTree:

	leafCount() -> int
	
number of words in a ParseTree:

	wordCount(excludeStopWords: bool) -> int
	
above methods can be used.

# Cite

	@INPROCEEDINGS{9259873,
  	author={N. {Kara} and B. {Marşan} and M. {Özçelik} and B. N. {Arıcan} and A. {Kuzgun} and N. {Cesur} and D. B. {Aslan} and O. T. {Yıldız}},
  	booktitle={2020 Innovations in Intelligent Systems and Applications Conference (ASYU)}, 
  	title={Creating A Syntactically Felicitous Constituency Treebank For Turkish}, 
  	year={2020},
  	volume={},
  	number={},
  	pages={1-6},
  	doi={10.1109/ASYU50717.2020.9259873}}
