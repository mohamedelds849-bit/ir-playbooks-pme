# Fiches réflexes (à imprimer et afficher)

Une page par playbook. À afficher près des postes et à glisser dans l'annuaire de crise papier. Les numéros sont à compléter.

<!-- pagebreak -->

## FICHE RÉFLEXE A — Courriel piégé / compte Google piraté

**Numéro d'alerte : RI [__________]  —  suppléant [__________]  —  gérant [__________]**

**Vous avez cliqué, saisi votre mot de passe ou validé une demande inattendue ? APPELEZ. Pas de reproche : la vitesse compte.**

**Signes d'alerte** : courriel « document partagé », « facture », « mot de passe expiré » avec lien de connexion ; demande MFA que vous n'avez pas déclenchée ; client qui vous répond à un message que vous n'avez pas envoyé ; demande urgente de changement de RIB ou de virement « confidentiel ».

| SALARIÉ — à faire | SALARIÉ — à ne pas faire |
|---|---|
| Appeler le RI **par téléphone** | Prévenir uniquement par courriel |
| Noter l'heure et ce que vous avez fait | Supprimer le courriel suspect (le signaler d'abord) |
| Signaler le courriel avec « Signaler l'hameçonnage » | Transférer le courriel à des collègues |
| Rester disponible pour le RI | Payer ou changer un RIB sans vérification par téléphone |

**RESPONSABLE INCIDENT — dans les 30 minutes**

1. □ Ouvrir le registre (heure, compte, constat) ; fixer la gravité (S1 si virement en jeu).
2. □ Réinitialiser le mot de passe, **déconnecter toutes les sessions**.
3. □ Révoquer applications tierces inconnues et mots de passe d'application ; vérifier les méthodes MFA.
4. □ Capturer **puis** supprimer : transferts, filtres, délégations, réponse automatique.
5. □ Exporter le journal de connexions ; enregistrer le courriel au format original (`.eml`).
6. □ Purger le courriel des autres boîtes ; bloquer expéditeur / domaine.
7. □ Paiement en jeu : **banque (service fraude) immédiatement**, client appelé sur son numéro connu.
8. □ Données personnelles exposées : référent données (CNDP recommandé).

**Clôture** : MFA forte activée, 14 jours sans activité suspecte, correspondants informés, retour d'expérience planifié.

| Contact de crise | Numéro / référence |
|---|---|
| Gérant (directeur de crise) / RAF (suppléant) | [__________] / [__________] |
| Prestataire IT (astreinte) / hébergeur (n° contrat) | [__________] / [__________] |
| Banque — service fraude / avocat | [__________] / [__________] |
| maCERT (DGSSI) — signalement volontaire / police (19) | [à vérifier sur dgssi.gov.ma] / 19 |

<!-- pagebreak -->

## FICHE RÉFLEXE B — Rançongiciel (fichiers chiffrés, note de rançon)

**Numéro d'alerte : RI [__________]  —  prestataire [__________]  —  gérant [__________]**

**Fichiers qui ne s'ouvrent plus, extension inconnue, message de rançon ? DÉBRANCHEZ LE RÉSEAU, N'ÉTEIGNEZ PAS, APPELEZ.**

**Signes d'alerte** : fichiers renommés avec une extension inconnue ; fichier `LISEZ-MOI` / `HOW_TO_DECRYPT` dans les dossiers ; fond d'écran remplacé ; alerte Defender « rançongiciel » ou antivirus désactivé ; PC ou NAS anormalement lents avec le disque qui tourne sans arrêt.

| SALARIÉ — à faire | SALARIÉ — à ne pas faire |
|---|---|
| Débrancher le câble réseau, couper le Wi-Fi | Éteindre ou redémarrer le PC |
| Appeler le RI immédiatement | Brancher une clé USB ou un disque pour « sauver » des fichiers |
| Photographier l'écran (note de rançon) | Répondre à l'attaquant, payer |
| Laisser le PC tel quel, poser une étiquette rouge | En parler à l'extérieur ou sur les réseaux sociaux |

**RESPONSABLE INCIDENT — dans les 30 minutes**

