# IR Playbooks PME — Dispositif de réponse aux incidents pour une PME marocaine

Projet de portfolio en cybersécurité (réponse aux incidents / GRC). Il fournit un dispositif complet de réponse aux incidents pour **AgriSouss SARL**, une PME agricole **fictive** du Souss (~15 salariés, boutique PHP/MariaDB chez un hébergeur, Google Workspace, postes Windows, un NAS, un informaticien et un prestataire externe). C'est la même entreprise fictive que dans le projet GRC du portfolio, décrite environ 12 mois après le plan d'action de l'audit (d'où Google Workspace, le NAS sauvegardé et l'informaticien, absents au moment de l'audit ; voir `docs/00-introduction.md`).

> **Contenu uniquement défensif.** Entreprise, personnes et incidents fictifs. Les éléments juridiques sont une lecture des textes publics par l'auteur, pas un avis juridique.

## Contenu (FR)

| Fichier | Contenu |
|---|---|
| `docs/00-introduction.md` | Contexte, hypothèses, référentiels, correspondance NIST r2 / SANS / CSF 2.0 |
| `docs/01-politique-reponse-incidents.md` | Politique : rôles et RACI, niveaux de gravité S1-S4, escalade, communication, autorités (obligatoire vs recommandé : CNDP / loi 09-08, DGSSI-maCERT / loi 05-20, plainte / loi 07-03), preuves et chaîne de possession |
| `docs/02-playbook-phishing-bec.md` | Playbook A : hameçonnage et compte Google Workspace compromis (BEC) |
| `docs/03-playbook-ransomware.md` | Playbook B : rançongiciel sur poste ou NAS |
| `docs/04-playbook-compromission-site-web.md` | Playbook C : défiguration, web shell, fuite de données sur le site e-commerce |
| `docs/05-exercice-tabletop-ransomware.md` | Kit d'exercice sur table : 6 injects chronométrés, guide d'animation, questions, grille /28, RETEX d'exemple **simulé** |
| `docs/06-fiches-reflexes.md` | Trois fiches réflexes d'une page, imprimables |
| `diagrams/*.mmd` | Arbres de décision Mermaid extraits des playbooks (générés par le script) |
| `output/AgriSouss-Reponse-Incidents.pdf` | Le dossier complet en PDF : page de titre, sommaire, signets |
| `build/build_pdf.py` | Générateur PDF (reportlab), Markdown → PDF |
| `LEARN.md` | Notes de révision : NIST vs SANS, confinement, volatilité, rançon, communication, 15 questions d'entretien, ligne de CV |

Chaque playbook contient : déclencheurs et sources de détection, check-list de triage, arbre de décision (Mermaid), étapes de confinement / éradication / rétablissement, preuves à collecter, modèles de messages (salariés, clients), check-list post-incident, indicateurs (MTTD, MTTC, MTTR...).

**Référentiels** : NIST SP 800-61 Rev. 2 (phases), NIST SP 800-61 Rev. 3 (avril 2025, profil CSF 2.0), SANS PICERL, RFC 3227.

### Régénérer le PDF

```bash
pip install reportlab
python build/build_pdf.py
```

Le script cherche des polices TrueType (Arial/Consolas sous Windows, DejaVu sous Linux) pour les accents et symboles.

**Limite connue** : les arbres de décision ne sont **pas rendus en image** dans le PDF ; ils y figurent en source Mermaid (texte). Ils s'affichent graphiquement sur GitHub dans les fichiers `docs/*.md`, ou en collant un fichier `diagrams/*.mmd` dans mermaid.live.

## English summary

A portfolio incident-response package for a **fictional** Moroccan agricultural SME (≈15 staff, PHP/MariaDB web shop at an external host, Google Workspace, Windows PCs, a NAS, no dedicated security staff). Written in **French** for the target audience.

- **Incident response policy**: roles and RACI matrix, S1–S4 severity levels, escalation path with an out-of-band crisis channel, internal and customer communication, and an honest "mandatory vs. recommended" table for Moroccan authorities (CNDP under Law 09-08, which to the author's reading has no explicit general breach-notification duty; DGSSI/maCERT under Law 05-20, mandatory only for public bodies, critical infrastructure and some operators, so voluntary here; police complaint under Law 07-03; GDPR if EU customers are targeted). Evidence handling and chain of custody.
- **Three playbooks**: phishing / compromised Google account (BEC), ransomware on a PC or NAS, website compromise (defacement, web shell, customer data leak). Each has triggers, triage checklist, Mermaid decision tree, containment / eradication / recovery, evidence list, staff and customer message templates, post-incident checklist and KPIs.
- **Tabletop exercise kit** for the ransomware case: 6 timed injects, facilitator guide, participant questions, a 28-point evaluation grid and a sample after-action report clearly marked as **simulated**.
- **One-page quick-reaction sheets** for each playbook.
- A **Python/reportlab build script** that turns the Markdown into a single PDF with title page, table of contents and bookmarks. Decision trees appear as Mermaid source text in the PDF (not rendered images).
- Aligned with NIST SP 800-61 r2 phases and SANS PICERL, with the mapping to NIST SP 800-61 r3 (2025) / CSF 2.0 functions.

**Disclaimer**: defensive content only; fictional company and events; legal notes are not legal advice.

## Auteur / Author

Mohamed Elansari — élève ingénieur en cybersécurité, Universiapolis Agadir (Maroc). Licence MIT.
