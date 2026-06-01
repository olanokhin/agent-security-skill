# Example `owasp my code` Report

Target: `examples/unsafe.py`

## CRITICAL / HIGH Findings

```text
🚨 LAYER 1 · LLM01 · HIGH
Location: examples/unsafe.py:11
Issue: Raw user input is concatenated into an instruction-bearing prompt, allowing prompt injection to alter model behavior.
Fix: Keep system instructions in a system message and pass user-controlled content as a separate user message or delimited data block.
```

```text
🚨 LAYER 2 · PIPE01 · HIGH
Location: examples/unsafe.py:18
Issue: Retrieved external content is inserted into the prompt without isolation, so a poisoned document can inject instructions.
Fix: Wrap retrieved content in explicit delimiters and instruct the model to treat it as untrusted data only.
```

```text
🚨 LAYER 1 · LLM10 · HIGH
Location: examples/unsafe.py:28
Issue: The LLM call has no token, timeout, request, or cost controls.
Fix: Set explicit output token limits, timeouts, and request/cost budgets for model calls.
```

```text
🚨 LAYER 3 · ASI05 · CRITICAL
Location: examples/unsafe.py:37
Issue: Agent tool execution passes model/user-controlled text to a shell command with shell=True.
Fix: Remove shell=True, use an allowlisted command interface, validate arguments, and run tools in a sandbox with timeouts.
```

```text
🚨 LAYER 1 · LLM06 · HIGH
Location: examples/unsafe.py:40
Issue: The agent can delete arbitrary files without approval or path restrictions.
Fix: Restrict file operations to an allowlisted workspace path and require verified confirmation before destructive actions.
```

```text
🚨 LAYER 2 · PIPE13 · HIGH
Location: examples/unsafe.py:47
Issue: A package name suggested by an LLM can be installed automatically, enabling hallucination-driven dependency attacks.
Fix: Require human review and verify package identity, publisher, version, and integrity before installation.
```

## Notes

This fixture intentionally contains insecure code. It exists to show what the skill should catch when a user runs:

```text
owasp my code
```
