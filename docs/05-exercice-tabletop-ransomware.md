# Kit d'exercice sur table — « Récolte chiffrée » (rançongiciel)

> **EXERCICE SIMULÉ.** Tout ce chapitre décrit un exercice de discussion. Aucun système n'est touché, aucun outil n'est lancé. Les noms, chiffres et événements sont fictifs.

## 1. Fiche d'identité de l'exercice

| Élément | Valeur |
|---|---|
| Format | Exercice sur table (discussion), salle de réunion, 2 h 30 dont 30 min de débriefing |
| Participants | Gérant (directeur de crise), RAF (référent données), informaticien (RI), un commercial, le chef de station logistique ; prestataire IT invité (en visio) |
| Animation | 1 animateur (facilitateur) + 1 observateur preneur de notes |
| Playbook testé | AGS-PB-B Rançongiciel ; politique AGS-POL-IR-01 |
| Objectifs | O1 : isoler correctement et vite. O2 : activer la cellule de crise et le canal hors bande. O3 : vérifier que les sauvegardes permettent de repartir (RPO/RTO). O4 : prendre et justifier la décision sur la rançon. O5 : produire des communications internes et clients exactes. O6 : identifier les démarches légales (plainte, CNDP, maCERT). |
| Hors périmètre | Investigation technique détaillée, négociation réelle |

## 2. Guide de l'animateur

**Avant (J-14 à J-1)**

- Valider la date avec le gérant ; bloquer 2 h 30 sans téléphone (sauf pour les injects).
- Imprimer : playbook B, fiche réflexe B, politique (section rôles et autorités), annuaire de crise, cartes d'injects (une par inject, à distribuer au fil de l'eau).
- Préparer un tableau blanc avec une **ligne de temps** et trois colonnes : Décisions / Actions / Questions ouvertes.
- Ne pas communiquer le scénario aux participants.

**Pendant**

- Rappeler les règles en ouverture (5 min) : environnement sans jugement, on joue « comme si », pas de bonne réponse unique, on dit « je ne sais pas » plutôt que d'inventer, le temps de l'exercice est accéléré.
- Lire chaque inject à voix haute, distribuer la carte, laisser **10 à 20 min** de discussion, puis poser les questions prévues.
- Ne pas donner la solution ; relancer avec « Qui fait quoi ? Comment le savez-vous ? Où est-ce écrit ? ».
- Si le groupe bloque plus de 5 min, donner un indice (« Que dit la fiche réflexe ? »).
- L'observateur note les **heures fictives** des décisions et les écarts par rapport au playbook.

**Après**

- Débriefing à chaud de 30 min (ce qui a bien marché / ce qui a manqué / 3 actions prioritaires).
- Rapport post-exercice (RETEX) envoyé sous 10 jours ouvrés ; plan d'actions suivi en réunion mensuelle.

## 3. Scénario et injects

