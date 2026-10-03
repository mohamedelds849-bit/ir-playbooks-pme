# Revue sécurité / QA — IR Playbooks PME

Relecteur : « Security Reviewer » (relecture type incident responder senior + QA), 2026-10-03.
Périmètre : `docs/00` à `docs/06`, `README.md`, `LEARN.md`, `build/build_pdf.py`, `diagrams/*.mmd`, `output/AgriSouss-Reponse-Incidents.pdf` (régénéré et relu page par page, 29 pages).

| Critère | Résultat |
|---|---|
| Note technique | 8/10 |
| Note pédagogique | 8/10 |
| Sécurité (contenu défensif uniquement) | PASS |
| Cohérence docs / PDF / README | PASS (après corrections) |
| Verdict | **APPROUVÉ** (avec recommandations) |

## 1. Ce qui est solide

- **Cadre** : les phases de NIST SP 800-61 r2, SANS PICERL, la Rev. 3 (avril 2025, profil communautaire CSF 2.0, six fonctions), ID.IM pour l'amélioration continue, et les catégories CSF 2.0 citées (DE.CM, DE.AE, RS.MA, RS.AN, RS.MI, RS.CO, RC.RP, RC.CO) sont exacts. Les critères de choix du confinement correspondent à NIST r2 §3.3.1.
- **RFC 3227** : l'ordre de volatilité est complet et exact, et la remarque sur le cloud (journaux distants = souvent la seule preuve, rétention limitée) est juste.
- **BEC / Google Workspace** : la séquence est la bonne (réinitialisation, déconnexion des sessions / cookies, révocation OAuth et mots de passe d'application, revue des méthodes 2SV, capture *avant* suppression des règles, `.eml` avec en-têtes complets, banque appelée immédiatement, vérification hors bande). Les noms d'alertes cités existent. Les réserves sur l'édition (outil d'enquête) sont honnêtes.
- **Rançongiciel** : isoler sans éteindre, couper le NAS, débrancher la sauvegarde USB, suspendre la synchronisation cloud, changer les mots de passe depuis un poste sain, réinstaller au lieu de « nettoyer », cause racine avant reconnexion, 3-2-1-1-0, No More Ransom, avertissement sur le téléversement d'échantillons : tout est correct.
- **Site web** : « préserver avant de nettoyer » (instantané hébergeur), changement de tous les secrets, comparaison avec une source de référence, PHP interdit dans le dossier d'envoi, réexamen Search Console, ne pas télécharger la base fuitée : pratiques correctes.
- **Juridique** : formulations prudentes et justes. Loi 09-08 art. 23 (sécurité) ; pas d'obligation générale explicite de notification de violation (bien présenté comme « selon notre lecture ») ; loi 05-20 / décret 2-21-406 avec déclaration obligatoire limitée à un périmètre défini ; loi 07-03 = art. 607-3 à 607-11 du Code pénal ; RGPD art. 3(2) et 72 h ; police 19. Rien n'est affirmé de façon abusive.
- **Tabletop** : grille sur 28 cohérente (14 critères × 2), somme du RETEX vérifiée (17/28, bonne tranche de lecture), date fictive cohérente (jeudi 12/11/2026), RETEX clairement marqué **SIMULÉ**.
- **Ligne de CV** : honnête, avec la liste explicite de ce qu'il ne faut pas écrire.
- **Sécurité** : aucun contenu offensif, aucune commande d'attaque, pas de vraie URL malveillante ; avertissements présents dans le README, l'introduction et le PDF.

## 2. Problèmes trouvés

| # | Gravité | Fichier | Problème |
|---|---|---|---|
| P1 | Moyenne (exactitude) | `docs/02` | Le scénario « changement de RIB » était appelé « fraude au président ». La fraude au président est une usurpation du dirigeant ; une demande de changement de RIB envoyée à un client, c'est une fraude au faux fournisseur / au changement de RIB. Un recruteur peut relever la confusion. |
| P2 | Moyenne (exactitude) | `docs/03`, `LEARN.md` Q7 | Le texte disait que la mise en veille prolongée faisait perdre la mémoire vive. C'est faux : l'hibernation écrit la mémoire dans `hiberfil.sys`, qui reste exploitable par un analyste. C'est justement ce qui la rend préférable à une coupure brutale. |
| P3 | Faible (exactitude) | `docs/04` modèle client | « mot de passe chiffré » : les mots de passe doivent être **hachés**, pas chiffrés. Un recruteur SOC le remarquera. |
| P4 | Faible (rendu PDF) | `build_pdf.py` | Des titres « 3. Arbre de décision » restaient seuls en bas de page (p. 10, 14, 18), avec le diagramme renvoyé à la page suivante. La légende Mermaid était aussi séparée de son bloc. |
| P5 | Faible (cohérence) | `docs/05` RETEX vs `docs/01` | Le RETEX d'exemple dit que la position sur la rançon « n'était écrite nulle part », alors que la politique v1.0 la contient (principe 4). Ça se défend (le RETEX aurait précédé la v1.0, d'où l'action A5), mais ce n'est pas dit. **Non corrigé** : voir R5. |
| P6 | Faible (rendu PDF) | PDF p. 24 | Le libellé en gras « Chronologie fictive des décisions » reste seul en bas de page, avec son tableau en page 25. Purement esthétique. |

