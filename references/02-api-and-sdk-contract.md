# API and SDK contract snapshot

**Classification:** PUBLIC-SOURCE snapshot / PUBLIC-DERIVED
**Snapshot date:** 2026-09-17

Re-check the live documentation before implementation because model identifiers, limits,
SDK behavior, pricing, and request details can change.

Snapshot used by this implementation skill:

- hosted base URL: `https://api.typesafe.ai`;
- System One endpoint: `POST /v1/systemone`;
- models endpoint: `GET /v1/models`;
- bearer authorization;
- standard runtime API-key environment variable: `TYPESAFE_API_KEY`;
- Python package: `typesafe-sdk`;
- Python client: `TypeSafeClient`;
- Python primitives: `Choice`, `Noul`, `Score`;
- JavaScript package: `@typesafe-ai/sdk`;
- default/current model identifier in the source snapshot: `jev-latest`.

The skill itself does not call these endpoints and requires no credentials.

## Python request pattern

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

state = {"ticket": {"text": "..."}}
questions = {
    "route": Choice(
        instructions="Which supplied route best fits the ticket?",
        criteria={"billing": "...", "technical": "...", "other": "..."},
    ),
    "needs_human": Noul(
        instructions="Does resolving this ticket require a policy decision absent from state?"
    ),
    "urgency": Score(
        instructions="How urgent is the issue based only on the supplied ticket?",
        criteria=["low: ...", "moderate: ...", "high: ..."],
    ),
}

with TypeSafeClient() as client:
    response = client.system_one(state=state, questions=questions)
```

Do not copy a key into code to make this sample work. Configure runtime credentials by
the target application's ordinary secret mechanism.

## Raw HTTP shape snapshot

```json
{
  "model": "jev-latest",
  "state": {"document": "..."},
  "questions": {
    "category": {
      "type": "choice",
      "instructions": "Which category best fits the document?",
      "criteria": {"a": null, "b": null, "other": null}
    }
  }
}
```

## Retry snapshot

The researched Python SDK snapshot included transport retries for connection/timeout
errors and selected HTTP statuses. Treat SDK retry defaults as implementation details to
re-check, not policy. Semantic uncertainty is not a transport failure and should not be
"retried until agreeable."