1. □ Isoler chaque poste touché ; **couper le NAS du réseau** ; **débrancher le disque de sauvegarde USB**.
2. □ Suspendre les synchronisations cloud ; bloquer les accès distants (bureau à distance, télémaintenance).
3. □ Classer S1/S2 ; appeler le gérant et le prestataire ; activer le **groupe de crise hors bande**.
4. □ Registre : postes touchés, heures, comptes, décisions (dont « éteindre ou non »).
5. □ Vérifier la dernière sauvegarde **hors ligne / hors site** saine (date, intégrité).
6. □ Désactiver les comptes utilisés ; changer les mots de passe **depuis un poste sain**.
7. □ Conserver note, fichiers chiffrés, courriels de l'attaquant (SHA-256, chaîne de possession).
8. □ Gérant + avocat : refus de payer par défaut ; plainte ; CNDP si vol de données (recommandé) ; maCERT (volontaire).

**Ne jamais reconnecter** un poste non réinstallé. Restaurer par priorité : facturation → commandes → dossiers → archives.

| Contact de crise | Numéro / référence |
|---|---|
| Gérant (directeur de crise) / RAF (suppléant) | [__________] / [__________] |
| Prestataire IT (astreinte) / hébergeur (n° contrat) | [__________] / [__________] |
| Banque — service fraude / avocat | [__________] / [__________] |
| maCERT (DGSSI) — signalement volontaire / police (19) | [à vérifier sur dgssi.gov.ma] / 19 |

<!-- pagebreak -->

## FICHE RÉFLEXE C — Site e-commerce piraté

**Numéro d'alerte : RI [__________]  —  hébergeur (support + n° contrat) [__________]  —  gérant [__________]**

**Page modifiée, redirection, alerte « site dangereux », client qui signale un problème ? CAPTUREZ L'ÉCRAN ET APPELEZ LE RI.**

**Signes d'alerte** : page d'accueil remplacée ; redirection vers un autre site ; alerte « site dangereux » du navigateur ou de Google Search Console ; formulaire de carte bancaire sur notre site (il ne doit jamais y en avoir) ; courriel de l'hébergeur signalant un abus ; clients qui reçoivent des hameçonnages citant leurs commandes.

| SALARIÉ — à faire | SALARIÉ — à ne pas faire |
|---|---|
| Faire une capture (URL, date, heure) | Se connecter à l'administration du site pour « réparer » |
| Appeler le RI | Répondre publiquement aux clients ou sur les réseaux |
| Prendre les commandes par téléphone | Promettre qu'« aucune donnée n'a été touchée » |

**RESPONSABLE INCIDENT — dans les 2 heures**

1. □ Registre ; variante : défiguration / fichier suspect (web shell) / script injecté / fuite de données.
2. □ Appeler l'hébergeur : **instantané fichiers + base à l'état actuel** et export des journaux, **avant** tout nettoyage.
3. □ Mettre le site **en maintenance** (ou suspension par l'hébergeur).
4. □ Changer **tous** les accès depuis un poste sain : panneau d'hébergement, FTP/SFTP/SSH, admins boutique, utilisateur MariaDB, clés d'API.
5. □ Capturer puis supprimer les comptes admin inconnus.
6. □ Paiement possiblement concerné : prévenir **le prestataire de paiement** sans délai (S1).
7. □ Données clients possiblement exposées : référent données + avocat (CNDP recommandé, RGPD si clients UE).
8. □ Reconstruire depuis le **code de référence** et une **sauvegarde saine**, après correction de la faille.

**Remise en ligne** seulement après : faille corrigée, secrets changés, fichiers vérifiés, page de paiement contrôlée. Surveillance 30 jours.

| Contact de crise | Numéro / référence |
|---|---|
| Gérant (directeur de crise) / RAF (suppléant) | [__________] / [__________] |
| Prestataire IT (astreinte) / hébergeur (n° contrat) | [__________] / [__________] |
| Banque — service fraude / avocat | [__________] / [__________] |
| maCERT (DGSSI) — signalement volontaire / police (19) | [à vérifier sur dgssi.gov.ma] / 19 |
