# TP : Analyse de données de ventes

**Contexte Business:** Vous êtes analyste de données chez DataShop, une entreprise de commerce en ligne spécialisée dans la vente de produits électroniques. Vous disposez d'un ensemble de données des ventes mensuelles de différents produits sur un an. Votre objectif est d'analyser ces données pour aider l'entreprise à optimiser ses stocks et ses stratégies de vente.

**Dataset:** Le dataset (jeu de données) est simulé comme un tableau NumPy 2D nommé `ventes`, où chaque ligne représente un mois (Janvier à Décembre), et chaque colonne représente un produit différent. Les valeurs dans le tableau représentent le nombre d'unités vendues.

**Note :** 

- Il est possible d'utiliser le paramètre `axis` sur de nombreuses fonctions.
- Cherchez les fonctions non-découvertes pour le moment.
- Pensez à utiliser le slicing si nécessaire.

## Exercice 1: Initialisation du Dataset

- Créez un tableau NumPy `ventes` de dimensions 12x5 contenant des valeurs aléatoires entre 0 et 1000 pour simuler les ventes mensuelles de 5 produits différents sur un an.

## Exercice 2: Affichage des Statistiques de Base

- Calculez et affichez la moyenne des ventes pour chaque produit.

## Exercice 3: Mois avec les Meilleures Ventes pour le Produit 1

- Utilisez un filtre booléen pour identifier les mois où les ventes du produit 1 ont dépassé la moyenne des ventes de ce produit.

## Exercice 4: Comparaison des Ventes Entre Deux Produits

- Identifiez les mois où le produit 2 a mieux vendu que le produit 3. Utilisez `np.where` pour obtenir les indices de ces mois.

## Exercice 5: Produit Star du Catalogue

- Déterminez quel produit a eu le plus grand nombre total de ventes sur l'année et affichez ce produit et son total de ventes.

## Exercice 6: Mois avec Ventes Faibles pour Tous les Produits

- Trouvez les mois où toutes les ventes de produits sont en dessous de 500 unités. Utilisez l'indexation booléenne pour identifier ces mois.
- **Note :** Vous pouvez enlever la seed (si vous en avez une) pour trouver une génération correspondante.

## Exercice 7: Augmentation des Ventes Mois sur Mois

- Pour chaque produit, identifiez les mois où les ventes ont augmenté par rapport au mois précédent. Affichez une liste de ces mois pour chaque produit.

## Exercice 8: Stagnation des Ventes

- Calculer la tendance moyenne des ventes pour chaque produit sur l'année et identifier le produits le plus performant ainsi que celui à risque, nécessitant une attention particulière.

## Exercice 9: Identification des Opportunités de Bundle

- Identifiez les mois où au moins trois produits ont des ventes supérieures à leur moyenne respective. Ces mois pourraient indiquer des opportunités pour créer des bundles de produits pour stimuler les ventes.