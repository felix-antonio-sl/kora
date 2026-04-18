#!/usr/bin/env python3
"""Deprecated compatibility alias for prepare_atomic_fidelity_review.py."""

from __future__ import annotations

import sys

from prepare_atomic_fidelity_review import main


if __name__ == "__main__":
    print(
        "Deprecated: use prepare_atomic_fidelity_review.py; this alias only prepares the review packet.",
        file=sys.stderr,
    )
    raise SystemExit(main())
