# Politique de réponse aux incidents de sécurité

| Référence | Version | Date | Propriétaire | Approbation |
|---|---|---|---|---|
| AGS-POL-IR-01 | 1.0 | 2026-10 | Responsable informatique | Gérant d'AgriSouss SARL |

## 1. Objet et champ d'application

Cette politique définit comment AgriSouss SARL détecte, traite, communique et tire les leçons des incidents de sécurité de l'information. Elle s'applique à tous les salariés, stagiaires et prestataires, et à tous les actifs : comptes Google Workspace, postes de travail, NAS, réseau du bureau, site e-commerce et sa base de données, téléphones utilisés pour le travail.

**Événement** : fait observable (alerte antivirus, courriel suspect, lenteur). **Incident** : événement qui compromet ou menace la confidentialité, l'intégrité ou la disponibilité d'une information ou d'un service, ou qui viole la politique de sécurité. Tout incident est un événement ; tout événement n'est pas un incident.

Principes :

1. **Signaler vite, sans crainte.** Un salarié qui a cliqué sur un lien ou ouvert une pièce jointe le signale immédiatement. Aucune sanction n'est prise pour un signalement de bonne foi ; la sanction concerne la dissimulation.
2. **Protéger d'abord les personnes et l'activité**, puis les preuves, puis le confort technique.
3. **Documenter tout** dans le registre d'incidents (date, heure, auteur, action).
4. **Ne jamais payer de rançon** sans décision écrite du gérant après avis juridique ; la position par défaut est le refus (arguments dans le playbook B et dans LEARN.md).

## 2. Rôles et responsabilités

| Rôle | Titulaire (fictif) | Suppléant | Missions principales |
|---|---|---|---|
| Responsable de l'incident (RI) | Informaticien interne | Prestataire externe | Pilote technique, tient le registre, décide du confinement immédiat |
| Directeur de crise | Gérant | Responsable administratif et financier (RAF) | Décisions métier, budget, communication externe, plainte |
| Prestataire IT externe | Société de maintenance sous contrat | — | Renfort technique, réinstallation, analyse |
| Hébergeur web | Fournisseur d'hébergement | — | Journaux serveur, instantanés, restauration, blocage |
| Référent données personnelles | RAF | Gérant | Évalue l'impact sur les données clients/salariés, prépare l'éventuelle démarche CNDP |
| Conseil juridique | Avocat externe | — | Obligations légales, plainte, contrats, rançon |
| Salariés | Tous | — | Détecter, signaler, appliquer les consignes |

### Matrice RACI

R = réalise, A = rend des comptes (un seul A par ligne), C = consulté, I = informé.

| Activité | Gérant | RI (IT interne) | Prestataire IT | Hébergeur | Référent données | Avocat | Salariés |
|---|---|---|---|---|---|---|---|
| Signaler un événement | I | I | — | — | — | — | R |
| Qualifier et classer la gravité | C | A/R | C | — | C | — | — |
| Confinement immédiat (isoler PC, bloquer compte) | I | A/R | R | R (site) | — | — | C |
| Décider l'arrêt d'un service métier (site, NAS) | A | R | C | C | C | — | I |
| Collecte et conservation des preuves | I | A/R | R | R (journaux) | — | C | — |
| Éradication et restauration | I | A | R | R (site) | — | — | — |
| Évaluer l'impact sur les données personnelles | C | C | — | C | A/R | C | — |
| Démarche CNDP / information des personnes | A | C | — | — | R | C | — |
| Signalement maCERT / plainte police | A | R | C | — | — | C | — |
| Communication aux clients et partenaires | A/R | C | — | — | C | C | I |
| Communication interne | A | R | — | — | — | — | I |
| Retour d'expérience et plan d'actions | A | R | C | C | C | — | I |

## 3. Niveaux de gravité

La gravité est fixée par le RI lors du triage, puis révisée à chaque point de situation. En cas de doute entre deux niveaux, on prend le **plus élevé**.

