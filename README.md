For Developers
============

You can also see [Java](https://github.com/starlangsoftware/ParseTree), [C++](https://github.com/starlangsoftware/ParseTree-CPP), or [C#](https://github.com/starlangsoftware/ParseTree-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

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

## Cite
If you use this resource on your research, please cite the following paper: 

```
@inproceedings{yildiz2014constructing,
  title={Constructing a {T}urkish-{E}nglish parallel treebank},
  author={Y{\i}ld{\i}z, O. T. and Solak, E. and G{\"o}rg{\"u}n, O. and Ehsani, R.},
  booktitle={Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics},
  volume={2},
  pages={112--117},
  year={2014}
}

@incollection{yildiz2015constructing,
  title={Constructing a {T}urkish constituency parse treeBank},
  author={Y{\i}ld{\i}z, O. T. and Solak, E. and {\c{C}}and{\i}r, {\c{S}}. and Ehsani, R. and G{\"o}rg{\"u}n, O.},
  booktitle={Information Sciences and Systems 2015},
  pages={339--347},
  year={2015},
  publisher={Springer}
}

@InProceedings{gorgun16,
  author    = {O. Gorgun and O. T. Yildiz and E. Solak and R. Ehsani},
  title     = {{E}nglish-{T}urkish Parallel Treebank with Morphological Annotations and its Use in Tree-based SMT},
  booktitle = {International Conference on Pattern Recognition and Methods},
  year      = {2016},
  address   = {Rome, Italy},
  pages     = {510--516}
}
