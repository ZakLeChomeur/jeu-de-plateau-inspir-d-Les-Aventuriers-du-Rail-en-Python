# jeu-de-plateau-inspir-d-Les-Aventuriers-du-Rail-en-Python

Ce projet correspond au développement d’un jeu de plateau inspiré d’Les Aventuriers du Rail, implémenté en Python, dans un cadre académique. L’objectif principal est de poser les fondations logiques et algorithmiques du jeu, en modélisant les cartes, les joueurs et le déroulement général d’une partie, plutôt que de proposer une version entièrement finalisée.

Le jeu est actuellement à l’état de prototype. Toutes les mécaniques du jeu original ne sont pas encore implémentées. En particulier, certaines actions centrales, comme la prise de possession des routes ou le calcul final détaillé des scores, ne sont pas encore disponibles. Le projet se concentre principalement sur la gestion des cartes (wagons et trajets), leur mélange, leur distribution aux joueurs, ainsi que sur plusieurs actions associées à ces cartes au fil des tours.

L’architecture du programme repose sur une approche orientée objet. La classe `Carte` gère les différentes piles de cartes, leur tirage aléatoire et leur épuisement progressif. La classe `joueur` modélise l’état interne d’un joueur, incluant sa main de cartes, ses trajets collectés et son score. La classe `jeu` centralise la logique globale : choix du mode de jeu, initialisation de la partie, enchaînement des tours et exécution des actions possibles à chaque tour.

Le jeu propose un mode joueur contre joueur, partiellement fonctionnel, ainsi qu’un mode joueur contre ordinateur, encore en cours de développement. Les interactions se font via une interface en ligne de commande. Pour effectuer des choix, le joueur doit simplement entrer le chiffre correspondant à l’action souhaitée, en se laissant guider par les messages affichés dans le terminal. Ce choix volontairement minimaliste permet de se concentrer sur la logique interne du jeu plutôt que sur l’interface graphique.

⚠️ État du projet – à finaliser
Ce projet constitue une base fonctionnelle mais incomplète, destinée à être reprise et améliorée. Les principales pistes de finalisation incluent :

* l’implémentation complète des routes et de leur attribution,
* le calcul final des scores,
* l’amélioration de l’intelligence artificielle,
* le renforcement de la robustesse des entrées utilisateur,
* la restructuration et la documentation du code.

Ce projet illustre avant tout une capacité à concevoir et structurer un système complexe, à identifier clairement ses limites actuelles et à définir des axes précis d’amélioration pour une version future plus aboutie.
