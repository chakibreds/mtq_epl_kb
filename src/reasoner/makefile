# Compilation et éxecution du Programme java JenaApi
# Prérequis: 
#	l'API Jena, le chemin vers les fichiers JAR's
# 		À Spécifier dans la variable $(CP) (ClassPath)
# 	Un fichier RDF au format RDF/XML
#		À Spécifier dans la variable $(EXEARG)
#
# Author: Massili Kezzoul, Chakib Elhouiti
#

CLASSNAME = JenaApi
CP = ./lib/*:
COMPARG= # -XLint

EXEARG = ../../ontologies/Bet.owl ../../ontologies/data.owl # path to RDF/XML file 

all:
	javac $(COMPARG) -cp $(CP) $(CLASSNAME).java

use:
	java -cp $(CP) $(CLASSNAME) $(EXEARG) > output.owl