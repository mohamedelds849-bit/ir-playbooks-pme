# Introduction et périmètre

## Objet du document

Ce dossier rassemble le dispositif de réponse aux incidents de sécurité de **AgriSouss SARL**, PME agricole **fictive** de la région Souss-Massa (environ 15 salariés). Il complète le projet GRC (analyse de risques et politique de sécurité) bâti sur la même entreprise fictive. Il s'agit d'un **projet de portfolio** : l'entreprise, les personnes, les adresses et les incidents sont inventés.

Le dossier contient :

- une **politique de réponse aux incidents** (rôles, gravité, escalade, communication, preuves) ;
- trois **playbooks** opérationnels : hameçonnage et compte Google compromis (BEC), rançongiciel sur poste ou partage de fichiers, compromission du site e-commerce PHP ;
- un **kit d'exercice sur table** (tabletop) pour le scénario rançongiciel, avec un rapport post-exercice d'exemple **simulé** ;
- une **fiche réflexe** imprimable d'une page par playbook.

## Contexte de l'entreprise (hypothèses)

| Élément | Hypothèse retenue |
|---|---|
| Activité | Production et vente de produits agricoles (agrumes, primeurs, huile d'argan), B2B et vente en ligne |
| Effectif | ~15 personnes : gérant, administration/comptabilité (3), commercial (3), logistique/station (6), 1 informaticien polyvalent, stagiaires ponctuels |
| Messagerie | Google Workspace (Gmail, Drive, Meet), domaine `agrisouss.example` |
| Site web | Boutique PHP / MariaDB chez un hébergeur externe (hébergement mutualisé ou VPS géré), paiement par carte délégué à une page de paiement hébergée (type CMI) |
| Postes | ~14 PC Windows 10/11, 1 NAS de partage de fichiers au bureau, Wi-Fi bureau, imprimante réseau |
| Sauvegardes | NAS sauvegardé chaque nuit sur disque USB + copie hebdomadaire hors site (hypothèse à vérifier en exercice) |
| Sécurité | Antivirus Microsoft Defender, pas de SOC, pas de SIEM, 1 informaticien interne + prestataire externe sous contrat de maintenance |
| Assurance | Pas de police cyber au moment de la rédaction (point d'amélioration) |

## Référentiels utilisés

- **NIST SP 800-61 Rev. 2** (2012), *Computer Security Incident Handling Guide* : cycle en quatre phases — Préparation ; Détection et analyse ; Confinement, éradication et rétablissement ; Activité post-incident.
- **NIST SP 800-61 Rev. 3** (avril 2025), *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*. La Rev. 3 remplace la Rev. 2 et ne décrit plus un cycle propre : elle range la réponse aux incidents dans les six fonctions du **NIST CSF 2.0** (Govern, Identify, Protect, Detect, Respond, Recover). Ce dossier garde la structure en phases de la Rev. 2 / SANS parce qu'elle est plus simple pour une PME, et indique à chaque fois la fonction CSF 2.0 correspondante.
- **SANS PICERL** : Preparation, Identification, Containment, Eradication, Recovery, Lessons learned.
- **RFC 3227** : ordre de volatilité des preuves.
- Cadre marocain : **loi 09-08** (données personnelles, CNDP), **loi 05-20** (cybersécurité, DGSSI / maCERT), **loi 07-03** (articles 607-3 à 607-11 du Code pénal, atteintes aux systèmes de traitement automatisé de données).

## Correspondance des phases

| NIST 800-61 r2 | SANS PICERL | NIST CSF 2.0 (800-61 r3) | Dans ce dossier |
|---|---|---|---|
| Préparation | Preparation | Govern, Identify, Protect | Politique, sauvegardes, contacts, exercices |
| Détection et analyse | Identification | Detect, (Respond : analyse) | Déclencheurs, triage, arbre de décision |
| Confinement, éradication, rétablissement | Containment, Eradication, Recovery | Respond (mitigation), Recover | Étapes C / E / R des playbooks |
| Activité post-incident | Lessons learned | Identify (Improvement), Govern | Check-list post-incident, retour d'expérience |

## Limites et avertissements

- Contenu **uniquement défensif**. Aucune technique offensive n'est décrite.
- Les éléments juridiques sont une **lecture d'étudiant** des textes publics, pas un avis juridique. Ils doivent être validés par un avocat ou par la CNDP / DGSSI avant tout usage réel.
- Les noms de menus de la console Google Workspace changent régulièrement et certaines fonctions (outil d'enquête, journaux Gmail détaillés) dépendent de l'édition souscrite. Les chemins indiqués sont à vérifier sur la console réelle.
- Les diagrammes de décision sont fournis en **source Mermaid** (rendue graphiquement sur GitHub ou tout éditeur compatible). Dans le PDF, ils apparaissent sous forme de **source texte**, car le script de génération n'embarque pas de moteur de rendu Mermaid.
