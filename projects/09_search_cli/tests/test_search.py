from search import find_matches


def test_find_matches(tmp_path):
    (tmp_path / "one.md").write_text("Python\nbackend\n", encoding="utf-8")
    result = find_matches(tmp_path, "python")
    assert result[0]["line"] == 1
    assert result[0]["text"] == "Python"


def test_invalid_pattern(tmp_path):
    try:
        find_matches(tmp_path, "[")
    except ValueError as error:
        assert "Неверный шаблон" in str(error)
    else:
        raise AssertionError("ValueError expected")
