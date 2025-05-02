from unittest.mock import patch

# Fake user input and avoid actual sleep
with patch('builtins.input', return_value='2'), \
     patch('time.sleep', return_value=None) as mock_sleep, \
     patch('services.weather_services.store_weather_data') as mock_store:

    from app import run_weather_tracker

    # Check that it called store_weather_data 6 times (3 cities * 2 hours)
    assert mock_store.call_count == 6, f"Expected 6 calls, got {mock_store.call_count}"

    # Check that sleep was called twice
    assert mock_sleep.call_count == 2, f"Expected 2 calls to sleep, got {mock_sleep.call_count}"

    print("✅ All checks passed.")
