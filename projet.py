#!/usr/bin/env python
# coding: utf-8

# In[175]:


g = Graph()


# In[176]:


g . add_edges ([[0 ,1] ,[1 ,2]])


# In[3]:


g


# In[4]:


print(g)


# In[177]:


g . add_edges([[0 ,1] ,[0 ,2] ,[0 ,3] ,[1 ,4] ,[2 ,4] ,[4 ,5] ,[5 ,6] ,[5 ,7] ,[6 ,7] ,
[4 ,9] ,[4 ,8] ,[8 ,9] ,[1 ,2] ,[2 ,3]])


# In[178]:


g


# In[254]:


exemple = Graph()
exemple.add_edges([(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5),
                 (5, 6), (5, 9), (5, 10), (6, 7), (6, 8), (7, 8), (9, 10)])


# In[255]:


exemple


# In[282]:


def parcours_graphe(g, ordre=None):
    """
    Cette fonction permet de parcourir un graphe.
    
    ordre (optionnel) : ordre de parcours des noeuds.        
    """
    global nb_aretes_visitees, indice_chaine
    
    g = DiGraph(g) # on convertit les graphes non-orientés en orientés
    noeuds = g.vertices()
            
    couleur = {n: BLANC for n in noeuds} # tous les noeuds sont blancs au début
    deja_vu = {n: False for n in noeuds} # pour la décomposition en chaînes
    
    ordre_dfi = [] # DFI-order
    nb_aretes_visitees = 0 # pour la décomposition en chaînes
    
    chaines = []
    indice_chaine = 0 # sert à indicer la liste 'chaines'
        
    arbre_parcours = DiGraph() # DFS-tree T (contient *aussi* les arc arrières !)
    arbre_parcours.add_vertices(noeuds) # on met tous les noeuds de G dans T
    
    
    def parcours(noeud):
        """ Parcours individuel de chaque noeud. """  
        
        print('debut', noeud)        
        couleur[noeud] = GRIS
        ordre_dfi.append(noeud)
        
        for voisin in g.neighbors_out(noeud):
            print('\t', voisin)
            
            if couleur[voisin] == BLANC: # arc avant
                arbre_parcours.add_edge([voisin, noeud], label='arbre')                
                parcours(voisin)
                
            elif couleur[voisin] == GRIS: # arc arrière
                if voisin not in arbre_parcours.neighbors_out(noeud):
                    arbre_parcours.add_edge([voisin, noeud], label='arriere')  
        
              
        print('fin', noeud)
        couleur[noeud] = NOIR
        
    
    def est_connexe():
        """ 
        Renvoie True si le graphe est connexe, False sinon.
        On vérifie qu'il ne reste aucun sommet blanc.
        """                
        return not(BLANC in couleur.values())
    
    
    def lance_parcours():
        """
        Fonction qui lance le parcours en profondeur.
        """    
        if ordre: # si on a un ordre de parcours des noeuds        
            for n in ordre:
                if couleur[n] == BLANC:
                    parcours(n)
        else:
            for n in noeuds:
                if couleur[n] == BLANC:                
                    parcours(n)
    
    
    def parcours_decomposition_chaine(noeud, t=arbre_parcours):
        """ 
        Parcours individuel de chaque noeud,
        pour la décomposition en chaînes.
        Ici, on s'arrête dès qu'on rencontre un noeud déjà visité.
        
        ic: indice de la chaîne dans laquelle on rajoute les noeuds
        """  
        global nb_aretes_visitees, indice_chaine
        
        print('debut', noeud)        
        deja_vu[noeud] = True
        chaines[indice_chaine].append(noeud)
        
        voisins = t.neighbors_out(noeud)
        fonction_tri = lambda x : ordre_dfi.index(x)
        voisins_tries = sorted(voisins, key=fonction_tri)
        
        print(f'voisins_tries = {voisins_tries}')
        
        for voisin in voisins_tries:
            print('\t', voisin)
            
            if deja_vu[voisin]: # on s'arrête
                chaines[indice_chaine].append(voisin)
                indice_chaine += 1
                chaines.append([])
                print('fin', noeud)
                return STOP
            
            else:
                nb_aretes_visitees += 1
                parcours_decomposition_chaine(voisin)
              
        
        
    
    def decomposition_en_chaines(t=arbre_parcours, ordre=ordre_dfi):
        """
        Fonction qui effectue la décomposition en chaîne,
        à partir de l'arbre de parcours.
        """
        global indice_chaine
                
        #ordre de parcours des noeuds        
        for n in ordre:
            if not deja_vu[n]:
                chaines.append([])
                parcours_decomposition_chaine(n, t)
                indice_chaine += 1
                
        return chaines
    
    
    # code
    lance_parcours()
    print("---------- DECOMPO EN CHAINES ----------")
    decomposition_en_chaines()
    
    print(chaines)
    
    print(est_connexe())
    print(f'ordre DFI {ordre_dfi}')
    
    return arbre_parcours


# In[283]:


a = parcours_graphe(exemple)


# In[270]:


plot_couleur(a)


# In[251]:


a = parcours_graphe(g)
ordre = [4, 3, 2, 1, 9, 8, 7, 6, 5, 0, 28, 25]


# In[240]:


plot_couleur(a)


# In[151]:


b = parcours_graphe(graphs.CompleteGraph(4))
plot_couleur(b)


# In[49]:


e = DiGraph()
e.add_vertices(g.vertices())
e


# In[44]:


type(g.vertices())


# In[165]:


g = DiGraph(g)
g


# In[ ]:





# In[40]:


len(g)


# In[162]:


g.add_edge([25, 28])


# In[154]:


g.add_vertex(25)


# In[ ]:




