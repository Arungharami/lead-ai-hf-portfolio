"""Discover Hugging Face Hub assets and save a structured report."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from huggingface_hub import HfApi


@dataclass(frozen=True)
class HubAsset:
    asset_type: str
    repo_id: str
    author: str | None
    likes: int
    downloads: int | None
    tags: list[str]


def _to_asset(asset_type: str, item: Any) -> HubAsset:
    repo_id = getattr(item, "id", None) or getattr(item, "modelId", None)
    if not repo_id:
        raise ValueError(f"Unable to determine repository ID for {asset_type}")

    return HubAsset(
        asset_type=asset_type,
        repo_id=repo_id,
        author=getattr(item, "author", None),
        likes=int(getattr(item, "likes", 0) or 0),
        downloads=getattr(item, "downloads", None),
        tags=list(getattr(item, "tags", None) or []),
    )


def discover_assets(query: str, limit: int = 5, api: HfApi | None = None) -> dict[str, list[HubAsset]]:
    """Search models, datasets, and Spaces using one query."""
    if not query.strip():
        raise ValueError("query must not be empty")
    if limit < 1 or limit > 50:
        raise ValueError("limit must be between 1 and 50")

    client = api or HfApi()
    models = [_to_asset("model", item) for item in client.list_models(search=query, limit=limit)]
    datasets = [
        _to_asset("dataset", item) for item in client.list_datasets(search=query, limit=limit)
    ]
    spaces = [_to_asset("space", item) for item in client.list_spaces(search=query, limit=limit)]
    return {"models": models, "datasets": datasets, "spaces": spaces}


def save_report(report: dict[str, list[HubAsset]], output: Path) -> None:
    """Write a discovery report as formatted JSON."""
    output.parent.mkdir(parents=True, exist_ok=True)
    serializable = {
        category: [asdict(asset) for asset in assets] for category, assets in report.items()
    }
    output.write_text(json.dumps(serializable, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True, help="Search phrase, such as 'explainable AI'")
    parser.add_argument("--limit", type=int, default=5, help="Results per asset type (1-50)")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("reports/discovery.json"),
        help="JSON report destination",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report = discover_assets(args.query, args.limit)
    save_report(report, args.output)
    print(f"Saved discovery report to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