**Situation de départ (lue par l'animateur).** Mardi, 8 h 40, pleine saison d'export des agrumes. Le bureau tourne à plein ; trois camions doivent partir à 14 h avec des documents d'export et des factures.

| N° | Heure fictive | Inject (ce qui est annoncé aux participants) | Ce qu'on attend | Questions à poser |
|---|---|---|---|---|
| 1 | 08:40 | Salma (commerciale) appelle : « Mes fichiers Excel ne s'ouvrent plus, ils finissent tous par `.agrlck`, et il y a un fichier `LISEZ-MOI.txt` sur mon bureau. » | Reconnaître un rançongiciel probable ; isoler le poste sans l'éteindre ; ouvrir le registre | Que dit-on à Salma, mot pour mot ? Qui décide ? Éteint-on le PC ? |
| 2 | 09:05 | Le chef de station signale que le dossier partagé « EXPORT » sur le NAS contient aussi des fichiers `.agrlck`. Deux autres postes affichent la note. | Passer en S1 ; couper le NAS ; débrancher le disque USB de sauvegarde ; appeler le gérant ; activer le groupe de crise hors bande | Quel niveau de gravité ? Qui appelle qui, et par quel canal ? Que fait-on du disque USB branché sur le NAS ? |
| 3 | 10:00 | L'informaticien constate que le disque USB de la nuit est **lui aussi chiffré** (il était branché en permanence). La dernière copie hors site date d'il y a **6 jours**. Le prestataire IT peut venir à 15 h. | Évaluer la perte (6 jours) ; prioriser la restauration ; organiser un mode dégradé (documents d'export à la main, depuis les courriels Gmail) | Qu'est-ce qui est vraiment critique aujourd'hui ? Comment faire partir les camions à 14 h ? Qu'avions-nous promis comme RPO ? |
| 4 | 11:30 | Un courriel arrive sur l'adresse de contact : l'attaquant réclame l'équivalent de **8 000 USD en crypto-actifs** sous 72 h, et affirme avoir **copié la base clients et les factures**, avec une capture d'écran de dossiers internes en preuve. | Ne pas répondre à chaud ; conserver le message ; prendre en compte la double extorsion ; appeler l'avocat ; préparer la décision sur la rançon | Paie-t-on ? Qui décide, sur quels critères ? Quelles conséquences juridiques et pratiques ? Le vol de données change-t-il nos obligations ? |
| 5 | 13:00 | Un client B2B important, à Agadir, appelle : il a entendu « qu'AgriSouss a été piraté » et demande si ses données et ses commandes sont en danger. Un salarié a publié « journée galère, tout est planté » sur un réseau social. | Message client factuel et prudent ; rappel interne sur la communication ; porte-parole unique | Que lui répond-on exactement ? Que fait-on de la publication du salarié ? Faut-il prévenir les autres clients maintenant ? |
| 6 | 16:30 | Le prestataire identifie le vecteur probable : un **accès bureau à distance exposé** sur un PC avec un mot de passe faible, activé l'an dernier pour du télétravail. Il propose de réinstaller les trois postes et de restaurer le NAS depuis la copie hors site. | Valider le plan d'éradication et de restauration ; changer les mots de passe ; fermer l'accès distant ; plainte ; démarches CNDP et maCERT ; planifier le retour d'expérience | Qu'est-ce qui garantit qu'on ne sera pas réinfectés ? Qui dépose plainte et avec quelles preuves ? Que dit-on à la CNDP, et faut-il la contacter ? Quand clôture-t-on ? |

**Inject de réserve (si le groupe va vite)** : 18 h — le gérant reçoit un SMS de « la banque » demandant de confirmer un virement urgent. Test : hameçonnage opportuniste pendant la crise, vérification hors bande.

## 4. Questions transverses aux participants

1. Où se trouve la liste des numéros d'urgence si les PC et le NAS sont inaccessibles ?
2. Qui a l'autorité pour couper le NAS ou Internet pendant les heures de travail ?
3. Comment savons-nous que la copie hors site n'est pas elle aussi compromise ?
4. Combien de jours de travail pouvons-nous perdre sans conséquence grave ? Le savions-nous avant aujourd'hui ?
5. Quels documents pouvons-nous reconstituer depuis Gmail / Drive, et lesquels sont perdus ?
6. Qu'est-ce qui est obligatoire pour nous vis-à-vis de la CNDP, de la DGSSI / maCERT et de la police, et qu'est-ce qui est seulement recommandé ?
7. Quelle est notre position sur le paiement d'une rançon, et est-elle écrite quelque part ?
8. Qui parle aux clients, à la presse, aux salariés ?
9. Quelles preuves faut-il garder pour la plainte et comment les conserve-t-on ?
10. Qu'aurions-nous dû avoir en place avant pour que cet incident soit mineur ?

## 5. Grille d'évaluation

Notation par l'observateur : 0 = non réalisé, 1 = partiel ou tardif, 2 = conforme au playbook.

| N° | Critère | Objectif lié | Attendu | Note (0-2) | Commentaire |
|---|---|---|---|---|---|
| E1 | Isolement réseau du premier poste sans extinction | O1 | < 10 min fictives après l'inject 1 | | |
| E2 | Coupure du NAS et protection de la sauvegarde | O1 | Dès l'inject 2 | | |
| E3 | Classement S1 et escalade au gérant | O2 | Inject 2 | | |
| E4 | Utilisation d'un canal de crise hors bande | O2 | Inject 2 | | |
| E5 | Registre d'incident tenu (heures, décisions) | O2 | Tout l'exercice | | |
| E6 | Évaluation RPO/RTO et priorités métier | O3 | Inject 3 | | |
| E7 | Mode dégradé pour la continuité (camions de 14 h) | O3 | Inject 3 | | |
| E8 | Décision rançon argumentée, avis juridique, refus par défaut | O4 | Inject 4 | | |
| E9 | Prise en compte de la double extorsion (données) | O4/O6 | Inject 4 | | |
| E10 | Message client exact, sans promesse non vérifiée | O5 | Inject 5 | | |
| E11 | Message interne et gestion de la publication du salarié | O5 | Inject 5 | | |
| E12 | Préservation des preuves et chaîne de possession | O6 | Injects 1 à 6 | | |
| E13 | Démarches : plainte, CNDP (recommandé), maCERT (volontaire) | O6 | Inject 6 | | |
| E14 | Cause racine traitée avant reconnexion | O1/O3 | Inject 6 | | |
| | **Total** | | | **/28** | |

Lecture : 24-28 dispositif mature ; 16-23 base solide avec écarts ; 8-15 dispositif à renforcer ; < 8 dispositif à construire.

## 6. Exemple de rapport post-exercice (RETEX)

> **EXERCICE SIMULÉ — RAPPORT D'EXEMPLE.** Ce rapport illustre le format attendu. Il ne décrit **aucun** incident réel ni aucun exercice qui aurait été mené dans une entreprise réelle. Les résultats sont inventés pour l'illustration.

| Élément | Valeur |
|---|---|
| Exercice | « Récolte chiffrée » — rançongiciel, format sur table |
| Date (fictive) | Jeudi 2026-11-12, 9 h 00 - 11 h 30 |
| Participants | Gérant, RAF, informaticien, commerciale, chef de station ; prestataire IT en visio |
| Animateur / observateur | Animateur externe (fictif) / observateur : stagiaire administratif |
| Score | **17 / 28** — base solide avec écarts importants |

**Synthèse.** L'équipe a réagi vite au premier signalement et a correctement isolé le poste sans l'éteindre. La coupure du NAS a été décidée rapidement, mais personne n'a pensé au disque USB de sauvegarde branché en permanence, ce qui, dans le scénario, a fait perdre 6 jours de données. La décision de ne pas payer a été prise et justifiée, mais la position n'était écrite nulle part avant l'exercice. La communication client a été improvisée et contenait au départ une promesse non vérifiée (« aucune donnée n'a été volée »).

**Chronologie fictive des décisions**

| Heure fictive | Décision / action | Écart |
|---|---|---|
| 08:46 | Poste de Salma débranché du réseau, laissé allumé | Conforme |
| 09:12 | Classement S1, appel du gérant par téléphone | Conforme |
| 09:20 | NAS débranché du réseau | Conforme ; disque USB oublié (E2 = 1) |
| 09:35 | Groupe WhatsApp de crise improvisé | Groupe non créé à l'avance, numéro du prestataire introuvable (E4 = 1) |
| 10:40 | Mode dégradé : documents d'export refaits depuis Gmail | Bonne idée, venue du chef de station |
| 11:50 | Refus de payer, appel de l'avocat | Avocat non référencé à l'avance |
| 13:10 | Réponse au client : « aucune donnée volée » | Promesse non vérifiée, corrigée par le RAF (E10 = 1) |
| 16:45 | Plan de réinstallation validé ; plainte décidée | CNDP et maCERT évoqués seulement sur relance de l'animateur (E13 = 1) |

**Notes par critère** : E1 2, E2 1, E3 2, E4 1, E5 0 (registre non tenu, notes éparses), E6 1, E7 2, E8 2, E9 1, E10 1, E11 1, E12 0, E13 1, E14 2 → **17/28**.

**Points forts**

- Réflexe d'isolement sans extinction acquis.
- Bonne idée de mode dégradé à partir de Gmail pour les documents d'export.
- Refus de payer argumenté (aucune garantie, financement du crime, double extorsion qui reste possible même après paiement).

**Axes d'amélioration**

1. Sauvegarde : le disque USB toujours branché n'est pas une copie hors ligne.
2. Pas d'annuaire de crise papier ni de groupe de crise créé à l'avance.
3. Preuves : personne n'a parlé de photographier la note, de conserver le courriel de l'attaquant ni de la chaîne de possession (E12 = 0).
4. Communication : pas de modèle préparé, promesse non vérifiée.
5. Obligations légales mal connues (confusion entre CNDP obligatoire et recommandée, maCERT inconnu de la direction).

**Plan d'actions**

| N° | Action | Responsable | Échéance | Priorité |
|---|---|---|---|---|
| A1 | Mettre en place une rotation de 2 disques USB, dont un toujours débranché et emporté hors site ; ou une sauvegarde cloud immuable | Informaticien | 2026-12-15 | Haute |
| A2 | Test de restauration du NAS chronométré, puis trimestriel | Informaticien + prestataire | 2026-12-31 | Haute |
| A3 | Créer le groupe de crise et l'annuaire papier (coffre + domicile du gérant) | RAF | 2026-11-30 | Haute |
| A4 | Fermer tout accès bureau à distance exposé ; recenser les accès distants | Prestataire | 2026-11-30 | Haute |
| A5 | Écrire la position « rançon » dans la politique, validée par le gérant et l'avocat | Gérant | 2026-12-31 | Moyenne |
| A6 | Imprimer les fiches réflexes et les afficher ; former les salariés en 30 min | Informaticien | 2027-01-15 | Moyenne |
| A7 | Préparer les modèles de communication clients validés par l'avocat | RAF | 2027-01-31 | Moyenne |
| A8 | Rejouer un exercice (scénario BEC) | Informaticien | 2027-05 | Basse |
