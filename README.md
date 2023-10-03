# ft_matrix

It is the study of vector spaces, which consist of objects called vectors. Tranformations
of vectors, called linear maps, are generally represented as objects called "matrices" in
the most usual (finite-dimensional) case. There also exist other, more complex, kinds
of vector spaces: like real or complex polynomials, and function spaces. Linear algebra
allows us to study these diverse subjects within a unifying framework. This makes the
more complicated cases easier to understand, since their properties are generally the same
as the simple cases, and so you can use the simple cases to mentally visualize what would
happen in the complicated ones. For this reason, we will concentrate on the fundamental
case of finite-dimensional vectors and matrices, with an emphasis on 2D and 3D, which
can easily be visualized.

If the mathematical operation is nonsensical (ie, summing a vector and a scalar, or vectors of different sizes), the result is undefined.
### Should i put an exception or nothing ?

### TODO:
- exercise 04 is it ok if there is a different format for the print ?
- [ ] make the functions in "Code constraints" ?
- [ ] make a function called "from" ? ex00
- [ ] for "dot function" should i change self or just return the result ?

[Row Echelon](https://saturncloud.io/blog/reducing-a-matrix-to-row-echelon-form-using-numpy-a-comprehensive-guide/)

## Row Echelon Form

[Theory](https://www.auto-math.be/public/8/module/16/theorie/65)

[Theory on Matrix](https://bouquinpython.readthedocs.io/fr/latest/matrices.html)

[Gaussian Elimination Using Pivot](https://www.delftstack.com/fr/howto/python/gaussian-elimination-using-pivoting/)

[Using Pivot in Python](http://desaintar.free.fr/python/cours/pivot.pdf)

## Determinant

Il s'agit donc d'effectuer tous les produits possibles en prenant un élément par ligne et par colonne dans la matrice, de les multiplier tantôt par +1 tantôt par –1, et de faire la somme des n! termes ainsi obtenus. Cette affectation (+1 ou –1) fait intervenir le nombre d'inversions de la permutation, c'est-à-dire le nombre de paires parmi les termes du produit où l’élément de gauche dans la matrice est situé plus bas que l'élément de droite. Si ce nombre est impair, le produit est multiplié par –1, sinon il est multiplié par +1.

![img](utils/Screenshot%202023-09-20%20at%2015.15.48.png)

Il y a six produits à calculer en prenant un terme par ligne et par colonne :

* Le produit (–2)(1)(–1) est précédé de + car dans toutes les paires, le terme de gauche est au-dessus de celui de droite ;
* le produit (–2)(0)(3) est précédé du signe – car il existe une seule paire, la paire {0;3}, où le terme de gauche est sous le terme de droite ;
* le produit (–1)(2)(–1) précédé de – car il existe une seule paire, {–1;2}, où le terme de gauche est sous celui de droite ;
* le produit (–1)(0)(–3) précédé de + à cause des paires {–1;–3} et {0;–3} ;
* le produit (4)(2)(3) précédé de + à cause des paires {4;2} et {4;3} ;
* et le produit (4)(1)(–3) précédé de – à cause des trois paires {4;1}, {4;–3} et {1;–3}.

![img](utils/Screenshot%202023-09-20%20at%2015.17.13.png)

[HEC: Cofactor, minor, Laplace Formula](https://www.hec.ca/cams/rubriques/Les_determinants_des_matrices.pdf)

[Determinant](http://gilles.dubois10.free.fr/algebre_lineaire/evaldet.html)

## Inverse

There is 3 rules to find the inverse of a matrix:
* must be square
* the determinant must be different from 0

[Inverse](https://www.youtube.com/watch?v=wOlG_fnd3v8&list=PL3WoIG-PLjSv9vFx2dg0BqzDZH_6qzF8-&index=3)

## Rank

[rank](https://www.nagwa.com/fr/explainers/402106373582/)

[course](https://math.univ-cotedazur.fr/~walter/L1_Info/Cours_rang.pdf)

Le rang d'une matrice échelonnée, réduite ou non, est le nombre de lignes possédant un pivot (non nul). C'est également le rang de la matrice initiale, les opérations de réduction ci-dessus conservant chacune le rang.