| Niveau | Nom | Critères (au moins un) | Exemples | Délai de prise en charge | Escalade |
|---|---|---|---|---|---|
| S1 | Critique | Arrêt de l'activité ; chiffrement de plusieurs postes ou du NAS ; fuite avérée de données clients ou bancaires ; fraude financière en cours | Rançongiciel sur le NAS, base clients publiée, virement frauduleux | Immédiat, 24 h/24 | Gérant appelé immédiatement ; prestataire mobilisé ; avocat sous 24 h |
| S2 | Élevé | Compte à privilèges ou compte du gérant/compta compromis ; site défiguré ou web shell ; un poste chiffré isolé | Compte Gmail de la comptable piraté, page d'accueil défigurée | < 1 h ouvrée | Gérant informé < 1 h |
| S3 | Modéré | Compte standard compromis sans fraude constatée ; malware bloqué mais exécuté ; vol d'un PC chiffré | Mot de passe saisi sur une fausse page, MFA active | < 4 h ouvrées | Gérant informé le jour même |
| S4 | Faible | Tentative bloquée, sans impact | Courriel d'hameçonnage signalé sans clic | < 1 jour ouvré | Synthèse mensuelle |

Facteurs aggravants qui font monter d'un niveau : données personnelles de plus de 100 personnes concernées, données de paiement, implication d'un partenaire ou d'un client B2B, couverture médiatique ou publique, récurrence.

## 4. Escalade et circuit d'alerte

1. Le salarié signale par **téléphone** au RI (pas seulement par courriel : la messagerie peut être compromise). Numéro affiché sur chaque poste et dans la fiche réflexe.
2. Le RI ouvre une entrée dans le **registre d'incidents** (tableur hors ligne + copie papier en S1), qualifie et classe.
3. S1/S2 : le RI appelle le gérant ; si injoignable sous 15 min, le RAF. Le prestataire IT est appelé selon les termes du contrat (vérifier le délai d'intervention contractuel).
4. Points de situation : S1 toutes les 2 h, S2 deux fois par jour, jusqu'à clôture.
5. Canal de crise hors bande : **groupe WhatsApp/Signal « Crise AgriSouss »** créé à l'avance avec gérant, RI, RAF, prestataire, plus une liste papier des numéros. On n'utilise pas un compte Google potentiellement compromis pour coordonner la crise.

Annuaire de crise (à tenir à jour, une copie papier dans le coffre du bureau) : gérant, RI, RAF, prestataire IT (numéro astreinte), hébergeur (support + numéro de contrat), banque (service fraude), avocat, assureur éventuel, maCERT/DGSSI, police judiciaire.

## 5. Communication

### 5.1 Interne

- Un seul porte-parole interne (gérant), messages préparés par le RI.
- Message factuel : ce qui se passe, ce qu'on attend des salariés, ce qu'il ne faut pas faire (ne pas éteindre/rallumer, ne pas rebrancher, ne pas parler à l'extérieur).
- Pas de détails techniques inutiles, pas de recherche de coupable.

### 5.2 Clients, partenaires, fournisseurs

- Décidée par le gérant, après avis du référent données et, si besoin, de l'avocat.
- Prévenir **rapidement** les partenaires exposés (ex. : ils ont reçu des courriels frauduleux depuis notre domaine ou des demandes de changement de RIB).
- Ne jamais promettre ce qu'on ne sait pas (« aucune donnée n'a été touchée ») avant la fin de l'analyse. Dire ce qu'on sait, ce qu'on fait, ce que la personne peut faire, et quand on reviendra vers elle.
- Les modèles de messages sont dans chaque playbook.

### 5.3 Autorités : obligatoire ou recommandé ?

Cette section distingue ce qui est, selon notre lecture, **obligatoire** pour une PME privée et ce qui est **recommandé**. À valider par un juriste.

| Destinataire | Base | Situation d'AgriSouss | Statut |
|---|---|---|---|
| **CNDP** (Commission nationale de contrôle de la protection des données à caractère personnel) | Loi 09-08 : obligation de sécurité des traitements (art. 23), déclaration ou autorisation préalable des traitements, droits des personnes | La loi 09-08 ne contient pas, à notre connaissance, d'obligation générale et explicite de notifier une violation de données dans un délai fixé, à la différence de l'art. 33 du RGPD. Une réforme de la loi est discutée. | **Fortement recommandé** de contacter la CNDP en cas de fuite de données personnelles, et d'informer les personnes concernées quand elles courent un risque (fraude, hameçonnage ciblé). Vérifier l'état du droit et les délibérations récentes de la CNDP au moment de l'incident. |
| **RGPD** (UE) | Art. 3(2) : s'applique si l'on cible des personnes situées dans l'UE (vente en ligne vers l'UE) | Possible si la boutique livre ou cible des clients européens | Si applicable : notification à l'autorité compétente sous 72 h et information des personnes en cas de risque élevé. À faire analyser par l'avocat. |
| **DGSSI / maCERT** (CERT national) | Loi 05-20 et décret 2-21-406 : obligation de déclarer les incidents pour les administrations, établissements publics, infrastructures d'importance vitale (IIV) et certains opérateurs | AgriSouss n'est ni administration ni IIV | **Non obligatoire, recommandé.** Signalement volontaire utile : maCERT peut aider à qualifier une menace, et le signalement améliore la connaissance nationale des attaques. Coordonnées à vérifier sur le site de la DGSSI. |
| **Police judiciaire / parquet** | Loi 07-03 (art. 607-3 et suivants du Code pénal) ; escroquerie | Intrusion, rançongiciel, fraude au virement | **Recommandé**, et souvent **exigé en pratique** par la banque (contestation de virement) et par un assureur. Déposer plainte avec les preuves conservées. |
| **Banque** | Contrat bancaire | Virement frauduleux | **Urgent** : appeler le service fraude immédiatement ; les chances de rappel des fonds baissent très vite. |
| **Assureur** | Contrat | Si une police cyber est souscrite | Selon contrat : délai de déclaration souvent court, et l'assureur peut imposer ses prestataires. |
| **CMI / prestataire de paiement** | Contrat commerçant, PCI DSS | Si la page de paiement ou des données de carte peuvent être concernées | **Contractuel** : prévenir le prestataire sans délai. |

