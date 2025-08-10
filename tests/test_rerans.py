import  pytest
import  random

@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_rerans():
    assert random.choice([True, False])