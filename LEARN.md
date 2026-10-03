# LEARN — Réponse aux incidents pour une PME

Notes de révision qui accompagnent le projet. Elles expliquent les choix faits dans les playbooks et préparent aux entretiens (stage, PFE, poste SOC / GRC junior).

## 1. NIST SP 800-61 et SANS PICERL : deux découpages du même travail

| NIST SP 800-61 r2 (2012) | SANS PICERL | Ce qu'on fait concrètement |
|---|---|---|
| 1. Préparation | P — Preparation | Politique, rôles, contacts, sauvegardes testées, journaux activés, exercices |
| 2. Détection et analyse | I — Identification | Recevoir l'alerte, qualifier (événement ou incident ?), fixer la gravité, établir le périmètre |
| 3. Confinement, éradication et rétablissement | C — Containment, E — Eradication, R — Recovery | Arrêter la propagation, retirer la cause, revenir à un état sain et surveillé |
| 4. Activité post-incident | L — Lessons learned | Retour d'expérience, plan d'actions, indicateurs |

Différences à retenir :

- NIST regroupe C, E et R en **une seule phase**, parce qu'en pratique on boucle entre elles (on confine, on découvre un autre poste touché, on reconfine). SANS les sépare pour qu'on n'en oublie aucune.
- NIST insiste sur le fait que le cycle est **circulaire** : la phase post-incident nourrit la préparation, et la détection peut renvoyer à l'analyse.
- **NIST SP 800-61 Rev. 3 (avril 2025)** remplace la Rev. 2. Elle ne propose plus son propre cycle : elle est écrite comme un **profil communautaire du CSF 2.0** et répartit la réponse aux incidents dans les six fonctions *Govern, Identify, Protect, Detect, Respond, Recover*. Idée clé : la réponse aux incidents n'est pas un service à part, c'est une partie de la gestion des risques de l'organisation. Préparation = surtout *Govern / Identify / Protect* ; détection = *Detect* ; traitement = *Respond* ; reprise = *Recover* ; amélioration = *Identify (Improvement)*.
- Pour une PME, le découpage en phases reste le plus simple à enseigner ; la correspondance CSF 2.0 sert à parler le même langage qu'un auditeur.

## 2. Stratégies de confinement

Le confinement achète du temps. Il doit être **rapide, réversible si possible, et documenté**.

| Stratégie | Exemple PME | Avantage | Inconvénient |
|---|---|---|---|
| Isolement réseau d'un poste | Débrancher le câble, couper le Wi-Fi | Immédiat, garde la mémoire | Le poste reste inutilisable |
| Coupure d'un service | Mettre le site en maintenance, couper le NAS | Stoppe la propagation et l'exposition | Impact métier direct |
| Désactivation de comptes / révocation de sessions | Réinitialiser le mot de passe Google + déconnecter les sessions + révoquer OAuth | Coupe l'accès de l'attaquant au cloud | Doit être complet, sinon l'attaquant garde un jeton |
| Blocage | Bloquer un domaine expéditeur, une IP sur l'admin du site | Simple | Contournable |
| Segmentation d'urgence | Couper le bureau d'Internet | Stoppe l'exfiltration et le contrôle à distance | Arrête tout le monde |
| Observation contrôlée | Laisser l'attaquant actif pour comprendre | Renseignement | **Réservé à des équipes expérimentées** ; non adapté à une PME |

Critères de choix (repris de NIST r2) : risque de dommages supplémentaires, besoin de préserver les preuves, disponibilité du service, temps et ressources, efficacité, durée de la solution (temporaire ou définitive).

Piège classique : **avertir l'attaquant** (par exemple en changeant un seul mot de passe alors qu'il a d'autres accès) avant d'avoir le périmètre complet. En PME, on accepte souvent ce risque parce que la priorité est de stopper la fraude ou le chiffrement.

## 3. Ordre de volatilité des preuves (RFC 3227)

On collecte d'abord ce qui disparaît le plus vite :

1. Registres et cache du processeur ;
2. Table de routage, cache ARP, table des processus, statistiques noyau, **mémoire vive** ;
3. Systèmes de fichiers temporaires ;
4. **Disque** ;
5. Journalisation et supervision à distance (journaux Google Workspace, hébergeur, pare-feu) ;
6. Configuration physique et topologie réseau ;
7. Supports d'archive (sauvegardes).

Remarques pratiques :

- En PME, les étapes 1 à 3 demandent un prestataire compétent ; le salarié et l'informaticien doivent surtout **ne pas détruire** : isoler sans éteindre, photographier, ne pas « nettoyer ».
- Dans le cloud, l'ordre est différent : les journaux distants (5) sont souvent **la seule preuve**, et leur **rétention est limitée**. Il faut les exporter tôt.
- Chaque preuve : empreinte SHA-256, horodatage, fiche de **chaîne de possession** (qui, quoi, quand, où, transferts).

