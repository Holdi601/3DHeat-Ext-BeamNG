"""The standalone app on a synthetic BeamNG.drive install (tiny fake files, no game data)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from heat3d_ext_beamng import standalone_spec
from heat3d_ext_beamng.app import entry, update


@pytest.fixture(autouse=True)
def _isolated(tmp_path, monkeypatch):
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "appdata"))
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "appdata"))
    monkeypatch.setenv("HEAT3D_LEVELS", str(tmp_path / "levels"))
    monkeypatch.setenv("HEAT3D_NO_UPDATE", "1")
    update.AUTO_THIS_RUN = False


def _install(tmp_path: Path) -> Path:
    game = tmp_path / "BeamNG.drive"
    (game / "content" / "levels").mkdir(parents=True)
    (game / "gameengine.zip").write_bytes(b"PK\x05\x06" + b"\0" * 18)
    return game


def test_find_from_a_chosen_folder(tmp_path):
    game = _install(tmp_path)
    find = standalone_spec.SPEC.games[0].find
    assert find(str(game)) == game
    assert find(str(game / "content")) is None
    assert find(str(tmp_path / "elsewhere")) is None


def test_tasks_take_the_chosen_install(tmp_path, monkeypatch, capsys):
    game = _install(tmp_path)
    spec = standalone_spec.SPEC
    monkeypatch.setattr(standalone_spec, "game_folders", lambda s, given=None: {"beamng": game})
    tasks = {t.id: t for t in spec.tasks}
    argv = tasks["course"].argv({"lap": "lap.csv"}, tmp_path / "levels")
    assert argv == ["heat3d-beamng-maps", "course", "lap.csv", "--install", str(game)]
    assert tasks["levels"].argv({}, tmp_path / "levels")[:2] == ["heat3d-beamng-maps", "levels"]
    for t in spec.tasks:
        assert t.argv({i.key: "x" for i in t.inputs}, tmp_path)[0] in spec.tools


def test_status_has_no_maps_and_extract_says_so(capsys):
    spec = standalone_spec.SPEC
    assert not spec.has_maps()
    assert entry.main(spec, ["status", "--json"]) == 0
    doc = json.loads(capsys.readouterr().out)
    assert doc["id"] == "heat3d-beamng" and doc["games"][0]["maps"] == []
    assert entry.main(spec, ["extract", "--new", "--progress-json"]) == 0
    lines = [json.loads(l) for l in capsys.readouterr().out.splitlines() if l.startswith("{")]
    assert lines[-1] == {"event": "done", "ok": 0, "failed": 0}
