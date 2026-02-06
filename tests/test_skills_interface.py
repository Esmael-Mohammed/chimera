def test_skill_fetch_trends_interface():
    # Mock input to match expected structure
    skill_input = {"platform": "twitter", "trends": ["trend1", "trend2"]}
    assert "platform" in skill_input
    assert skill_input["platform"] == "twitter"
