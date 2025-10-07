def test_metadata_fixture_available(test_metadata):
    assert "search" in test_metadata["categories"]