## 4. Pourquoi ne pas payer une rançon, et les aspects juridiques

Raisons pratiques :

- **Aucune garantie** : le déchiffreur peut être lent, buggé, ou ne jamais arriver.
- **Double extorsion** : payer ne garantit pas que les données volées seront supprimées ; elles peuvent être revendues ou republiées.
- **Récidive** : une victime qui paie est connue comme solvable et peut être ciblée de nouveau.
- On **finance** des groupes criminels et leurs prochaines attaques.
- Le paiement ne dispense ni de l'éradication, ni de la reconstruction, ni des obligations envers les personnes dont les données ont fuité.

Aspects juridiques (lecture d'étudiant, à faire valider par un avocat) :

- Au Maroc, à ma connaissance, aucun texte n'interdit expressément à une entreprise privée de payer une rançon, mais le paiement soulève plusieurs problèmes : la **réglementation des changes** (paiement à l'étranger, et position de l'Office des changes et de Bank Al-Maghrib sur les monnaies virtuelles, rappelée depuis 2017 ; un cadre légal des crypto-actifs est en préparation, à vérifier au moment des faits) ; le risque de payer un groupe ou une personne visés par des **sanctions internationales** (par exemple les listes de l'OFAC américain), ce qui peut exposer l'entreprise vis-à-vis de ses partenaires et banques étrangers ; la **fiscalité et la comptabilité** d'une dépense non justifiable.
- L'intrusion et le chiffrement sont des infractions (loi **07-03**, art. 607-3 et suivants du Code pénal) ; l'extorsion aussi. **Porter plainte** est recommandé dans tous les cas.
- La position par défaut de la politique est donc le **refus**, et toute étude de paiement exige une décision écrite du gérant après avis juridique.
- Les autorités (CISA, ANSSI, maCERT, Europol via No More Ransom) recommandent de **ne pas payer**.

## 5. Communication de crise

