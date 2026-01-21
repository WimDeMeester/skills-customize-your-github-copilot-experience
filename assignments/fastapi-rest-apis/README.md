# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Leer hoe je moderne RESTful APIs bouwt met het FastAPI-framework in Python. Je bouwt een kleine API met endpoints om data te maken, op te vragen en te valideren.

`Due date:` 2026-01-28

## 📝 Tasks

### 🛠️ Task 1 — Basis API

#### Description
Maak een eenvoudige REST API met FastAPI die de volgende endpoints biedt:

- `GET /` — basis health-check
- `POST /items/` — maak een nieuw item (JSON body)
- `GET /items/{item_id}` — haal een item op

#### Requirements

Een voltooid project moet:

- FastAPI gebruiken voor routing en request validation
- Pydantic models gebruiken voor invoer- en uitvoervalidatie
- Werkende voorbeelden tonen hoe de server lokaal te starten

### 🛠️ Task 2 — Optionele uitbreidingen (bonus)

#### Description
Voeg één of meer van de volgende opties toe voor extra punten:

- persistente opslag (bijv. JSON-bestand of SQLite)
- extra endpoints (`PUT`, `DELETE`, query-parameters)
- authenticatie (API key of eenvoudige token)
- automatische OpenAPI-documentatie uitbreiden (beschrijvingen / voorbeelden)

## 📂 Starter bestanden

- `assignments/fastapi-rest-apis/starter-code.py` — minimale FastAPI-app en run-instructies

## 🔎 Beoordelingscriteria

- API werkt lokaal en voldoet aan de basis-eindpunten
- heldere Pydantic-modellen en invoervalidatie
- eenvoudige, leesbare en goed gestructureerde code

## 📤 Inleverinstructies

1. Werk in de map `assignments/fastapi-rest-apis/` en sla je code op in `starter-code.py` of extra modules.
2. Voeg in de README korte startinstructies toe (zie voorbeeld hieronder).

### Startinstructie (voorbeeld)

1. Installeer afhankelijkheden:

```bash
python3 -m pip install fastapi uvicorn
```

2. Start de server:

```bash
python3 starter-code.py
```

3. Open de docs: http://127.0.0.1:8000/docs

Als je wilt, kan ik de starter-code nakijken of uitbreiden met extra features.