# ParseTree-Py

For Developers
============
You can also see either [Java](https://github.com/olcaytaner/ParseTree) 
or [C++](https://github.com/olcaytaner/ParseTree-CPP) repository.
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

	git clone https://github.com/olcaytaner/ParseTree-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `ParseTree-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 


## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run ParseTree-Py.

Detailed Description
============
+ [TreeBank](#treebank)
+ [ParseTree](#parsetree)

## TreeBank

Kaydedilmiş ParseTreelerden oluşan bir TreeBank'ı belirli bir klasörden yüklemek için

	TreeBank(File folder)

bir klasördeki ağaçlardan ismi belirli bir örüntüye sahip ağaçları yüklemek için

	TreeBank(File folder, String pattern)
	
bir klasördeki ağaçlardan ismi belirli bir örüntüye sahip ve numaraları da belirli bir aralıkta olanları yüklemek için ise

	TreeBank(File folder, String pattern, int from, int to)
	
kullanılır. Örneğin

	a = TreeBank(new File("/mypath"));

o anda bulunan klasörün altındaki "mypath" klasörünün altındaki ağaçları yüklemek için kullanılır. Aynı klasörün altındaki sadece "train" uzantılı ağaçlar yüklenecekse, 

	a = TreeBank(new File("/mypath"), ".train");

bu ağaçlardan sadece 1 ile 500 arasındaki ağaçlar yüklenecekse de

	a = TreeBank(new File("/mypath"), ".train", 1, 500);

kullanılır.

TreeBank yüklendikten sonra ağaçlar üstünde gezmek için ise,

	for (int i = 0; i < a.size(); i++){
		ParseTree p = a.get(i);
	}
	
gibi bir kod kullanılabilir.

## ParseTree

Kaydedilmiş bir ParseTree'yi yüklemek için

	ParseTree(FileInputStream file)
	
kullanılır. Genel olarak tek tek ParseTree yüklemek yerine yukarıda anlatıldığı gibi bir TreeBank yüklemek daha mantıklıdır.

Bir ParseTree'nin düğüm sayısını

	int nodeCount()
	
yaprak sayısını 

	int leafCount
	
içinde yer alan kelime sayısını da

	int wordCount(boolean excludeStopWords)
	
metodları ile bulabiliriz.