- **Un porte-parole**, des messages préparés, validés par la direction (et l'avocat si données personnelles).
- Structure d'un message : ce qui s'est passé (factuel), ce qu'on a fait, ce que la personne doit faire, quand on reviendra vers elle, qui contacter.
- Ne jamais affirmer ce qu'on n'a pas vérifié (« aucune donnée n'a été touchée »). Une communication fausse coûte plus cher qu'une communication tardive.
- Canal **hors bande** (téléphone, groupe de messagerie créé à l'avance) : la messagerie de l'entreprise peut être compromise.
- Interne d'abord (consignes), puis partenaires exposés (fraude au RIB), puis clients.
- **Obligatoire ou recommandé ?** Pour une PME privée marocaine : la loi 09-08 impose de sécuriser les données (art. 23) mais, selon ma lecture, ne fixe pas d'obligation générale et explicite de notification de violation comme le RGPD (art. 33-34) ; contacter la CNDP et informer les personnes reste fortement recommandé. La déclaration d'incident à la DGSSI prévue par la loi 05-20 vise les administrations, établissements publics, IIV et certains opérateurs ; pour AgriSouss, le signalement à **maCERT** est volontaire. Si la boutique cible des clients dans l'UE, le RGPD peut s'appliquer (art. 3(2)) avec notification sous 72 h.

## 6. Quinze questions d'entretien et réponses modèles

**1. Quelle est la différence entre un événement et un incident ?**
Un événement est un fait observable (connexion, alerte, courriel reçu). Un incident est un événement, ou une suite d'événements, qui compromet ou menace la confidentialité, l'intégrité ou la disponibilité, ou qui viole la politique de sécurité. Le triage sert justement à passer de l'un à l'autre.

**2. Citez les phases de NIST 800-61 r2 et de SANS PICERL.**
NIST r2 : préparation ; détection et analyse ; confinement, éradication et rétablissement ; activité post-incident. SANS : Preparation, Identification, Containment, Eradication, Recovery, Lessons learned. Même contenu, SANS sépare C, E et R.

**3. Qu'apporte NIST 800-61 Rev. 3 ?**
Publiée en avril 2025, elle remplace la Rev. 2 et intègre la réponse aux incidents dans le CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover). Le message : la réponse aux incidents fait partie de la gestion globale des risques, avec une gouvernance explicite, et pas seulement d'une équipe technique.

**4. Un salarié dit avoir saisi son mot de passe Google sur une fausse page. Que faites-vous dans les 15 premières minutes ?**
Je réinitialise le mot de passe, je déconnecte toutes ses sessions, je révoque les jetons OAuth et mots de passe d'application inconnus, je vérifie les méthodes MFA. Ensuite je regarde le journal de connexion et les paramètres Gmail (transferts, filtres, délégations) en capturant avant de supprimer. Si une demande de paiement est en jeu, j'appelle la banque immédiatement.

**5. Pourquoi changer le mot de passe ne suffit pas ?**
Parce que l'attaquant peut garder une session ouverte (cookie), un jeton OAuth accordé à une application, un mot de passe d'application, une règle de transfert qui continue d'envoyer les messages, ou une méthode MFA qu'il a ajoutée. Il faut traiter tous ces accès.

**6. Qu'est-ce qu'une fraude BEC et comment la prévenir ?**
*Business Email Compromise* : l'attaquant utilise une vraie boîte compromise ou usurpe un correspondant pour obtenir un virement (changement de RIB, faux président). Prévention : MFA forte, DMARC, blocage du transfert automatique externe, et surtout une **procédure de vérification par téléphone** sur un numéro connu pour tout changement de coordonnées bancaires.

**7. Ransomware : faut-il éteindre le poste ?**
Par défaut non : on l'isole du réseau, ce qui stoppe la propagation tout en gardant la mémoire, utile à l'analyse. Si le chiffrement local continue et qu'on ne peut pas l'arrêter autrement, on peut mettre en veille prolongée ou couper : on sacrifie des preuves pour sauver des données. La décision et l'heure sont notées.

**8. Qu'est-ce que la règle 3-2-1-1-0 ?**
Trois copies des données, sur deux supports différents, dont une hors site, une hors ligne ou immuable, et zéro erreur lors des tests de restauration. Le « 1 hors ligne » est ce qui sauve contre un rançongiciel : un disque USB branché en permanence se fait chiffrer comme le reste.

**9. Donnez l'ordre de volatilité des preuves.**
Selon la RFC 3227 : registres et cache ; tables réseau, processus et mémoire vive ; fichiers temporaires ; disque ; journaux distants ; configuration physique et topologie ; archives. Dans le cloud, les journaux distants deviennent prioritaires car leur rétention est limitée.

**10. Qu'est-ce que la chaîne de possession et pourquoi est-elle importante ?**
C'est la traçabilité de chaque preuve : qui l'a collectée, quand, comment, avec quelle empreinte, où elle est stockée et à qui elle a été transmise. Sans elle, une preuve peut être contestée devant un juge, un assureur ou dans un litige commercial.

**11. Le site e-commerce contient un web shell. Pourquoi ne pas simplement supprimer le fichier ?**
Parce que je perds la preuve et la compréhension de l'attaque, et que l'attaquant a souvent d'autres accès (autres fichiers, compte admin ajouté, identifiants de base volés). Je demande d'abord un instantané et les journaux à l'hébergeur, je mets le site en maintenance, je change tous les secrets, puis je reconstruis depuis un code et une sauvegarde sains après avoir corrigé la faille.

**12. Une PME marocaine doit-elle notifier la CNDP en cas de fuite ?**
Selon ma lecture, la loi 09-08 impose de sécuriser les traitements mais ne prévoit pas d'obligation générale explicite de notification avec délai, contrairement au RGPD. Je recommande quand même de contacter la CNDP et d'informer les personnes exposées, et je ferais valider par un juriste, d'autant qu'une réforme est en discussion et que le RGPD peut s'appliquer si l'on cible des clients européens.

**13. Et maCERT / la DGSSI ?**
maCERT est le CERT national, rattaché à la DGSSI. La loi 05-20 impose la déclaration des incidents aux administrations, établissements publics, infrastructures d'importance vitale et certains opérateurs. Pour une PME privée hors de ce périmètre, le signalement est volontaire mais utile : aide à la qualification et meilleure connaissance des menaces au niveau national.

**14. Quels indicateurs suivez-vous pour mesurer la réponse aux incidents ?**
MTTD (temps moyen de détection), MTTA (prise en charge), MTTC (confinement), MTTR (rétablissement), plus des indicateurs de préparation : taux de succès des tests de restauration, taux de signalement et de clic aux campagnes d'hameçonnage, délai d'application des correctifs. Il faut définir précisément le point de départ et d'arrivée de chaque mesure, sinon les chiffres ne sont pas comparables.

**15. À quoi sert un exercice sur table et comment l'évaluez-vous ?**
À tester les décisions, les rôles et la communication sans toucher aux systèmes. On fait vivre un scénario par injects chronométrés, un observateur note les heures de décision et les écarts au playbook, on note une grille de critères et on termine par un retour d'expérience avec un plan d'actions daté et attribué. L'exercice réussi est celui qui révèle des manques, pas celui où tout se passe bien.

## 7. Ligne de CV (honnête)

> Rédigé un dispositif de réponse aux incidents pour une PME fictive (politique avec RACI et niveaux de gravité, 3 playbooks BEC / rançongiciel / site web alignés NIST SP 800-61 et SANS PICERL, kit d'exercice sur table avec grille d'évaluation et RETEX simulé), et un générateur PDF Python (reportlab) à partir des sources Markdown.

Ce qu'il ne faut **pas** écrire : « géré des incidents réels » ou « mené un exercice de crise en entreprise ». Ce projet est un travail documentaire et un exercice simulé.