## 3. Corrections appliquées (commit sur `master`)

1. `docs/02-playbook-phishing-bec.md` : « fraude au président / BEC » remplacé par « fraude au changement de RIB / faux fournisseur, forme courante de BEC » (P1).
2. `docs/03-playbook-ransomware.md` : paragraphe « Éteindre ou non ? » corrigé. L'hibernation écrit la mémoire dans `hiberfil.sys` ; la coupure d'alimentation, en dernier recours, perd la mémoire vive (P2).
3. `LEARN.md` Q7 : même correction dans la réponse d'entretien (P2).
4. `docs/04-playbook-compromission-site-web.md` : « mot de passe chiffré » remplacé par « mot de passe stocké sous forme hachée » (P3).
5. `build/build_pdf.py` : `keepWithNext` ajouté sur les titres h2, h3 et h4 et sur la légende des diagrammes Mermaid. Les titres et légendes ne restent plus seuls en bas de page (P4).
6. `output/AgriSouss-Reponse-Incidents.pdf` régénéré (29 pages ; sommaire et signets OK ; accents, □ et → rendus ; une fiche réflexe par page, p. 27-29).
7. Ajout de ce fichier `REVIEW.md`.

## 4. Recommandations restantes (non appliquées, à décider par l'auteur)

- **R1 — Loi 05-20, périmètre exact.** Citer la liste complète des assujettis : administrations, collectivités, établissements et entreprises publics, IIV, plus exploitants de réseaux publics de télécoms, FAI, prestataires de services de cybersécurité, prestataires de services numériques et éditeurs de plateformes Internet. Expliquer en une phrase pourquoi une petite boutique en ligne n'est *a priori* pas un « éditeur de plateforme ». Question d'entretien probable chez DGSSI, un intégrateur ou un cabinet.
- **R2 — Loi 09-08, angle GRC manquant.** Ajouter deux points dans la Préparation : (a) la déclaration préalable à la CNDP du traitement « clients » ; (b) Google Workspace héberge les données hors du Maroc, ce qui pose la question du **transfert vers l'étranger** (art. 43-44, autorisation CNDP selon le pays). Ces deux points font très bien en entretien GRC.
- **R3 — Sources à vérifier.** LEARN §4 affirme que maCERT recommande de ne pas payer. Ajouter une référence (bulletin, guide) ou retirer maCERT de la liste. Même chose pour la référence et la date du décret 2-21-406 (juillet 2021), à recouper sur le Bulletin officiel.
- **R4 — Playbook A, compléments utiles.** Vérifier aussi l'adresse et le téléphone de **récupération** du compte (souvent modifiés par l'attaquant). Prévoir une variante « compte super administrateur compromis » : passer par un second super admin, revoir les rôles et les journaux Admin. Préciser que la purge en masse via l'outil d'enquête demande une édition Enterprise ; en Business, le recours est la recherche dans le journal des e-mails plus une action par destinataire.
- **R5 — Cohérence RETEX / politique.** Ajouter une phrase du type « exercice mené avant l'adoption de la v1.0 de la politique » (P5), ou reformuler « la position n'était pas connue des participants ».
- **R6 — PDF.** Les diagrammes Mermaid restent en texte, ce qui pèse le plus sur l'impression visuelle pour un recruteur qui ne lit que le PDF. Option : les rendre en PNG/SVG avec `mmdc` (mermaid-cli) et les intégrer. Autres points : fixer la date de couverture (aujourd'hui `date.today()`, donc non reproductible) et garder la ligne en gras de la p. 24 avec son tableau (P6).
- **R7 — Rançongiciel.** Ajouter un point de triage sur les indices d'exfiltration : volumes sortants, outils de synchronisation ou de transfert installés récemment, journaux de la box. C'est cohérent avec la double extorsion déjà évoquée.
- **R8 — Entretien.** Préparer une version anglaise de la ligne de CV et une réponse orale de 60 secondes : pourquoi garder les phases r2 alors que la r3 l'a remplacée (la justification est déjà dans l'introduction, il faut savoir la dire).

## 5. Verdict

**APPROUVÉ.** Le dossier est techniquement juste, prudent sur le droit marocain, honnête sur son caractère fictif et simulé, et utilisable en entretien. Les trois erreurs factuelles relevées (P1 à P3) sont corrigées, ainsi que le principal défaut de mise en page du PDF (P4). Les points restants (P5, P6, R1 à R8) sont des améliorations, pas des blocages.
