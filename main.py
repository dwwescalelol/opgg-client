from pathlib import Path

from clients.client import OPGGClient
from models.base_model import BaseResponse
from models.shared import Region
from tests.test_client import JSON_EXTENTION, DataPaths

client = OPGGClient(region=Region.EUW)
TEST_SUMMONER_ID = "r5WSLNaMXFIpGO-vdtQCHzPjGBTMQB-7JkMjHkpsgdT3qJg"


def save_json_test_data(filename: str, data: BaseResponse) -> dict:
    """Helper function to load JSON test data."""
    test_data_path = (
        Path(__file__).parent
        / "tests"
        / DataPaths.DIR.value
        / "match_history"
        / filename
    )
    with open(
        test_data_path.with_suffix(JSON_EXTENTION),
        "w",
        encoding="utf-8",
    ) as file:
        file.write(data.model_dump_json())


for g in client.get_all_match_history(summoner_id=TEST_SUMMONER_ID):
    print("hello")
    save_json_test_data(filename=str(g.meta.last_game_created_at)[:10], data=g)


client.get_champ_stats(TEST_SUMMONER_ID)

client.get_champion_metadata()
