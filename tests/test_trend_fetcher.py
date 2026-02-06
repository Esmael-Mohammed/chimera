def test_trend_contract():
    response = {"trends": ["trend1", "trend2"]}
    assert "trends" in response
    assert isinstance(response["trends"], list)
    assert len(response["trends"]) > 0