## 6. Gestion des preuves et chaîne de possession

Objectif : pouvoir comprendre l'attaque, la prouver (plainte, assurance, litige) et ne pas détruire d'indices en voulant réparer.

Règles :

1. **Ne pas éteindre** un poste suspect sans raison : l'isoler du réseau (câble, Wi-Fi, mode avion). Exception : chiffrement en cours et impossibilité d'isoler, voir playbook rançongiciel.
2. Collecter dans l'**ordre de volatilité** (RFC 3227) : mémoire et connexions actives, puis disque, puis journaux distants (Google Workspace, hébergeur), puis sauvegardes et supports d'archive.
3. Travailler sur des **copies** ; calculer une empreinte **SHA-256** de chaque fichier ou image au moment de la collecte et la noter.
4. Photographier les écrans (note de rançon, défiguration) avec date et heure visibles.
5. Exporter les journaux cloud **tôt** : leur durée de rétention est limitée (elle dépend de l'édition Google Workspace et de l'offre d'hébergement).
6. Stocker les preuves sur un support dédié, étiqueté, rangé sous clé ; accès limité au RI et au gérant.
7. Tenir une **fiche de chaîne de possession** pour chaque élément.

Modèle de fiche de chaîne de possession :

| Champ | Contenu |
|---|---|
| N° de preuve | INC-2026-007-P03 |
| Description | Image disque du PC « COMPTA-02 » (SSD 256 Go), ou export CSV du journal de connexion Google |
| Source | Poste, numéro de série, utilisateur ; ou console et requête utilisées |
| Collecté par / date / heure | Nom, signature, horodatage avec fuseau (Africa/Casablanca) |
| Méthode et outil | Outil et version, bloqueur d'écriture le cas échéant |
| Empreinte SHA-256 | Valeur notée à la collecte |
| Lieu de stockage | Armoire fermée, bureau du gérant, disque étiqueté P03 |
| Transferts | Date, de qui à qui, motif, signatures des deux parties |

Si une analyse judiciaire est probable (plainte, fraude importante), demander l'avis de l'avocat **avant** toute manipulation lourde et faire intervenir un prestataire spécialisé en investigation numérique.

## 7. Registre, retour d'expérience et amélioration

- Chaque incident S1 à S3 donne lieu à une **réunion de retour d'expérience** sous 10 jours ouvrés après la clôture : chronologie, ce qui a marché, ce qui a manqué, actions avec responsable et date.
- Indicateurs suivis (voir playbooks) : MTTD (délai moyen de détection), MTTA (délai de prise en charge), MTTC (délai de confinement), MTTR (délai de rétablissement), nombre de signalements par les salariés, taux de clic aux campagnes de sensibilisation.
- **Exercice sur table** au moins une fois par an (kit fourni) ; test de restauration des sauvegardes au moins une fois par trimestre.
- Révision de la politique : annuelle, ou après tout incident S1/S2.
