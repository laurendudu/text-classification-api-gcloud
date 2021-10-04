## Notre projet ##
Nous avons créé une API avec `Python 3.9.7` et `Flask` qui utilise le modèle `distilbert-base-uncased-finetuned-sst-2-english` de [Hugging Face](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english). Cette API a été déployée avec [Google Cloud](https://cloud.google.com/). 


## Lien de l'API ##


## Coûts de l'API ##
cacules avec le site ...
pour 10 000 invocations

## Serverless vs. Iaas ##
* Serverless

Ce type de développement permet de créer des applications ainsi que de les faire fonctionner sans à gérer de serveurs. Il est toujours nécessaire de les utilise mais ce n’est plus le problème de l’utilisateur : c’est au fournisseur de services cloud (AWS, Azure ou encore Google Cloud) de tout gérer de ce côté-ci. De plus, le serverless est facturé selon son activité. Le fournisseur se doit de faire fonctionner les applications via des conteneurs qui se mettent en route en fonction de l’utilisation qui est activé suivant une étape de déclenchement (requête de http par exemple). Le serverless est aussi appelé FaaS (Functions as a Service).  

Exemples : AWS Lambda, Azure Functions, Cloud Functions  

 

* IaaS (Infrastructure-as-a-Service):  

Il s’agit d’un service de cloud computing qui offre à son utilisateur le stockage et la virtualisation mais ces services sont facturés. De plus, l’utilisateur a à sa disposition des serveurs et n’a pas à gérer la maintenance ou encore les mises à jour. Via l’Iaas il est possible de développer facilement ses environnements et de les tester ou encore de les supprimer lorsque l’utilisateur n’en a plus besoin. En effet, l’utilisateur d’Iaas achète seulement ce qui l’intéresse dans les composantes proposées et il peut les faire évoluer. Néanmoins, l’utilisateur se doit de payer à l’avance les unités de capacité dont il aura besoin. Ainsi les serveurs sont actifs tout le temps pour le fonctionnement des applications de l’utilisateur, même lorsque l’application n’est pas lancée.  

Exemples : AWS, Microsoft Azure, Google Cloud  

## Groupe ##
Ce projet a été réalisé par [Sirine Haddouche](https://github.com/sirinehaddouche) et Lauren Durivault.

