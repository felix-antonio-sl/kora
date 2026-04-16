# Boot — kora/korax

## On startup

1. Check PCA status: GET http://kora-pca:8100/api/estado — verify API responds
2. Check MEMORY.md for last known state and pending items
3. If PCA is down or critical issues found, report via message tool to operator
4. If all OK, reply with NO_REPLY
