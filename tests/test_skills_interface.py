def test_skill_io_contract():
    input_payload = {"audio": "file.wav"}
    output_payload = {"text": "transcription"}

    assert "audio" in input_payload
    assert "text" in output_payload
