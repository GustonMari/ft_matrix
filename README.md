# ft_matrix

If the mathematical operation is nonsensical (ie, summing a vector and a scalar, or vectors of different sizes), the result is undefined.
### Should i put an exception or nothing ?

### TODO:
- [ ] need to change the `__str__` of the matrix
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
