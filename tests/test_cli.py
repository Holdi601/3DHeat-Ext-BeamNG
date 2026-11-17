"""
The command line as someone runs it - and as 3DHeat GameFiles runs it, with
the user's own arguments: `identify` on BeamNG's files, `course` on another
game's lap, `levels` on an install built the way the game ships one.
"""

from __future__ import annotations

import io
import json
import zipfile

import pytest

from heat3d_ext_beamng.cli import main

from .beamng_fixtures import LEVEL, build_install, cdae, lap_document, road_lap, terrain_file


def run(capsys, *argv) -> tuple[int, str, str]:
    code = main([str(a) for a in argv])
    out, err = capsys.readouterr()
    return code, out, err


def level_zip(path):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as bundle:
        bundle.writestr("levels/example_level/info.json", '{"title": "Example"}')
        bundle.writestr("levels/example_level/main/items.level.json", "{}\n" * 50)
        bundle.writestr("levels/example_level/art/rock.cdae", b"\x1f" + bytes(40))
    path.write_bytes(buffer.getvalue())
    return path


class TestIdentify:
    def test_a_beamng_level_zip(self, capsys, tmp_path):
        code, out, _ = run(capsys, "identify", level_zip(tmp_path / "example_level.zip"))

        assert code == 0
        assert "zip archive, 3 entries" in out
        assert "example_level (laid out as a BeamNG.drive level)" in out

    def test_a_beamng_shape(self, capsys, tmp_path):
        path = tmp_path / "rail.cdae"
        path.write_bytes(cdae([[0, 0, 0], [4, 0, 0], [4, 0, 1]], [[0, 1, 2]], materials=("rail_mat",)))

        code, out, _ = run(capsys, "identify", path)

        assert code == 0
        assert "BeamNG.drive shape (.cdae), version 31" in out and "rail_mat" in out

    def test_a_beamng_terrain(self, capsys, tmp_path):
        path = tmp_path / "example.ter"
        path.write_bytes(terrain_file()[0])

        code, out, _ = run(capsys, "identify", path)

        assert code == 0
        assert "BeamNG.drive terrain (.ter), version 9" in out
        assert "65 x 65" in out and "Grass, Asphalt" in out

    def test_anything_else_is_not_this_games(self, capsys, tmp_path):
        other = tmp_path / "other.zip"
        with zipfile.ZipFile(other, "w") as bundle:
            bundle.writestr("readme.txt", "nothing of a level")
        for path in (other, tmp_path / "notes.txt"):
            if not path.exists():
                path.write_text("just some text\n", encoding="utf-8")
            code, out, err = run(capsys, "identify", path)
            assert code == 2 and out == ""
            assert err.strip() == f"not a BeamNG.drive file: {path.name}"

    def test_a_missing_file(self, capsys, tmp_path):
        code, _, err = run(capsys, "identify", tmp_path / "gone.cdae")
        assert code == 2 and "no such file" in err


class TestCourse:
    @pytest.mark.parametrize(
        "game, tool",
        [("forza-horizon-5", "heat3d-forza-maps"), ("assetto-corsa-rally", "heat3d-acrally-maps")],
    )
    def test_another_games_lap_names_the_tool_for_it(self, capsys, tmp_path, game, tool):
        path = tmp_path / "lap.json"
        doc = lap_document(road_lap())
        doc["game"] = game
        path.write_text(json.dumps(doc), encoding="utf-8")

        code, out, err = run(capsys, "course", path)

        assert code == 2 and out == ""
        assert f"{tool} course" in err

    def test_game_overrides_what_the_lap_says(self, capsys, tmp_path):
        path = tmp_path / "lap.json"
        path.write_text(json.dumps(lap_document(road_lap())), encoding="utf-8")

        code, _, err = run(capsys, "course", path, "--game", "forza")

        assert code == 2 and "heat3d-forza-maps" in err

    def test_no_install_is_one_line_and_exit_2(self, capsys, tmp_path):
        path = tmp_path / "lap.json"
        path.write_text(json.dumps(lap_document(road_lap())), encoding="utf-8")

        code, _, err = run(capsys, "course", path, "--install", tmp_path / "nowhere")

        assert code == 2
        assert len(err.strip().splitlines()) == 1 and "gameengine.zip" in err

    def test_every_option_of_gamefiles_course_is_taken(self, capsys, tmp_path):
        """GameFiles hands its own arguments over unchanged, the Forza ones included."""
        install = build_install(tmp_path / "game")
        lap = tmp_path / "lap.json"
        lap.write_text(json.dumps(lap_document(road_lap())), encoding="utf-8")
        out = tmp_path / "course.glb"

        code, report, _ = run(
            capsys, "course", lap, "-o", out, "--install", install, "--margin", "30", "--no-textures",
            "--season", "winter", "--track", tmp_path, "--game", "beamng", "--level", LEVEL,
            "--detail-budget", "100000", "--texture-size", "512",
        )

        assert code == 0 and out.exists()
        assert "(BeamNG.drive)" in report


class TestLevels:
    def test_the_install_and_its_levels(self, capsys, tmp_path):
        install = build_install(tmp_path / "game")

        code, out, _ = run(capsys, "levels", "--install", install)

        assert code == 0
        assert f"BeamNG.drive at {install}" in out
        assert f"  {LEVEL}" in out.splitlines()

    def test_no_install(self, capsys, tmp_path):
        code, out, err = run(capsys, "levels", "--install", tmp_path)

        assert code == 2 and out == ""
        assert len(err.strip().splitlines()) == 1 and "gameengine.zip" in err


def test_without_gamefiles_one_line_and_exit_2(capsys, monkeypatch):
    import heat3d_ext_beamng.cli as cli

    monkeypatch.setattr(cli, "find_gamefiles", lambda: False)
    code, out, err = run(capsys, "levels")
    assert code == 2 and out == ""
    assert err.strip() == "heat3d-beamng-maps: needs 3DHeat GameFiles: pip install " \
        "https://github.com/Holdi601/3DHeat-GameFiles/archive/refs/tags/v1.1.0.zip, or set HEAT3D_GAMEFILES to its folder"
