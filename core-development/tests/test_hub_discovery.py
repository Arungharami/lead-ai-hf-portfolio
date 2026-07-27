from types import SimpleNamespace

import pytest

from src.hub_discovery import discover_assets


class FakeApi:
    def list_models(self, search: str, limit: int):
        return [SimpleNamespace(id="org/model", author="org", likes=7, downloads=100, tags=[search])]

    def list_datasets(self, search: str, limit: int):
        return [SimpleNamespace(id="org/dataset", author="org", likes=3, downloads=50, tags=[search])]

    def list_spaces(self, search: str, limit: int):
        return [SimpleNamespace(id="org/space", author="org", likes=2, tags=[search])]


def test_discover_assets_returns_all_categories():
    report = discover_assets("explainable AI", limit=1, api=FakeApi())

    assert set(report) == {"models", "datasets", "spaces"}
    assert report["models"][0].repo_id == "org/model"
    assert report["datasets"][0].asset_type == "dataset"
    assert report["spaces"][0].downloads is None


@pytest.mark.parametrize("limit", [0, 51])
def test_discover_assets_rejects_invalid_limit(limit: int):
    with pytest.raises(ValueError, match="between 1 and 50"):
        discover_assets("test", limit=limit, api=FakeApi())


def test_discover_assets_rejects_empty_query():
    with pytest.raises(ValueError, match="must not be empty"):
        discover_assets("   ", api=FakeApi())
